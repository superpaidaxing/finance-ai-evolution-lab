# GitHub Workflow：完全在线迭代方法

## 1. 不依赖本地同步的维护方式

这个项目可以只在 GitHub 网页端维护：

1. 打开任意 Markdown 文件。
2. 点击铅笔图标编辑。
3. 修改后点击 Commit changes。
4. 用 Issue 记录待办、研究问题和实验计划。
5. 用 GitHub Projects 做长期路线图。

## 2. 推荐 GitHub Project 看板

### 视图 1：学习流水线

列：

- Backlog
- This Week
- In Progress
- Review
- Done
- Archived

### 视图 2：季度路线图

按 Quarter 分组：

- 2026-Q2
- 2026-Q3
- 2026-Q4
- 2027-Q1

### 视图 3：能力地图

按 Track 分组：

- Finance
- AI
- Use Case
- Governance
- Lab
- Output

## 3. Issue 标签建议

- `track:finance`
- `track:ai`
- `track:use-case`
- `track:governance`
- `track:lab`
- `track:output`
- `depth:L1`
- `depth:L2`
- `depth:L3`
- `depth:L4`
- `depth:L5`
- `status:weekly`
- `status:quarterly`

## 4. Commit 规范

建议格式：

```text
docs: add reading note for NIST AI RMF
case: add KYC genai use case
lab: add complaint classification experiment
review: add 2026-W20 weekly review
roadmap: update Q3 focus
```

## 5. 每周操作流程

1. 打开 Project 看板。
2. 从 Backlog 挑 1-3 个 Issue 到 This Week。
3. 完成文档或实验。
4. 关闭 Issue。
5. 更新 `weekly-review.md`。
6. 如果有新问题，创建新 Issue，不要打断当前主线。

## 6. 每季度操作流程

1. 回顾已完成 Issue。
2. 统计输出数量。
3. 更新路线图。
4. 归档过期主题。
5. 选择下季度重点主题。
