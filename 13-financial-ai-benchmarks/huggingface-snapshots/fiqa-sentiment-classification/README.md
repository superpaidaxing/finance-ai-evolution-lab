---
language: en
license: mit
dataset_info:
  features:
  - name: _id
    dtype: string
  - name: sentence
    dtype: string
  - name: target
    dtype: string
  - name: aspect
    dtype: string
  - name: score
    dtype: float64
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 119567
    num_examples: 822
  - name: valid
    num_bytes: 17184
    num_examples: 117
  - name: test
    num_bytes: 33728
    num_examples: 234
  download_size: 102225
  dataset_size: 170479
---
# Dataset Name

## Dataset Description

This dataset is based on the task 1 of the Financial Sentiment Analysis in the Wild (FiQA) challenge. It follows the same settings as described in the paper 'A Baseline for Aspect-Based Sentiment Analysis in Financial Microblogs and News'. The dataset is split into three subsets: train, valid, test with sizes 822, 117, 234 respectively.

## Dataset Structure

- `_id`: ID of the data point
- `sentence`: The sentence
- `target`: The target of the sentiment
- `aspect`: The aspect of the sentiment
- `score`: The sentiment score
- `type`: The type of the data point (headline or post)

## Additional Information

- Homepage: [FiQA Challenge](https://sites.google.com/view/fiqa/home)
- Citation: [A Baseline for Aspect-Based Sentiment Analysis in Financial Microblogs and News](https://arxiv.org/pdf/2211.00083.pdf)

## Downloading CSV
```python
from datasets import load_dataset

# Load the dataset from the hub
dataset = load_dataset("ChanceFocus/fiqa-sentiment-classification")

# Save the dataset to a CSV file
dataset["train"].to_csv("train.csv")
dataset["valid"].to_csv("valid.csv")
dataset["test"].to_csv("test.csv")
```
