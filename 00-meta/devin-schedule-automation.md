# Devin Schedule Automation：如何用 Devin 做定时任务

Devin 支持 Scheduled Sessions，可以按计划自动启动 Devin 会话，适合做长期学习项目的提醒、资料整理、周报生成和 GitHub 更新。

官方文档：

- https://docs.devin.ai/product-guides/scheduled-sessions

## 1. Devin 能做什么

可以做：

- 每周自动创建一个学习复盘任务。
- 每周自动搜索金融 AI 新资料。
- 每周自动更新 GitHub 仓库中的 `weekly-review.md` 草稿。
- 每月自动生成一个月度总结草稿。
- 定时创建 Devin 会话并通知你查看结果。
- 如果配置了 `SERVERCHAN_SENDKEY`，还可以调用 Server 酱发送微信/手机通知。

不建议完全自动做：

- 不经你确认就发布观点文章。
- 不经你确认就引用敏感资料。
- 不经你确认就做重要仓库合并。

## 2. 邮件通知

Scheduled Sessions 支持 Email notifications：

- Always：每次运行后都发邮件。
- On failure only：只在失败时发邮件。
- Never：不发邮件。

如果你希望它像学习助理一样提醒你，建议选择：

- 每周任务：Always
- 每日提醒：On failure only 或不建议太频繁

## 2.1 Server 酱通知

如果你更希望用 Server 酱接收手机通知，请先把 SendKey 保存为 Devin Secret：

```text
SERVERCHAN_SENDKEY
```

然后在定时任务 prompt 中要求 Devin 在任务完成后运行：

```bash
python scripts/notify_serverchan.py \
  --title "金融AI任务完成" \
  --desp "本次 Devin 定时任务已完成。请查看 Devin 会话和 GitHub PR。" \
  --short "Devin 任务完成"
```

详细说明见：

```text
00-meta/serverchan-notification.md
```

## 3. 推荐定时任务 1：每周金融 AI 学习助理

频率：

- 每周一早上 9 点

Prompt：

```text
请更新 GitHub 仓库 superpaidaxing/finance-ai-evolution-lab。

任务：
1. 阅读 README.md、00-meta/roadmap.md、00-meta/weekly-execution-plan.md。
2. 根据项目目标，为本周选择一个金融 + AI 学习主题。
3. 在 00-meta/weekly-review.md 中追加一段“本周建议主题、推荐阅读、建议产出”。
4. 如果需要新增资料，请优先使用公开资料来源：NIST、BIS/Basel、McKinsey、MIT Sloan、UK Finance。
5. 不要使用任何真实客户数据或内部银行资料。
6. 提交一个 PR，不要直接合并。
7. 总结本周我应该每天做什么。
8. 如果环境变量 SERVERCHAN_SENDKEY 存在，请用 scripts/notify_serverchan.py 发送 Server 酱通知；不要暴露 key。
```

通知：

- Email notifications: Always

## 4. 推荐定时任务 2：每月金融 AI 趋势雷达

频率：

- 每月 1 日早上 9 点

Prompt：

```text
请在 GitHub 仓库 superpaidaxing/finance-ai-evolution-lab 中生成本月金融 AI 趋势雷达草稿。

任务：
1. 搜索过去 30 天公开发布的金融 AI、银行大模型、AI 风险治理、监管科技相关资料。
2. 优先来源：BIS、Basel Committee、NIST、McKinsey、Accenture、UK Finance、MIT Sloan。
3. 按“银行场景、AI 技术、风险治理、值得跟踪的问题”四类整理。
4. 在 08-reading-notes/ 下创建一篇月度趋势笔记。
5. 在 09-career-and-output/ 下创建一篇可进一步编辑的月度文章草稿。
6. 提交 PR，不要直接合并。
```

通知：

- Email notifications: Always

## 5. 推荐定时任务 3：每周 Issue 清单整理

频率：

- 每周五下午 5 点

Prompt：

```text
请检查 GitHub 仓库 superpaidaxing/finance-ai-evolution-lab 的 Issues 和文档。

任务：
1. 总结本周打开和关闭的任务。
2. 给出下周建议继续推进的 1–3 个主题。
3. 如果 weekly-review.md 没有更新，创建一个草稿提醒。
4. 不要做大规模重构。
5. 提交 PR 或给出清晰建议。
```

通知：

- Email notifications: Always

## 6. 如何创建 Scheduled Session

方式一：从 Devin 输入框创建

1. 在 Devin 输入框写好 prompt。
2. 点击输入框右侧三个点。
3. 选择 Schedule Devin。
4. 设置频率、仓库、通知方式。

方式二：从设置页创建

1. 打开 Devin Settings。
2. 进入 Schedules。
3. 点击 Create schedule。
4. 填写名称、频率、仓库、prompt、通知方式。

## 7. 建议先从一个任务开始

不要一开始设置很多自动任务。建议先设置：

**每周一 9 点：金融 AI 学习助理**

运行 2–3 周后，再决定是否增加月度趋势雷达。
