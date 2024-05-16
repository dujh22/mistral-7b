from vllm import LLM

text = ["我是一个人工智能助手，我能够帮助你做如下这些事情："]

llm = LLM(model="/workspace/dujh22/models/mistral-7B-v0.1")  # Create an LLM.

outputs = llm.generate(text)  # Generate texts from the prompts.

print(outputs)