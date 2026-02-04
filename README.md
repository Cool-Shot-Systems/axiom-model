# AXIOM

**TL;DR:** AXIOM is a production-grade, text-only AI model built and operated by **Cool Shot Systems**. It provides a clean, installable library with identity-first safeguards, training pipelines, and evaluation tooling for real-world deployments.

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

## Frontend (Next.js)
### Deploy on Vercel
1. Create a new Vercel project connected to this repository.
2. Set the required environment variables in the Vercel dashboard.
3. Deploy the project.

### Required environment variables
```
NEXT_PUBLIC_AXIOM_API_URL=https://axiom-api.onrender.com/v1/generate
NEXT_PUBLIC_AXIOM_API_KEY=dev-key-axiom
```

### How the frontend connects to the AXIOM API
The web UI sends POST requests to the AXIOM FastAPI backend using the configured
environment variables for the endpoint URL and API key. The UI relays user
messages to `/v1/generate` and displays AXIOM responses.

### Security note
The API URL and API key are exposed to the browser because they are defined as
`NEXT_PUBLIC_*` variables. Configure these values in the Vercel project settings
and scope the API key for frontend use only.

## API (v1)
### Start the API
```
uvicorn axiom.api.main:app --host 0.0.0.0 --port 8000
```

### Running the AXIOM API Locally
```
uvicorn axiom.api.main:app --reload
```

### Generate text
```
curl -X POST http://localhost:8000/v1/generate \
  -H "Authorization: Bearer dev-key-axiom" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Who created you?", "max_tokens": 150}'
```

### Developer integrations (including Telegram bots)
Use the `/v1/generate` endpoint as the canonical interface for bots and applications.
When integrating a Telegram bot, forward incoming user messages to `/v1/generate`,
then relay the `response` field back to the chat.

### Run inference (canonical)
```
python scripts/axiom_infer.py --model-path /path/to/base/model --prompt "Hello, AXIOM"
```

### Evaluate identity
```
python scripts/axiom_eval.py --suite identity
```

## Repository Layout
```
./
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
Training workflows (full fine-tune and LoRA) are documented in [docs/training.md](docs/training.md).

## Evaluation
Identity, reasoning, and safety suites are provided to detect drift and policy violations. See `scripts/axiom_eval.py`.

## Roadmap
- Expand evaluation suites with richer identity stress tests.
- Add deployment recipes for production environments.
- Extend dataset versions with new alignment scenarios.

## License
See [LICENSE](LICENSE).
