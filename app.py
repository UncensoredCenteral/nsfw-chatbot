from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "mrm8488/GPT-2-finetuned-cornell-movie-dialog"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

while True:
    prompt = input("You: ")
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id)
    print("Bot:", tokenizer.decode(outputs[0], skip_special_tokens=True))
