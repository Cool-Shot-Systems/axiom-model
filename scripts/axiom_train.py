#!/usr/bin/env python
"""Run fine-tuning for AXIOM."""

import argparse
from pathlib import Path

from axiom.__version__ import __version__
from axiom.training.finetune import FineTuneConfig, run_full_finetune
from axiom.training.lora import LoRAConfig, run_lora_finetune


def main() -> None:
    parser = argparse.ArgumentParser(description="Train AXIOM")
    parser.add_argument("--version", action="version", version=f"AXIOM {__version__}")
    parser.add_argument("--mode", choices=["lora", "full"], default="lora")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--learning-rate", type=float, default=None)
    args = parser.parse_args()

    if args.mode == "full":
        config = FineTuneConfig(
            model_path=args.model_path,
            dataset_path=args.dataset,
            output_path=args.output,
            epochs=args.epochs,
            batch_size=args.batch_size,
            learning_rate=args.learning_rate or 2e-5,
        )
        run_full_finetune(config)
    else:
        config = LoRAConfig(
            model_path=args.model_path,
            dataset_path=args.dataset,
            output_path=args.output,
            epochs=args.epochs,
            batch_size=args.batch_size,
            learning_rate=args.learning_rate or 2e-4,
        )
        run_lora_finetune(config)


if __name__ == "__main__":
    main()
