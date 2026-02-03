# AXIOM

AXIOM is a proprietary, text-only AI model developed and operated by **Cool Shot Systems**. It is built for production-ready language workflows with strict identity alignment, auditable configuration, and a clean separation between core runtime, training pipelines, and evaluation suites.

**Status:** Pre-Launch / Research & Development  
**Owner:** Cool Shot Systems  
**Tagline:** Building Innovations, Leading Technology

## Model Summary
AXIOM is designed for practical, real-world text applications such as knowledge assistants, productivity tools, and internal automation. The repository is structured for engineers who want a clean, installable library with training, evaluation, and deployment guidance.

## Intended Use
- Enterprise and internal assistants
- Knowledge search and summarization
- Customer support and operational workflows
- Education and research (text-only)

## Out-of-Scope Use
- Multimodal tasks (image, audio, or video)
- Safety-critical decision making without human oversight
- High-risk domains without domain-specific validation

## Identity & Governance
AXIOM must always identify as **AXIOM** and state it was created by **Cool Shot Systems**. Identity enforcement is implemented in configuration, system prompts, and runtime validators.

## Quickstart
### Install (local development)
```
pip install -e .
```

### Run inference
```
python scripts/axiom_infer.py --model-path /path/to/base/model --prompt "Hello, AXIOM"
```

### Run evaluation
```
python scripts/axiom_eval.py --suite identity
```

## Repository Layout
```
axiom-core/
├── README.md
├── MODEL_CARD.md
├── LICENSE
├── CHANGELOG.md
├── pyproject.toml
├── axiom/
│   ├── __init__.py
│   ├── __version__.py
│   ├── config/
│   │   ├── identity.yaml
│   │   ├── generation.yaml
│   │   └── safety.yaml
│   ├── modeling/
│   │   ├── loader.py
│   │   ├── inference.py
│   │   └── tokenizer.py
│   ├── training/
│   │   ├── finetune.py
│   │   ├── lora.py
│   │   └── datasets.py
│   ├── evaluation/
│   │   ├── identity.py
│   │   ├── reasoning.py
│   │   └── safety.py
│   ├── prompts/
│   │   └── system.txt
│   └── utils/
│       ├── logging.py
│       └── validators.py
├── data/
│   ├── axiom-identity-v1.jsonl
│   ├── axiom-instruction-v1.jsonl
│   └── eval/
├── scripts/
│   ├── axiom_infer.py
│   ├── axiom_train.py
│   └── axiom_eval.py
├── docs/
│   ├── index.md
│   ├── architecture.md
│   ├── training.md
│   └── deployment.md
└── examples/
    ├── basic_chat.py
    └── identity_check.py
```

## Training
- Full fine-tuning: `python scripts/axiom_train.py --mode full --model-path /path/to/base --dataset data/axiom-identity-v1.jsonl --output output/full`
- LoRA fine-tuning: `python scripts/axiom_train.py --mode lora --model-path /path/to/base --dataset data/axiom-identity-v1.jsonl --output output/lora`

## Evaluation
Identity, reasoning, and safety suites are provided to detect drift and policy violations. See `scripts/axiom_eval.py`.

## License
See [LICENSE](LICENSE).
