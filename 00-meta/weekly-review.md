# 周复盘

## 周期

- 时间范围：
- 本周主线：

## 本周完成

- [ ] 

## 本周学到的关键认知

1. 
2. 
3. 

## 银行业务连接

这个知识点可以连接到哪些银行场景？

- 

## AI 技术连接

涉及哪些 AI 方法或工具？

- 

## 风险与治理提醒

- 

## 下周计划

- [ ] 

## 本周一句话复盘

> 

---

## 2026-06-16 ~ 2026-06-22 周计划

### 建议主题

**银行反洗钱（AML）中的 AI 应用与治理**

选题理由：

1. 反洗钱是银行合规最核心、投入最大的场景之一，与 18 年银行经验高度相关。
2. 生成式 AI 正在重塑交易监测、客户尽调（CDD/EDD）和可疑活动报告（SAR）流程。
3. 该主题同时覆盖"业务场景 + AI 能力 + 治理框架"三条主线，契合项目四层闭环。
4. 公开资料丰富：BIS、NIST、McKinsey、UK Finance 均有高质量报告。

本周完成标准：

- 形成 1 篇反洗钱 AI 阅读笔记（记录到 `08-reading-notes/`）
- 拆解 1 个银行 AML + AI 用例（记录到 `04-banking-use-cases/`）
- 列出 AML AI 的关键风险与治理要点

### 推荐阅读

| 序号 | 来源 | 标题/主题 | 链接 | 阅读重点 |
|------|------|-----------|------|----------|
| 1 | BIS/Basel | 数字金融中的洗钱风险与监管科技 | https://www.bis.org/bcbs/publ/d575.htm | AI 如何嵌入银行反洗钱监管框架 |
| 2 | NIST | AI 风险管理框架（AI RMF 1.0） | https://www.nist.gov/itl/ai-risk-management-framework | 用"治理-映射-度量-管理"四维评估 AML AI |
| 3 | McKinsey | 生成式 AI 助力银行风险与合规管理 | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance | AML 合规效率提升的用例与落地路径 |
| 4 | UK Finance | 金融服务中的生成式 AI：机会与风险管理 | https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/generative-ai-action-opportunities-risk-management-financial-services | 客户尽调、交易监测与可疑报告 AI 化 |
| 5 | MIT Sloan | AI in Finance 课程大纲 | https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf | 金融 AI 的评估方法与监管影响 |

### 建议产出

1. **阅读笔记**：选读 McKinsey 或 UK Finance 报告中关于 AML 的章节，用阅读笔记模板记录 3 个核心观点。
2. **用例卡片**：拆解"AI 辅助可疑交易监测与 SAR 自动生成"用例，写清输入/输出/模型/评估/风险。
3. **治理清单**：在 `05-risk-governance-compliance/` 新增 AML AI 治理要点（数据隐私、模型偏差、误报率、人工复核机制、审计留痕）。

### 每日行动清单

| 日期 | 星期 | 时间建议 | 行动 | 产出 |
|------|------|----------|------|------|
| 06-16 | 一 | 30 分钟 | **选题确认**：在 `weekly-review.md` 确认本周主题为"银行 AML + AI"。浏览 McKinsey 和 UK Finance 报告目录，标记要精读的章节。 | 确认主题 + 阅读路径 |
| 06-17 | 二 | 45 分钟 | **输入日**：精读 McKinsey "How generative AI can help banks manage risk and compliance" 中 AML 相关段落。用阅读笔记模板记录。 | `08-reading-notes/aml-ai-mckinsey.md` |
| 06-18 | 三 | 30 分钟 | **业务连接**：结合银行经验回答 5 个问题——AML 在哪个部门？过去人工怎么做？痛点？AI 能增强哪步？最大风险？ | 业务连接笔记 |
| 06-19 | 四 | 45 分钟 | **AI 方案日**：把"AI 辅助可疑交易监测"翻译成 AI 用例卡片——输入（交易流水+客户画像）、输出（风险评分+SAR 草稿）、模型（分类+生成）、评估（召回率/误报率）、人工复核节点。 | `04-banking-use-cases/aml-ai-transaction-monitoring.md` |
| 06-20 | 五 | 30 分钟 | **沉淀日**：整理本周笔记，在 `05-risk-governance-compliance/` 新增 AML AI 治理清单。更新 `weekly-review.md` 本周复盘。 | 治理清单 + 周复盘 |
| 06-21 | 六 | 30 分钟（可选） | **轻实验**：用大语言模型（如 ChatGPT/Claude）模拟为一笔可疑交易生成 SAR 叙述段落，观察幻觉风险和合规表述质量。 | 实验记录（可选） |
| 06-22 | 日 | 10 分钟 | **回顾**：写一句话复盘——本周关于 AML AI 真正学到什么？下周是否继续深入 AML 还是切换主题？ | 一句话复盘 |

### 关键提醒

- 所有材料仅使用公开来源，不涉及任何真实客户数据或内部银行资料。
- 用例卡片中的交易数据均为虚构示例。
- 重点不是技术实现细节，而是"银行实务经验 + AI 能力匹配 + 风险治理"三层闭环。
