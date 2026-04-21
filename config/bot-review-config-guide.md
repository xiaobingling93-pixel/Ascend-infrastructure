# .infra/robot-config.yaml 配置指导文档

本文档用于指导如何配置 [config/bot-review-config.yaml](bot-review-config.yaml) 文件，该文件主要用于定义代码审核规则、PR目标分支管理策略以及标签自动化处理。

## 字段详细说明

### 1. configs (配置列表)
该部分定义了针对不同仓库的配置规则。

| 字段 | 类型 | 说明 | 示例 |
| :--- | :--- | :--- | :--- |
| `repos` | list | 适用的仓库列表。 | `["ascend-archive/testRepo"]` |
| `lgtm_need_nums` | int | 机器人添加 lgtm 标签需要的 `/lgtm` 评论数量。 | `3` |
| `approve_need_nums` | int | 机器人添加 approved 标签需要的 `/approve` 评论数量。 | `4` |
| `branch_configs` | list | 针对不同目标分支的合并策略配置列表。 | / |

### 2. branch_configs (分支配置列表)
每个分支配置项用于定义特定分支或默认分支的合并方式与标签规则。

| 字段 | 类型 | 说明 | 示例 |
| :--- | :--- | :--- | :--- |
| `branch` | string | 目标分支名称。与 `is_default` 二选一。 | `main` |
| `is_default` | bool | 设为 `true` 时作为兜底默认配置，匹配未被其他 branch_configs 命中的分支。 | `true` |
| `merge_method` | string | 合并 PR 的方式。可选值：`squash`, `merge`, `rebase`。 | `squash` |
| `labels` | list | 定义该分支所需的自动化标签列表。 | / |

#### labels 列表项说明：
每个标签配置项包含以下字段：

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `label` | string | 标签的名称。 |
| `person` | string | 负责自动添加该标签的机器人账号ID。 |

---

## 配置示例

```yaml
configs:
  - repos:
      - Ascend/testRepo
    lgtm_need_nums: 3
    approve_need_nums: 4
    branch_configs:
      - is_default: true
        merge_method: squash
        labels:
          - label: lgtm
            person: ascend-robot
          - label: approved
            person: ascend-robot
          - label: ascend-cla/yes
            person: ascend-robot
      - branch: main
        merge_method: squash
        labels:
          - label: lgtm
            person: ascend-robot
          - label: approved
            person: ascend-robot
          - label: ascend-cla/yes
            person: ascend-robot
          - label: ci-pipeline-passed
            person: ascend-robot
      - branch: release-1.0
        merge_method: merge
        labels:
          - label: lgtm
            person: ascend-robot
          - label: approved
            person: ascend-robot
          - label: ascend-cla/yes
            person: ascend-robot
          - label: ci-pipeline-passed
            person: ascend-robot
      
```

---
*注：修改配置后，请确保 YAML 格式正确。*
