#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse

def add_or_remove_labels(owner, project, pr_number, access_token, add_labels, remove_labels):
    """
    添加或删除 PR 标签
    
    Args:
        owner: 仓库所有者
        project: 项目名称
        pr_number: PR 编号
        access_token: 访问令牌
        add_labels: 要添加的标签列表
        remove_labels: 要删除的标签列表
    """
    try:
        print(f"going to update pr {owner}, {project}, {pr_number}, {add_labels}, {remove_labels}")
        
        base_url = f"https://gitcode.com/api/v5/repos/{owner}/{project}/pulls/{pr_number}"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json;charset=UTF-8"
        }
        
        # 删除 PR 的标签
        for label in remove_labels:
            request_url = f"{base_url}/labels/{label}"
            print(request_url)
            
            try:
                response = requests.delete(request_url, headers=headers)
                print(f"Delete label '{label}' response: {response.status_code}")
                if response.status_code == 404:
                    print(f"Label '{label}' not found, may have been already removed")
                elif response.status_code == 200:
                    print(f"Label '{label}' removed successfully")
            except Exception as e:
                print(f"Error deleting label {label}: {e}")
        
        # 添加新的标签
        if add_labels:
            request_url = f"{base_url}/labels"
            print(f"Adding labels to: {request_url}")
            print(f"Labels to add: {add_labels}")
            
            try:
                response = requests.post(request_url, headers=headers, json=add_labels)
                print(f"Add labels response: {response.status_code}")
                
                if response.status_code in [200, 201]:
                    print("Labels added successfully")
                else:
                    print(f"Failed to add labels: {response.status_code} - {response.text}")
                    
            except Exception as e:
                print(f"Error adding labels: {e}")
        else:
            print("No labels to add")
            
        print("Label update operation completed")
        
    except Exception as ex:
        print(f"Failed to update PR labels: {ex}")
        raise

def main():
    """主函数 - 使用 argparse 解析参数"""
    parser = argparse.ArgumentParser(description='CI pipeline label manager for GitCode PRs')
    parser.add_argument('--owner', required=True, help='仓库所有者')
    parser.add_argument('--project', required=True, help='项目名称')
    parser.add_argument('--pr-number', required=True, help='PR 编号')
    parser.add_argument('--token', required=True, help='GitCode 访问令牌')
    parser.add_argument('--action', choices=['ATDS', 'ATDF', 'ATDR'],
                        help='预定义操作: ATDS(成功), ATDF(失败), ATDR(运行中)')
    parser.add_argument('--add-labels', default='',
                        help='要添加的标签，逗号分隔 (与 --action 二选一)')
    parser.add_argument('--remove-labels', default='',
                        help='要删除的标签，逗号分隔 (与 --action 二选一)')
    args = parser.parse_args()

    if args.action:
        if args.action == "ATDS":
            add_labels = ["ci-pipeline-passed"]
            remove_labels = ["ci-pipeline-failed", "ci-pipeline-running"]
        elif args.action == "ATDF":
            add_labels = ["ci-pipeline-failed"]
            remove_labels = ["ci-pipeline-passed", "ci-pipeline-running"]
        else:  # ATDR
            add_labels = ["ci-pipeline-running"]
            remove_labels = ["ci-pipeline-passed", "ci-pipeline-failed"]
    else:
        add_labels = [l for l in args.add_labels.split(',') if l] if args.add_labels else []
        remove_labels = [l for l in args.remove_labels.split(',') if l] if args.remove_labels else []

    add_or_remove_labels(args.owner, args.project, args.pr_number, args.token, add_labels, remove_labels)

if __name__ == "__main__":
    main()