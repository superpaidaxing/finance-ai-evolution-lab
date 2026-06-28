# CNFinBench: 评估金融领域的专业知识、自主性和完整性

[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/2512.09506)
[![Leaderboard](https://img.shields.io/badge/Leaderboard-OpenCompass-blue)](https://cnfinbench.opencompass.org.cn/home)

---

📹 **请点击链接观看更清晰的视频：** [Video](https://www.bilibili.com/video/BV1tCFKz7E5V)  

https://github.com/user-attachments/assets/c15e95fb-8081-474b-936a-3686ac312c62

**语言**: [English](README.md) | [中文](README_CN.md)

## 📣 新闻与公告

📰 **媒体报道**  
- 👉 [CNFinBench 发布：金融大模型安全评估新基准](https://mp.weixin.qq.com/s/z427UB6r6QPNyAX_Pfc0JA)
- 👉 [从能力到智能体：CNFinBench 如何评估金融大模型的合规性与安全性](https://mp.weixin.qq.com/s/5UUBlklvoB67nQYOIXee7Q)
- 👉 [上海市政府：金融大模型评测体系2.0版在上海发布](https://www.shanghai.gov.cn/nw4411/20251229/3a87d71a2a104c9993164165a2e21c0a.html)
- 👉 [21世纪经济报道：行业标准再升级！2025金融大模型评测体系在沪正式发布](https://m.21jingji.com/article/20251229/herald/c4281b3b73c2b77940b8ab1010514875.html)
- 👉 [中国新闻网：2025金融大模型评测体系在沪成功落地](https://www.sh.chinanews.com.cn/kjjy/2025-12-27/143671.shtml)
- 👉 [国际金融报：2025金融大模型评测体系](https://www.ifnews.com/h5/news.html?aid=792908)
- 👉 [新华财经：2025金融大模型评测体系](https://bm.cnfic.com.cn/sharing/share/articleDetail/429697918115848192/1)
- 👉 [中国证券报：2025金融大模型评测体系](https://csapp1.cs.com.cn/hg/2025/12/28/detail_202512289338043.html)


📄 **学术发布**  
- **Beyond Knowledge to Agency: Evaluating Expertise, Autonomy, and Integrity in Finance with CNFinBench**  
  🔗 https://arxiv.org/abs/2512.09506

🌐 **在线排行榜**  
- 🔥 实时排行榜和模型提交：https://cnfinbench.opencompass.org.cn/home


---

## 📖 什么是 CNFinBench？


**CNFinBench** 是一个用于评估**高风险金融场景**中**大语言模型和智能体系统**的综合基准。

与传统的教科书式金融问答基准不同，CNFinBench 针对*高权限金融智能体*引入的**现实部署风险**，并沿着三个正交维度系统评估模型：

- **专业知识 (Expertise)** – 专业金融知识和推理能力  
- **自主性 (Autonomy)** – 多步骤规划、工具使用和智能体执行  
- **完整性 (Integrity)** – 在对抗性交互下的安全性、合规性和鲁棒性  

CNFinBench 涵盖**29 个细粒度任务**，基于认证的监管语料库、真实金融工作流程和多轮对抗性攻击场景。

---

## 🧩 任务分类

CNFinBench 将金融智能分解为三维评估空间：

<div align="center">
<img align="center" src="assets/fig-task-taxonomy.png" width="80%"/>
</div>



### 📚 专业知识 – 金融能力

- 金融知识掌握
- 复杂逻辑组合
- 上下文分析韧性

### ⚒️ 自主性 – 智能体执行

- 端到端执行（意图 → 计划 → 工具 → 验证）
- 战略规划与推理
- 元认知可靠性

### 🥷🏻 完整性 – 安全与合规

- 即时风险拦截
- 合规持久性
- 动态对抗编排

---

## 🔐 多轮安全评估与 HICS


为了量化**行为合规性退化**，CNFinBench 引入了：

### **有害指令合规分数 (Harmful Instruction Compliance Score, HICS)**

- 多维、严重程度感知的安全指标  
- 跟踪对话轮次中的违规升级  
- 支持可解释的规则级扣分日志  
- 揭示不同攻击策略下的**崩溃节奏**  

---

### 🏗 CNFinBench 是如何构建的？

CNFinBench 采用多阶段**数据生成流程**，结合：

<div align="center">
<img align="center" src="assets/fig-data-gen.png" width="80%"/>
</div>

- **LLM 辅助合成** – 用于可扩展的问题生成
- **专家编写与验证** – 确保领域准确性和风险覆盖
- **交互与安全任务设计** – 模拟信任边界和真实智能体执行链
- **任务感知的评分标准注释** – 实现跨 3 个维度的可解释模型评估

---

## 🏆 排行榜与评估平台


CNFinBench 部署在基于 **OpenCompass** 构建的**全自动评估平台**上，支持：

- **开源和闭源模型**的统一评估
- 具有 LLM-as-Judge 协议的任务感知评分标准
- 实时排行榜更新
- 动态任务和模型集成

🔗 **访问排行榜：**  
👉 https://cnfinbench.opencompass.org.cn/home

<div align="center">   <img src="./assets/image-20260131225448953.png" alt="Platform Overview" width="55%"> </div>

以下是**当前排行榜**的快照（在平台上实时更新）：

<div align="center">   <img src="./assets/image-20260131230239866.png" alt="Leaderboard Snapshot" width="55%"> </div>

---

## 📊 基准规模

- **29 个子任务**，涵盖专业知识 / 自主性 / 完整性  
- **11,947 个单轮问答实例**  
- **321 个多轮对抗性对话**（每个 4 轮）  
- **22 个评估模型**（开源、闭源、金融调优）

---

## 💻 代码使用

### 多轮对话评估

对于**多轮对抗性对话评估**，请参考 `multi-turn` 目录中的详细指南：

- 📖 **英文指南**: [multi-turn/README.md](multi-turn/README.md)
- 📖 **中文指南**: [multi-turn/README_CN.md](multi-turn/README_CN.md)

多轮评估流程包括：
1. 使用 `multi-turn/pred/` 中的脚本**生成多轮对话测试**
2. 使用 `multi-turn/pred/merge.py` **合并输出文件**
3. 使用 `multi-turn/judge/` 中的脚本**评估结果**

详细的评估脚本文档：
- 📖 **英文**: [multi-turn/judge/README_EN.md](multi-turn/judge/README_EN.md)
- 📖 **中文**: [multi-turn/judge/README.md](multi-turn/judge/README.md)

### 快速开始

1. **安装依赖**：
   ```bash
   cd multi-turn
   pip install -r requirements.txt
   ```

2. **生成多轮对话**：
   ```bash
   cd pred
   python main.py --data-dir ../data --output-dir ../output --model-name your_model_name \
       --attack-api-key your_attack_api_key --attack-base-url your_attack_base_url \
       --attack-model-name your_attack_model --defense-api-key your_defense_api_key \
       --defense-base-url your_defense_base_url --defense-model-name your_defense_model
   ```

3. **合并输出文件**：
   ```bash
   python merge.py --output-dir ../output
   ```

4. **评估结果**：
   ```bash
   cd ..
   python -m judge.evaluate --output-dir ./output \
       --judge-api-key your_judge_api_key --judge-base-url your_judge_base_url \
       --judge-model-name your_judge_model
   ```

更多详细说明和示例，请参阅 [multi-turn README](multi-turn/README_CN.md)。

---

## 📖 引用

如果CNFinBench对您的研究工作有所帮助，欢迎引用：

```bibtex
@inproceedings{ding2026kdd,
  title={Beyond Knowledge to Agency: Evaluating Expertise, Autonomy, and Integrity in Finance with CNFinBench},
  author={Ding, Jinru and Ding, Chao and Jiang, Yidong and Pang, Wenrao and Xiao, Boyi and Liu, Zhiqiang and Chen, Jiayuan and Zhong, Yun and Yuan, Tiantian and Guan, Junming and Cheng, Dawei and Xu, Jie},
  booktitle={Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  year={2026}
}
```

## 👥 贡献者

感谢本项目的贡献者 🎉

<a href="https://github.com/open-compass/CNFinBench/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=open-compass/CNFinBench" />
</a>

## ⭐ Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=open-compass/CNFinBench&type=Date)](https://star-history.com/#open-compass/CNFinBench&Date)

</div>

---
