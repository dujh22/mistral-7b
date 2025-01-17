from vllm import LLM

text = ["我是一个人工智能助手，我能够帮助你做如下这些事情："]

llm = LLM(model="/workspace/dujh22/models/mistral-7B-v0.1")  # Create an LLM.

outputs = llm.generate(text)  # Generate texts from the prompts.

# print(outputs)

# 解析输出
for output in outputs:
    print("输入提示:", output.prompt)
    for completion in output.outputs:
        print("生成的文本:", completion.text)
    print("请求ID:", output.request_id)
    print("提示Token IDs:", output.prompt_token_ids)
    print("完成原因:", output.outputs[0].finish_reason)
    print("时间指标:", output.metrics)

# 处理 NCCL 警告
import torch.distributed as dist
if dist.is_initialized():
    dist.destroy_process_group()
