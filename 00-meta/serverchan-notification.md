# ServerChan Notification：用 Server 酱接收 Devin 通知

本项目可以用 Server 酱把 Devin 定时任务结果推送到微信/手机。

## 1. 安全原则

`SendKey` 是敏感凭证：

- 不要写进 GitHub 仓库。
- 不要写进 Markdown 文档。
- 不要写进定时任务 prompt 明文。
- 只保存为 Devin Secret：`SERVERCHAN_SENDKEY`。

如果曾经在聊天、截图或公开环境中暴露过 SendKey，建议在 Server 酱后台重置一次，再保存新的 key。

## 2. Devin Secret 配置

Secret 名称：

```text
SERVERCHAN_SENDKEY
```

保存范围建议：

- `user`：只给你自己的 Devin 会话使用。

## 3. 通知脚本

脚本位置：

```text
scripts/notify_serverchan.py
```

调用方式：

```bash
python scripts/notify_serverchan.py \
  --title "金融AI周报完成" \
  --desp "本周学习主题和 PR 已生成，请查看 GitHub。" \
  --short "周报完成"
```

脚本会从环境变量读取：

```bash
SERVERCHAN_SENDKEY
```

## 4. Devin 定时任务中的用法

在 Scheduled Session 的 prompt 末尾加入：

```text
任务完成后，如果环境变量 SERVERCHAN_SENDKEY 存在，请运行：

python scripts/notify_serverchan.py \
  --title "金融AI任务完成" \
  --desp "本次 Devin 定时任务已完成。请查看本会话结果和 GitHub PR。" \
  --short "Devin 任务完成"

如果发送失败，请在最终回复中说明失败原因，不要暴露 SERVERCHAN_SENDKEY。
```

## 5. 推荐通知内容

### 每周学习助理

标题：

```text
金融AI周计划完成
```

内容：

```text
本周金融 AI 学习主题、每日行动清单和 GitHub PR 已生成。
请查看 Devin 会话与 PR。
```

### 每月趋势雷达

标题：

```text
金融AI月报完成
```

内容：

```text
本月金融 AI 趋势雷达草稿已生成。
请查看阅读笔记、文章草稿和 PR。
```

## 6. 推荐工作流

1. Devin 定时任务自动启动。
2. Devin 更新 GitHub 仓库并创建 PR。
3. Devin 调用 `scripts/notify_serverchan.py`。
4. 你在手机收到 Server 酱通知。
5. 你打开 Devin 或 GitHub 审核结果。

这样你不需要本机电脑一直在线。
