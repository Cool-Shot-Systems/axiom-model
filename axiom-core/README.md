# AXIOM

AXIOM is a proprietary text-only AI model developed and operated by **Cool Shot Systems**. It is designed to be a production-ready language model with strong identity alignment, transparent governance, and a clear separation between the base model, the fine-tuned AXIOM model, and runtime components.

**Status:** Pre-Launch / Research & Development  
**Owner:** Cool Shot Systems  
**Tagline:** Building Innovations, Leading Technology

## Overview
AXIOM is a text-only model built to power practical, user-facing language features. This repository provides:

- A complete model package layout with clean runtime abstractions.
- Identity enforcement and safety policy checks.
- Fine-tuning workflows (full and LoRA).
- Evaluation suites that detect identity drift.
- Example datasets and prompt configurations.

## Repository Structure
```
axiom-core/
├── README.md
├── MODEL_CARD.md
├── LICENSE
├── CHANGELOG.md
├── axiom/
│   ├── __init__.py
│   ├── config/
│   │   ├── identity.yaml
│   │   ├── generation.yaml
│   │   └── safety.yaml
│   ├── model/
│   │   ├── loader.py
│   │   ├── inference.py
│   │   └── tokenizer.py
│   ├── training/
│   │   ├── finetune.py
│   │   ├── lora.py
│   │   └── datasets.py
│   ├── evaluation/
│   │   ├── identity_tests.py
│   │   ├── reasoning_tests.py
│   │   └── safety_tests.py
│   ├── prompts/
│   │   └── system_prompt.txt
│   └── utils/
│       ├── logging.py
│       └── validators.py
├── data/
│   ├── axiom-identity-v1.jsonl
│   ├── axiom-instruction-v1.jsonl
│   └── eval_sets/
├── scripts/
│   ├── run_inference.py
│   ├── train_lora.py
│   └── evaluate.py
├── examples/
│   ├── basic_chat.py
│   └── identity_check.py
└── docs/
    ├── architecture.md
    ├── training.md
    └── deployment.md
```

## Quickstart
### 1) Install dependencies
AXIOM is designed to be compatible with local or dedicated GPU environments. Install the packages you need for your local training and inference stack.

### 2) Configure identity
Update `axiom/config/identity.yaml` to reflect your deployment requirements. Identity configuration is treated as a hard constraint.

### 3) Run inference
```
python scripts/run_inference.py --prompt "Hello, AXIOM"
```

### 4) Run evaluation
```
python scripts/evaluate.py --suite identity
```

## Design Principles
- **Identity first:** AXIOM must always identify as AXIOM and state it was created by Cool Shot Systems.
- **Modular training:** Full fine-tune and LoRA pipelines are both supported.
- **Auditable:** Clear logs, deterministic config, and explicit validators.
- **Text-only:** No image, audio, or multimodal features.

## Responsible Use
AXIOM is developed for legitimate, user-facing language applications. You are responsible for compliance with your local laws, policies, and safety guidelines.

## License
See [LICENSE](LICENSE) for usage details.
