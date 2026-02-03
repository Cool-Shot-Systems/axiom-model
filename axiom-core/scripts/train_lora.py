#!/usr/bin/env python
"""Run LoRA fine-tuning for AXIOM."""

import argparse
from pathlib import Path

from axiom.training.lora import LoRAConfig, run_lora_finetune


def main() -> None:
    parser = argparse.ArgumentParser(description="Train AXIOM with LoRA")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    args = parser.parse_args()

    config = LoRAConfig(
        model_path=args.model_path,
        dataset_path=args.dataset,
        output_path=args.output,
        epochs=args.epochs,
        batch_size=args.batch_size,
    )
    run_lora_finetune(config)


if __name__ == "__main__":
    main()
