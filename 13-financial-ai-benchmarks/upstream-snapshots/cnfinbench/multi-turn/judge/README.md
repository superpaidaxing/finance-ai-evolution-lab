# 评估脚本使用说明

**语言**: [English](README_EN.md) | [中文](README.md)

## 功能

`evaluate.py` 用于评估 `output` 目录下每个子文件夹中的 `merged.jsonl` 文件。对每一行对话记录进行评估，生成评估结果并保存。

## 使用方法

### 方式一：使用预配置脚本（推荐）

我们提供了两个预配置的脚本，可以直接使用：

#### Windows 系统

```cmd
REM 使用 Qwen3-235B 模型评估
judge\evaluate_qwen3_235b.bat

REM 使用 DeepSeek-V3 模型评估
judge\evaluate_deepseek_v3.bat
```

#### Linux/Mac 系统

```bash
# 首先添加执行权限
chmod +x judge/evaluate_qwen3_235b.sh
chmod +x judge/evaluate_deepseek_v3.sh

# 使用 Qwen3-235B 模型评估
./judge/evaluate_qwen3_235b.sh

# 使用 DeepSeek-V3 模型评估
./judge/evaluate_deepseek_v3.sh
```

### 方式二：直接使用 Python 命令

#### 基本用法

从项目根目录运行：

```bash
python -m judge.evaluate --output-dir ./output
```

#### 指定 API 配置

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key "your-api-key" \
    --judge-base-url "https://your-api-url/v1" \
    --judge-model-name "your-model-name"
```

### 参数说明

- `--output-dir`: output 目录路径（默认: `./output`）
- `--judge-api-key`: 评估模型 API Key（可选，有默认值）
- `--judge-base-url`: 评估模型 Base URL（可选，有默认值）
- `--judge-model-name`: 评估模型名称（可选，有默认值）

## 工作流程

1. **遍历子文件夹**: 扫描 `output` 目录下的所有子文件夹
2. **查找合并文件**: 在每个子文件夹中查找 `merged.jsonl` 或 `attack_mergered.jsonl`
3. **构建对话历史**: 从记录中提取并拼接对话历史
   - 格式：`original_question` + `round_1_answer` + `round_2_question` + `round_2_answer` + ... + `round_4_answer`
4. **选择规则模块**: 根据 `dataset` 字段选择对应的扣分规则
   - `MT_Inter` → `endogenous_rules_module`
   - `MT_App` → `application_rules_module`
   - `MT_Cog` → `cognitive_rules_module`
5. **调用 LLM API**: 使用完整的 prompt 调用评估模型
6. **解析结果**: 从 LLM 响应中提取 JSON 格式的评估结果
7. **保存结果**: 将原始记录和评估结果合并，保存到 `evaluation.jsonl`（每处理一条立即保存）

## 输出格式

每个子文件夹会生成一个 `evaluation.jsonl` 文件，每行包含：

```json
{
  "id": "1",
  "dataset": "MT_Inter",
  "type": "1",
  "original_question": "...",
  "round_1_answer": "...",
  "round_2_question": "...",
  "round_2_answer": "...",
  "round_3_question": "...",
  "round_3_answer": "...",
  "round_4_question": "...",
  "round_4_answer": "...",
  "evaluation": {
    "scoring_results": {
      "base_score": 100,
      "total_deductions": 5,
      "final_score": 95,
      "score_interpretation": "完美防御(90-100)",
      "affected_rounds": [2, 3]
    },
    "deduction_details": [
      {
        "deduction": 2,
        "reason": "...",
        "round": 2,
        "evidence": "...",
        "rule_applied": "A3"
      }
    ],
    "defense_assessment": {
      "overall_performance": "...",
      "critical_vulnerability": "..."
    }
  }
}
```

## 注意事项

1. **文件要求**: 输入的 `merged.jsonl` 文件必须包含以下字段：
   - `id`: 记录ID
   - `dataset`: 数据集类别（"MT_Inter"、"MT_App"、"MT_Cog"）
   - `original_question`: 原始问题
   - `round_1_answer`: 第1轮回答
   - `round_2_question`, `round_2_answer`: 第2轮问题和回答
   - `round_3_question`, `round_3_answer`: 第3轮问题和回答
   - `round_4_question`, `round_4_answer`: 第4轮问题和回答

2. **增量处理**: 如果 `evaluation.jsonl` 已存在，会被覆盖。如需增量处理，请先备份或修改代码。

3. **错误处理**: 如果某条记录处理失败，会打印错误信息并继续处理下一条记录。

4. **API 配置**: 默认使用项目中的 API 配置，如需修改请通过命令行参数传入。

## 脚本配置说明

### 修改脚本中的 API 配置

如果需要修改 API 配置，可以编辑对应的脚本文件：

- **Qwen3-235B**: 编辑 `judge/evaluate_qwen3_235b.bat` (Windows) 或 `judge/evaluate_qwen3_235b.sh` (Linux/Mac)
- **DeepSeek-V3**: 编辑 `judge/evaluate_deepseek_v3.bat` (Windows) 或 `judge/evaluate_deepseek_v3.sh` (Linux/Mac)

在脚本中找到以下变量并修改：

```bash
JUDGE_API_KEY="your-api-key"
JUDGE_BASE_URL="https://your-api-url/v1"
JUDGE_MODEL_NAME="your-model-name"
```

### 脚本文件说明

- `evaluate_qwen3_235b.bat` / `evaluate_qwen3_235b.sh`: 使用 Qwen3-235B 模型进行评估
- `evaluate_deepseek_v3.bat` / `evaluate_deepseek_v3.sh`: 使用 DeepSeek-V3 模型进行评估

**注意**: 
- Windows 用户使用 `.bat` 文件
- Linux/Mac 用户使用 `.sh` 文件（需要先添加执行权限：`chmod +x script.sh`）

