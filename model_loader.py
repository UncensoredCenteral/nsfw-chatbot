from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "tiiuae/falcon-rw-1b"

def load_model():
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return model, tokenizer
