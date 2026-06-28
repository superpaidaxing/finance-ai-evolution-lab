# 多轮对话评测使用指南

**语言**: [English](README.md) | [中文](README_CN.md)

本指南说明如何使用代码库进行多轮对话评测。评测过程包含三个主要步骤：

1. 使用 `pred` 文件夹下的脚本**生成多轮对话测试**
2. 使用 `merge.py` **合并输出文件**
3. 使用 `judge` 文件夹下的脚本**评估结果**

## 环境要求

- Python 3.x

### 环境配置

使用提供的 `requirements.txt` 文件安装所有必需的依赖包：

```bash
pip install -r requirements.txt
```

或者，您也可以根据需要单独安装以下包：
- `openai`
- `httpx`
- `pandas`
- `openpyxl` (用于处理 Excel 文件)

## 步骤 1：生成多轮对话测试

使用 `pred/main.py` 生成多轮对话测试。该脚本会执行三种类型的问答测试：MT_Inter、MT_Cog 和 MT_App。

### 命令

```bash
cd pred
python main.py \
    --data-dir ../data \
    --output-dir ../output \
    --model-name your_model_name \
    --attack-api-key your_attack_api_key \
    --attack-base-url your_attack_base_url \
    --attack-model-name your_attack_model_name \
    --defense-api-key your_defense_api_key \
    --defense-base-url your_defense_base_url \
    --defense-model-name your_defense_model_name
```

### 参数说明

- `--data-dir`: 输入数据目录路径（默认：`./data`）
  - 应包含：`MT_Inter.xlsx`、`MT_Cog.xlsx`、`MT_App.xlsx`
- `--output-dir`: 输出目录路径（默认：`./output`）
- `--model-name`: 测试模型名称，用作输出子文件夹名称（默认：`model_name`）
- `--attack-api-key`: 攻击模型的 API 密钥
- `--attack-base-url`: 攻击模型 API 的基础 URL
- `--attack-model-name`: 攻击模型名称
- `--defense-api-key`: 防御模型的 API 密钥
- `--defense-base-url`: 防御模型 API 的基础 URL
- `--defense-model-name`: 防御模型名称

### 输出

脚本会在 `{output-dir}/{model-name}/` 目录下生成输出文件。每种测试类型（MT_Inter、MT_Cog、MT_App）都会生成多个包含对话记录的 JSONL 文件。

### 示例

```bash
python main.py \
    --data-dir ../data \
    --output-dir ../output \
    --model-name deepseek-v3 \
    --attack-api-key sk-xxx \
    --attack-base-url https://api.example.com/v1 \
    --attack-model-name deepseek-r1 \
    --defense-api-key sk-yyy \
    --defense-base-url https://api.example.com/v1 \
    --defense-model-name deepseek-v3
```

## 步骤 2：合并输出文件

使用 `pred/merge.py` 将输出目录中每个子目录下的所有 JSONL 文件合并为单个 `merged.jsonl` 文件。

### 命令

```bash
cd pred
python merge.py --output-dir ../output
```

### 参数说明

- `--output-dir`: 输出目录路径（默认：当前脚本目录或默认路径）

### 功能说明

1. 扫描输出目录下的所有子目录
2. 在每个子目录中查找所有 JSONL 文件（排除 `merged.jsonl`）
3. 按 `id` 合并记录，处理轮次相关字段（如 `round_num`、`estimated_risk_escalation`、`strategy_chosen`、`reason`）
4. 在每个子目录中输出 `merged.jsonl`

### 输出

输出目录中的每个子目录将包含一个 `merged.jsonl` 文件，其中包含按 ID 合并的所有对话记录。

### 示例

```bash
python merge.py --output-dir ../output
```

## 步骤 3：评估结果

使用 `judge/evaluate.py` 评估合并后的对话记录。该脚本使用 LLM 评判模型来评估多轮对话中的防御表现。

### 命令

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key your_judge_api_key \
    --judge-base-url your_judge_base_url \
    --judge-model-name your_judge_model_name
