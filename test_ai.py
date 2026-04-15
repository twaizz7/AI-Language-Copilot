import dashscope
from dashscope import Generation

dashscope.api_key = "sk-cda7ce93c0054a49976f260a875bb472"

while True:
    user_input = input("请输入一句英文（输入exit退出）：")

    if user_input.lower() == "exit":
        break

    prompt = f"""
你是一个专业的语言学习助手，请严格按照以下格式分析句子。

【任务要求】
1. 逐词翻译
2. 标注词性
3. 分析句子结构
4. 解释语法点
5. 给出自然翻译

句子：
{user_input}
"""
    print("AI正在分析，请稍等...\n")

    response = Generation.call(
        model="qwen-turbo",
        prompt=prompt
    )

    print("\n分析结果：\n")
    print(response.output.text)
    print("\n" + "="*50 + "\n")