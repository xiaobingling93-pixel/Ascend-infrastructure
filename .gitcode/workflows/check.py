import os
import sys
import yaml
import requests
import argparse
from typing import Dict, List, Any, Optional, Set

GITCODE_BASE_URL = "https://api.gitcode.com/api/v5/"

class RobotConfigChecker:
    def __init__(self, token: str = ""):
        self.token = token or os.environ.get("GITCODE_TOKEN")

        self.session = requests.Session()
        if self.token:
            self.session.params = {"access_token": self.token}

        self.errors = []
        self.org_repos_cache = {} # cache org -> set of repo full names

    def add_error(self, message: str):
        self.errors.append(message)

    def get_org_repos(self, org: str) -> Set[str]:
        """Fetch all repositories for an organization using OpenAPI."""
        if org in self.org_repos_cache:
            return self.org_repos_cache[org]

        if not self.token:
            return set()

        repo_names = set()
        page = 1
        per_page = 100

        try:
            while True:
                url = f"{GITCODE_BASE_URL}orgs/{org}/repos"
                params = {"page": page, "per_page": per_page}
                response = self.session.get(url, params=params, timeout=15)

                if response.status_code != 200:
                    print(f"Warning: Failed to fetch repos for org {org}: {response.status_code}")
                    break

                data = response.json()
                if not data:
                    break

                for r in data:
                    html_url = r.get("html_url", "")
                    if html_url:
                        # 移除前缀 https://gitcode.com/ 并转为小写
                        repo_path = html_url.replace("https://gitcode.com/", "").strip("/").lower()
                        repo_names.add(repo_path)

                if len(data) < per_page:
                    break
                page += 1
        except Exception as e:
            print(f"Error fetching repos for org {org}: {e}")

        self.org_repos_cache[org] = repo_names
        return repo_names

    def check_repo_exists(self, repo_path: str) -> bool:
        """Check if repo exists by looking up in organization's repo list."""
        if not self.token:
            return True # Skip if no token

        parts = repo_path.split('/')
        if len(parts) != 2:
            return False

        org = parts[0]
        org_repos = self.get_org_repos(org)

        # If cache is empty but we have a token, it might be a fetch failure or no access
        # Fallback to direct check if org list is empty to be safe
        if not org_repos:
            url = f"{GITCODE_BASE_URL}repos/{repo_path}"
            try:
                response = self.session.get(url, timeout=10)
                print(f"DEBUG: Direct check for {repo_path}, status: {response.status_code}")
                return response.status_code == 200
            except Exception as e:
                print(f"DEBUG: Direct check for {repo_path} failed with exception: {e}")
                return False

        exists = repo_path.lower() in org_repos
        if not exists:
            print(f"DEBUG: {repo_path} not found in org {org} repo list (total {len(org_repos)} repos)")
            print(f"DEBUG: Org {org} repo list contents: {sorted(list(org_repos))}")
        return exists

    def run_check(self, config_path: str):
        if not os.path.exists(config_path):
            self.add_error(f"Config file not found: {config_path}")
            return False # 注意：这里返回False，但依然会生成result.md

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except Exception as e:
            self.add_error(f"Failed to parse YAML: {e}")
            return False

        if not config or 'configs' not in config:
            self.add_error("Missing 'configs' root element")
            return False

        for idx, item in enumerate(config['configs']):
            self.validate_item(item, idx)

        # 即使有错误，也返回False，确保生成报告
        return len(self.errors) == 0

    def validate_item(self, item: Dict[str, Any], index: int):
        # 1. Check lgtm_need_nums and approve_need_nums (0 < val < 10)
        for field in ['lgtm_need_nums', 'approve_need_nums']:
            val = item.get(field)
            if not isinstance(val, int) or not (0 < val < 10):
                self.add_error(f"{field} 必须是 1-9 之间的整数 (当前值: {val})")

        # 2. Check branch_configs and each branch's merge_method
        branch_configs = item.get('branch_configs', [])
        if not isinstance(branch_configs, list) or len(branch_configs) == 0:
            self.add_error(f"缺少 branch_configs 或 branch_configs 不是列表")
        else:
            valid_methods = ['squash', 'merge', 'rebase']
            for bi, bc in enumerate(branch_configs):
                if not isinstance(bc, dict):
                    self.add_error(f"branch_configs 必须是映射类型")
                    continue
                method = bc.get('merge_method')
                if method not in valid_methods:
                    self.add_error(
                        f"merge_method 必须是 {valid_methods} 之一 (当前值: {method})"
                    )
                # 每个 branch_configs 项必须有 branch 字段或 is_default: true
                has_branch = 'branch' in bc
                is_default = bc.get('is_default') is True
                if not has_branch and not is_default:
                    self.add_error(
                        f"branch_configs 必须包含 'branch' 字段或设置 'is_default: true'"
                    )

        # 3. Check repos format (org/repo) and existence
        repos = item.get('repos', [])
        if not isinstance(repos, list):
            self.add_error(f"repos 字段必须是列表")
        else:
            for repo in repos:
                if not isinstance(repo, str) or '/' not in repo or len(repo.split('/')) != 2:
                    self.add_error(f"仓库名 '{repo}' 格式错误，必须为 '组织/仓库' 格式")
                elif not self.check_repo_exists(repo):
                    self.add_error(f"仓库 '{repo}' 不存在")

    # >>>>>>>>>>>> 新增：生成 result.md 的逻辑 <<<<<<<<<<<<
    def generate_result_md(self):
        """
        生成 result.md 文件，输出格式为 markdown 表格
        参考了 print_results 的逻辑，将扁平的错误列表整理为表格形式
        """
        # 1. 数据预处理：将扁平的 self.errors 列表分类，以便填入表格
        # 注意：这里通过关键词匹配来归类，因为 validate_item 中是将所有错误混在一起的
        errors_by_category = {
            "字段数值错误": [],        # 对应 lgtm/approve 数值检查
            "branch_configs结构错误": [],  # 对应 branch_configs 缺失/格式错误
            "合并策略错误": [],        # 对应 merge_method 检查
            "仓库格式错误": [],        # 对应 repos 格式检查
            "仓库存在性错误": [],      # 对应 repo 不存在检查
            "其他错误": []             # 兜底分类
        }

        for error in self.errors:
            categorized = False
            if "lgtm_need_nums" in error or "approve_need_nums" in error:
                errors_by_category["字段数值错误"].append(error)
                categorized = True
            elif "merge_method" in error:
                errors_by_category["合并策略错误"].append(error)
                categorized = True
            elif "branch_configs" in error:
                errors_by_category["branch_configs结构错误"].append(error)
                categorized = True
            elif "格式错误" in error or "repos 字段必须是列表" in error:
                errors_by_category["仓库格式错误"].append(error)
                categorized = True
            elif "不存在" in error:
                errors_by_category["仓库存在性错误"].append(error)
                categorized = True

            if not categorized:
                errors_by_category["其他错误"].append(error)

        total_errors = sum(len(errs) for errs in errors_by_category.values())
        results = []

        # 2. 构建表格内容
        # 标题行
        if total_errors == 0:
            results.append("✅ 机器人配置检查通过！\n")
        else:
            results.append(f"❌ 机器人配置检查未通过 (共 {total_errors} 个错误)\n")

        results.append("检查项 | 检查结果 | 错误详情")
        results.append("--- | --- | ---")

        # 定义检查项顺序
        check_items = [
            ("lgtm/approve数值检查", ["字段数值错误"]),
            ("branch_configs结构检查", ["branch_configs结构错误"]),
            ("merge method检查", ["合并策略错误"]),
            ("repos格式检查", ["仓库格式错误"]),
            ("仓库存在性检查", ["仓库存在性错误"]),
            ("其他检查", ["其他错误"]),
        ]

        # 生成表格行
        for item_name, categories in check_items:
            item_errors = []
            for cat in categories:
                if cat in errors_by_category:
                    item_errors.extend(errors_by_category[cat])

            if item_errors:
                # 去重：使用 dict.fromkeys 保留顺序并去除重复
                unique_errors = list(dict.fromkeys(item_errors))
                error_count = len(unique_errors)

                # 使用 <br> 实现 Markdown 表格内的换行显示
                error_summary = "<br>".join(unique_errors)

                results.append(f"{item_name} | ❌ 未通过 ({error_count}) | {error_summary}")
            else:
                # "其他检查" 无错误时不输出，避免干扰
                if item_name == "其他检查":
                    continue
                results.append(f"{item_name} | ✅ 已通过 | -")

        # 3. 写入文件与控制台输出
        result_filename = "result.md"
        try:
            with open(result_filename, "w", encoding="utf-8") as f:
                f.write("\n".join(results))
            
            # 控制台输出
            print("\n" + "="*60)
            print("门禁检查结果")
            print("="*60)
            print("\n".join(results))
            
            # 如果有错误，在控制台输出详细列表
            if total_errors > 0:
                print(f"\n{'='*60}")
                print("详细错误列表")
                print(f"{'='*60}")
                for i, error in enumerate(self.errors, 1):
                    print(f"{i}. {error}")
            
            print(f"\n{'='*60}")
            print(f"详细结果已保存到 {result_filename}")
            print("="*60)

        except Exception as e:
            print(f"❌ 写入 {result_filename} 失败: {e}")
            # 失败时仍然尝试打印到控制台
            print("\n".join(results))

def main():
    parser = argparse.ArgumentParser(description='Robot config validator')
    parser.add_argument('--config', default='.infra/robot-config.yaml', help='Path to robot-config.yaml')
    parser.add_argument('--token', help='GitCode API token')
    parser.add_argument('--no-cleanup', action='store_true', help='检查完成后保留克隆的临时目录（用于调试）')
    args = parser.parse_args()

    checker = RobotConfigChecker(
        token=args.token
    )

    # 执行检查（不管结果如何，都继续生成报告）
    success = checker.run_check(args.config)
    
    # 无论成功或失败，都强制生成 result.md
    # 这是解决 "未生成 result.md" 错误的关键
    checker.generate_result_md()

    # 最后根据检查结果退出状态码
    if success:
        print("✅ Configuration is valid")
        sys.exit(0)
    else:
        print("❌ Configuration errors found:")
        for err in checker.errors:
            print(f"  - {err}")
        # 注意：这里不退出，因为 generate_result_md 已经被调用
        sys.exit(1)

if __name__ == "__main__":
    main()