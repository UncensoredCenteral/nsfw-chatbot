import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
        overwrite_cache=True
    )

def main():
    model_name = "gpt2"  # GPT-2 small, 124M params
    dataset_path = "nsfw_multiturn_dialogues.txt"

    # Load tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Load dataset
    train_dataset = load_dataset(dataset_path, tokenizer)

    # Data collator handles batching and masking
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Setup training arguments — tweak epochs and batch size for your hardware
    training_args = TrainingArguments(
        output_dir="./gpt2-nsfw-finetuned",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=1,
        save_steps=500,
        save_total_limit=2,
        prediction_loss_only=True,
        logging_steps=100,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
    )

    print("Starting fine-tuning... this might take a while on CPU...")
    trainer.train()

    # Save the final model
    trainer.save_model("./gpt2-nsfw-finetuned")
    tokenizer.save_pretrained("./gpt2-nsfw-finetuned")

    print("Fine-tuning complete! Model saved to ./gpt2-nsfw-finetuned")

if __name__ == "__main__":
    main()
