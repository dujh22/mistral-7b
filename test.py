import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda:4") if torch.cuda.is_available() else torch.device("cpu")

model_path = "/workspace/dujh22/models/mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map=device)

text = "我是一个人工智能助手，我能够帮助你做如下这些事情："
inputs = tokenizer(text, return_tensors="pt").to(device)

outputs = model.generate(**inputs, max_new_tokens=120, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
