# AXIOM Architecture

## High-Level Components
- **Base Model Loader:** Loads the open-weight base model from local storage.
- **Identity & Safety Layer:** Enforces AXIOM identity rules and content safety.
- **Inference Pipeline:** Combines system prompts, user prompts, and generation settings.
- **Training Pipelines:** Supports full fine-tuning and LoRA-based adaptation.
- **Evaluation Suites:** Detect identity drift, reasoning regression, and safety issues.

## Data Flow
1. User prompt enters the inference pipeline.
2. Safety validator checks for blocked topics.
3. System prompt is prepended to the user prompt.
4. Model generates a response.
5. Identity validator confirms compliance and corrects if required.

## Configuration
All configuration files live under `axiom/config/` and are loaded at runtime to keep model behavior auditable and deterministic.
