# 同步到 GitHub：之后如何同步到 GitHub

当前项目已经整理为标准 GitHub 仓库结构。后续有三种同步方式。

## 方式一：GitHub 网页端上传，最简单

适合不想处理命令行的时候。

1. 打开 https://github.com/new
2. 仓库名建议填写：`finance-ai-evolution-lab`
3. 仓库描述可填写：

   ```text
   一个面向银行从业者的金融 + AI 长期进化式学习与实践项目
   ```

4. 选择公开仓库或私有仓库。
5. 不要勾选 “Add a README file”，因为本项目已经有 README。
6. 创建仓库。
7. 点击 “uploading an existing file”。
8. 上传压缩包解压后的所有文件和目录。
9. 提交修改。

## 方式二：如果本机 GitHub CLI 已登录

如果之后确认 `gh auth status` 已登录，可以在项目目录执行：

```bash
gh repo create finance-ai-evolution-lab --public --source=. --remote=origin --push
```

如果想创建私有仓库，把 `--public` 改为：

```bash
--private
```

## 方式三：在 GitHub 新建空仓库后，用 git push

先在 GitHub 网页创建空仓库，然后执行：

```bash
git remote add origin https://github.com/superpaidaxing/finance-ai-evolution-lab.git
git branch -M main
git push -u origin main
```

## 后续完全在线维护

同步到 GitHub 后，可以只用网页端持续更新：

1. 打开文件。
2. 点击铅笔图标。
3. 编辑 Markdown。
4. 提交修改。
5. 用 Issues 管理待学习主题。
6. 用 Projects 管理路线图。

## 建议创建的 GitHub Project 字段

- 状态：待处理 / 本周 / 进行中 / 待复盘 / 已完成 / 已归档
- 主线：金融基础 / AI 基础 / 银行用例 / 风险治理 / 实验 / 输出
- 深度：L1 / L2 / L3 / L4 / L5
- 季度：2026-Q2、2026-Q3 等

## 首次同步后的建议动作

1. 创建 Project 看板。
2. 复制 `00-meta/first-30-issues.md` 中的任务为 Issues。
3. 给 Issues 加标签。
4. 每周固定更新 `00-meta/weekly-review.md`。
5. 每月新增一篇深度输出到 `09-career-and-output/`。
