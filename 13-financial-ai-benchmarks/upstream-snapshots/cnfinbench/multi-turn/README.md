# Multi-turn Dialogue Evaluation Guide

**Language**: [English](README.md) | [中文](README_CN.md)

This guide explains how to use the codebase to conduct multi-turn dialogue evaluation. The evaluation process consists of three main steps:

1. **Generate multi-turn dialogue tests** using scripts in the `pred` folder
2. **Merge output files** using `merge.py`
3. **Evaluate the results** using scripts in the `judge` folder

## Prerequisites

- Python 3.x

### Environment Setup

Install all required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, you can install packages individually as needed:
- `openai`
- `httpx`
- `pandas`
- `openpyxl` (for Excel file handling)

## Step 1: Generate Multi-turn Dialogue Tests

Use `pred/main.py` to generate multi-turn dialogue tests. This script executes three types of QA tests: MT_Inter, MT_Cog, and MT_App.

### Command

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

### Parameters

- `--data-dir`: Input data directory path (default: `./data`)
  - Should contain: `MT_Inter.xlsx`, `MT_Cog.xlsx`, `MT_App.xlsx`
- `--output-dir`: Output directory path (default: `./output`)
- `--model-name`: Test model name, used as output subfolder name (default: `model_name`)
- `--attack-api-key`: API key for the attack model
- `--attack-base-url`: Base URL for the attack model API
- `--attack-model-name`: Name of the attack model
- `--defense-api-key`: API key for the defense model
- `--defense-base-url`: Base URL for the defense model API
- `--defense-model-name`: Name of the defense model

### Output

The script generates output files in `{output-dir}/{model-name}/` directory. Each test type (MT_Inter, MT_Cog, MT_App) produces multiple JSONL files containing the dialogue records.

### Example

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

## Step 2: Merge Output Files

Use `pred/merge.py` to merge all JSONL files in each subdirectory of the output directory into a single `merged.jsonl` file.

### Command

```bash
cd pred
python merge.py --output-dir ../output
```

### Parameters

- `--output-dir`: Output directory path (default: current script directory or default path)

### What it does

1. Scans all subdirectories in the output directory
2. Finds all JSONL files in each subdirectory (excluding `merged.jsonl`)
3. Merges records by `id`, handling round-specific fields (e.g., `round_num`, `estimated_risk_escalation`, `strategy_chosen`, `reason`)
4. Outputs `merged.jsonl` in each subdirectory

### Output

Each subdirectory in the output directory will contain a `merged.jsonl` file with all dialogue records merged by ID.

### Example

```bash
python merge.py --output-dir ../output
```

## Step 3: Evaluate Results

Use `judge/evaluate.py` to evaluate the merged dialogue records. This script uses an LLM judge model to assess the defense performance in multi-turn dialogues.

### Command

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key your_judge_api_key \
    --judge-base-url your_judge_base_url \
    --judge-model-name your_judge_model_name
```

### Parameters

- `--output-dir`: Output directory path (default: `./output`)
- `--judge-api-key`: API key for the evaluation model (optional, has default value)
- `--judge-base-url`: Base URL for the evaluation model API (optional, has default value)
- `--judge-model-name`: Name of the evaluation model (optional, has default value)
- `--start-from`: Start from specified subdirectory (alphabetically, includes the subdirectory)
- `--end-at`: End at specified subdirectory (alphabetically, includes the subdirectory)

### What it does

1. Scans all subdirectories in the output directory
2. Looks for `merged.jsonl` or `attack_mergered.jsonl` in each subdirectory
3. Builds conversation history from the records
4. Selects appropriate scoring rules based on the `dataset` field:
   - `MT_Inter` → endogenous rules module
   - `MT_App` → application rules module
   - `MT_Cog` → cognitive rules module
5. Calls the LLM judge API with the complete prompt
6. Parses the JSON response and extracts evaluation results
7. Saves results to `evaluation.jsonl` in each subdirectory

### Output

Each subdirectory will contain an `evaluation.jsonl` file with evaluation results. The file includes:
- Original dialogue records
- Evaluation scores and deductions
- Detailed deduction reasons
- Defense assessment

Additionally, the script generates JSON and CSV summary files with statistics.

### Example

```bash
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key sk-zzz \
    --judge-base-url https://api.example.com/v1 \
    --judge-model-name qwen3-235b
```

## Complete Workflow Example

Here's a complete example of running the entire evaluation pipeline:

```bash
# Step 1: Generate multi-turn dialogues
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

# Step 2: Merge output files
python merge.py --output-dir ../output

# Step 3: Evaluate results
cd ..
python -m judge.evaluate \
    --output-dir ./output \
    --judge-api-key sk-judge \
    --judge-base-url https://api.example.com/v1 \
    --judge-model-name qwen3-235b
```

## Directory Structure

```
multi-turn/
├── data/                    # Input data files
│   ├── MT_Inter.xlsx
│   ├── MT_Cog.xlsx
│   └── MT_App.xlsx
├── pred/                    # Prediction/generation scripts
│   ├── main.py             # Main script to generate dialogues
│   ├── merge.py            # Script to merge output files
│   └── ...
├── judge/                   # Evaluation scripts
│   ├── evaluate.py         # Main evaluation script
│   ├── prompt.py           # Prompt templates
│   └── README.md           # Detailed evaluation guide
├── output/                  # Output directory (created after Step 1)
│   └── {model-name}/       # Subdirectory for each model
│       ├── *.jsonl         # Generated dialogue files
│       ├── merged.jsonl    # Merged file (after Step 2)
│       └── evaluation.jsonl # Evaluation results (after Step 3)
└── README.md               # This file
```

## Notes

1. **API Configuration**: Make sure to configure the correct API keys and base URLs for:
   - Attack model (used to generate adversarial questions)
   - Defense model (the model being evaluated)
   - Judge model (used for evaluation)

2. **File Requirements**: The input Excel files in `data/` directory must follow the expected format. Refer to the data files for the required structure.

3. **Error Handling**: If any step fails, check the error messages and ensure:
   - API keys are valid
   - Network connectivity is available
   - Input files are in the correct format
   - Output directory has write permissions

4. **Incremental Processing**: The evaluation script processes all subdirectories. You can use `--start-from` and `--end-at` parameters to process specific ranges if needed.

5. **Output Files**: 
   - After Step 1: Multiple JSONL files per test type
   - After Step 2: `merged.jsonl` in each subdirectory
   - After Step 3: `evaluation.jsonl` and summary files (JSON/CSV) in each subdirectory

## Troubleshooting

- **Import Errors**: Make sure you're running scripts from the correct directory or using the `-m` flag for module imports
- **API Errors**: Verify API keys and base URLs are correct, and check network connectivity
- **File Not Found**: Ensure input data files exist in the `data/` directory
- **Permission Errors**: Check that the output directory has write permissions

For more detailed information about the evaluation process, see [judge/README.md](judge/README_EN.md).
