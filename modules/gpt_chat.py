# modules/gpt_chat.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load tokenizer and model (uses PyTorch)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def gpt_reply(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
