# AXIOM Training Guide

## Overview
AXIOM supports two training modes:
- **Full Fine-Tune:** Updates all weights on the base model.
- **LoRA Fine-Tune:** Adds low-rank adapters while keeping the base model intact.

## Data Preparation
Training data must be JSONL with `prompt` and `response` fields. Identity alignment data should be included in every training run.

## Full Fine-Tune
Run:
```
python -m axiom.training.finetune --help
```

## LoRA Fine-Tune
Run:
```
python scripts/axiom_train.py --mode lora --model-path /path/to/base --dataset data/axiom-identity-v1.jsonl --output output/lora
```

## Full Fine-Tune (All Weights)
Run:
```
python scripts/axiom_train.py --mode full --model-path /path/to/base --dataset data/axiom-identity-v1.jsonl --output output/full
```

## Best Practices
- Keep identity and safety datasets up to date.
- Run evaluation suites after each training run.
- Store artifacts with versioned tags for auditability.
