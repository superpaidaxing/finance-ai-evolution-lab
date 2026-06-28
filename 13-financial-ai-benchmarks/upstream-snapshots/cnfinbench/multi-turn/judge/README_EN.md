# Evaluation Script Usage Guide

**Language**: [English](README_EN.md) | [中文](README.md)

## Functionality

`evaluate.py` is used to evaluate `merged.jsonl` files in each subdirectory under the `output` directory. It evaluates each dialogue record line by line, generates evaluation results, and saves them.

## Usage

### Method 1: Using Pre-configured Scripts (Recommended)

We provide two pre-configured scripts that can be used directly:

#### Windows System

```cmd
REM Evaluate using Qwen3-235B model
judge\evaluate_qwen3_235b.bat

REM Evaluate using DeepSeek-V3 model
judge\evaluate_deepseek_v3.bat
```

#### Linux/Mac System

```bash
# First, add execute permissions
chmod +x judge/evaluate_qwen3_235b.sh
chmod +x judge/evaluate_deepseek_v3.sh

# Evaluate using Qwen3-235B model
./judge/evaluate_qwen3_235b.sh

# Evaluate using DeepSeek-V3 model
./judge/evaluate_deepseek_v3.sh
```

### Method 2: Direct Python Command

#### Basic Usage

Run from the project root directory:

```bash
python -m judge.evaluate --output-dir ./output
```

#### Specify API Configuration

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key "your-api-key" \
    --judge-base-url "https://your-api-url/v1" \
    --judge-model-name "your-model-name"
```

### Parameter Description

- `--output-dir`: Output directory path (default: `./output`)
- `--judge-api-key`: Evaluation model API Key (optional, has default value)
- `--judge-base-url`: Evaluation model Base URL (optional, has default value)
- `--judge-model-name`: Evaluation model name (optional, has default value)
- `--start-from`: Start from specified subdirectory (alphabetically, includes the subdirectory)
- `--end-at`: End at specified subdirectory (alphabetically, includes the subdirectory)

## Workflow

1. **Traverse Subdirectories**: Scan all subdirectories under the `output` directory
2. **Find Merged Files**: Look for `merged.jsonl` or `attack_mergered.jsonl` in each subdirectory
3. **Build Conversation History**: Extract and concatenate conversation history from records
   - Format: `original_question` + `round_1_answer` + `round_2_question` + `round_2_answer` + ... + `round_4_answer`
4. **Select Rules Module**: Choose corresponding deduction rules based on the `dataset` field
   - `MT_Inter` → `endogenous_rules_module`
   - `MT_App` → `application_rules_module`
   - `MT_Cog` → `cognitive_rules_module`
5. **Call LLM API**: Call the evaluation model with the complete prompt
6. **Parse Results**: Extract JSON-format evaluation results from the LLM response
7. **Save Results**: Merge original records with evaluation results and save to `evaluation.jsonl` (saves immediately after processing each record)

## Output Format

Each subdirectory will generate an `evaluation.jsonl` file, with each line containing:

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

## Notes

1. **File Requirements**: The input `merged.jsonl` file must contain the following fields:
   - `id`: Record ID
   - `dataset`: Dataset category ("MT_Inter", "MT_App", "MT_Cog")
   - `original_question`: Original question
   - `round_1_answer`: Round 1 answer
   - `round_2_question`, `round_2_answer`: Round 2 question and answer
   - `round_3_question`, `round_3_answer`: Round 3 question and answer
   - `round_4_question`, `round_4_answer`: Round 4 question and answer

2. **Incremental Processing**: If `evaluation.jsonl` already exists, it will be overwritten. For incremental processing, please backup or modify the code first.

3. **Error Handling**: If a record fails to process, an error message will be printed and the script will continue processing the next record.

4. **API Configuration**: Default API configuration from the project is used. To modify, pass parameters via command line arguments.

## Script Configuration

### Modifying API Configuration in Scripts

If you need to modify the API configuration, you can edit the corresponding script files:

- **Qwen3-235B**: Edit `judge/evaluate_qwen3_235b.bat` (Windows) or `judge/evaluate_qwen3_235b.sh` (Linux/Mac)
- **DeepSeek-V3**: Edit `judge/evaluate_deepseek_v3.bat` (Windows) or `judge/evaluate_deepseek_v3.sh` (Linux/Mac)

Find and modify the following variables in the script:

```bash
JUDGE_API_KEY="your-api-key"
JUDGE_BASE_URL="https://your-api-url/v1"
JUDGE_MODEL_NAME="your-model-name"
```

### Script File Description

- `evaluate_qwen3_235b.bat` / `evaluate_qwen3_235b.sh`: Evaluate using Qwen3-235B model
- `evaluate_deepseek_v3.bat` / `evaluate_deepseek_v3.sh`: Evaluate using DeepSeek-V3 model

**Note**: 
- Windows users should use `.bat` files
- Linux/Mac users should use `.sh` files (need to add execute permissions first: `chmod +x script.sh`)
