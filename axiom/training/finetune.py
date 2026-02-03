"""Full fine-tuning pipeline for AXIOM."""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from axiom.training.datasets import iter_training_text, load_jsonl


@dataclass
class FineTuneConfig:
    model_path: Path
    output_path: Path
    dataset_path: Path
    epochs: int = 1
    batch_size: int = 1
    learning_rate: float = 2e-5


class TextDataset:
    def __init__(self, tokenized: dict) -> None:
        self.tokenized = tokenized

    def __len__(self) -> int:
        return self.tokenized["input_ids"].shape[0]

    def __getitem__(self, idx: int) -> dict:
        return {
            "input_ids": self.tokenized["input_ids"][idx],
            "attention_mask": self.tokenized["attention_mask"][idx],
            "labels": self.tokenized["input_ids"][idx],
        }


def run_full_finetune(config: FineTuneConfig) -> None:
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

    tokenizer = AutoTokenizer.from_pretrained(config.model_path)
    model = AutoModelForCausalLM.from_pretrained(config.model_path)

    examples = load_jsonl(config.dataset_path)
    training_text: List[str] = list(iter_training_text(examples))

    tokenized = tokenizer(training_text, return_tensors="pt", padding=True, truncation=True)
    dataset = TextDataset(tokenized)

    training_args = TrainingArguments(
        output_dir=str(config.output_path),
        num_train_epochs=config.epochs,
        per_device_train_batch_size=config.batch_size,
        learning_rate=config.learning_rate,
        logging_steps=10,
        save_steps=50,
    )

    trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
    trainer.train()
    trainer.save_model(str(config.output_path))


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run full fine-tuning for AXIOM")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--learning-rate", type=float, default=2e-5)
    args = parser.parse_args()

    config = FineTuneConfig(
        model_path=args.model_path,
        dataset_path=args.dataset,
        output_path=args.output,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
    )
    run_full_finetune(config)


if __name__ == "__main__":
    main()