```

### 参数说明

- `--output-dir`: 输出目录路径（默认：`./output`）
- `--judge-api-key`: 评估模型的 API 密钥（可选，有默认值）
- `--judge-base-url`: 评估模型 API 的基础 URL（可选，有默认值）
- `--judge-model-name`: 评估模型名称（可选，有默认值）
- `--start-from`: 从指定的子目录开始（按字母顺序，包含该子目录）
- `--end-at`: 在指定的子目录结束（按字母顺序，包含该子目录）

### 功能说明

1. 扫描输出目录下的所有子目录
2. 在每个子目录中查找 `merged.jsonl` 或 `attack_mergered.jsonl`
3. 从记录中构建对话历史
4. 根据 `dataset` 字段选择相应的评分规则：
   - `MT_Inter` → 内生规则模块
   - `MT_App` → 应用规则模块
   - `MT_Cog` → 认知规则模块
5. 使用完整的提示调用 LLM 评判 API
6. 解析 JSON 响应并提取评估结果
7. 将结果保存到每个子目录的 `evaluation.jsonl`

### 输出

每个子目录将包含一个 `evaluation.jsonl` 文件，其中包含评估结果。文件包括：
- 原始对话记录
- 评估分数和扣分
- 详细的扣分原因
- 防御评估

此外，脚本还会生成包含统计信息的 JSON 和 CSV 摘要文件。

### 示例

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key sk-zzz \
    --judge-base-url https://api.example.com/v1 \
    --judge-model-name qwen3-235b
```

## 完整工作流示例

以下是运行整个评测流程的完整示例：

```bash
# 步骤 1：生成多轮对话
cd pred
python main.py \
    --data-dir ../data \
    --output-dir ../output \
    --model-name test-model \
    --attack-api-key sk-attack \
    --attack-base-url https://api.example.com/v1 \
    --attack-model-name deepseek-r1 \
    --defense-api-key sk-defense \
    --defense-base-url https://api.example.com/v1 \
    --defense-model-name deepseek-v3

# 步骤 2：合并输出文件
python merge.py --output-dir ../output

# 步骤 3：评估结果
cd ..
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key sk-judge \
    --judge-base-url https://api.example.com/v1 \
    --judge-model-name qwen3-235b
```

## 目录结构

```
multi-turn/
├── data/                    # 输入数据文件
│   ├── MT_Inter.xlsx
│   ├── MT_Cog.xlsx
│   └── MT_App.xlsx
├── pred/                    # 预测/生成脚本
│   ├── main.py             # 生成对话的主脚本
│   ├── merge.py            # 合并输出文件的脚本
│   └── ...
├── judge/                   # 评估脚本
│   ├── evaluate.py         # 主评估脚本
│   ├── prompt.py           # 提示模板
│   └── README.md           # 详细评估指南
├── output/                  # 输出目录（步骤 1 后创建）
│   └── {model-name}/       # 每个模型的子目录
│       ├── *.jsonl         # 生成的对话文件
│       ├── merged.jsonl    # 合并后的文件（步骤 2 后）
│       └── evaluation.jsonl # 评估结果（步骤 3 后）
├── requirements.txt        # 依赖包列表
├── README.md               # 英文版本文档
└── README_CN.md            # 中文版本文档（本文件）
```

## 注意事项

1. **API 配置**：确保为以下模型配置正确的 API 密钥和基础 URL：
   - 攻击模型（用于生成对抗性问题）
   - 防御模型（被评估的模型）
   - 评判模型（用于评估）

2. **文件要求**：`data/` 目录中的输入 Excel 文件必须遵循预期格式。请参考数据文件了解所需结构。

3. **错误处理**：如果任何步骤失败，请检查错误消息并确保：
   - API 密钥有效
   - 网络连接可用
   - 输入文件格式正确
   - 输出目录具有写入权限

4. **增量处理**：评估脚本会处理所有子目录。如果需要，可以使用 `--start-from` 和 `--end-at` 参数处理特定范围。

5. **输出文件**：
   - 步骤 1 后：每种测试类型多个 JSONL 文件
   - 步骤 2 后：每个子目录中的 `merged.jsonl`
   - 步骤 3 后：每个子目录中的 `evaluation.jsonl` 和摘要文件（JSON/CSV）

## 故障排除

- **导入错误**：确保从正确的目录运行脚本或使用 `-m` 标志进行模块导入
- **API 错误**：验证 API 密钥和基础 URL 是否正确，并检查网络连接
- **文件未找到**：确保输入数据文件存在于 `data/` 目录中
- **权限错误**：检查输出目录是否具有写入权限

有关评估过程的更多详细信息，请参阅 [judge/README.md](judge/README.md)。
