from src.analyzer import analyze_sentence

while True:
    user_input = input("请输入一句英文（输入exit退出）：")

    if user_input.lower() == "exit":
        break

    print("\n🤖 AI正在分析，请稍等...\n")

    result = analyze_sentence(user_input)

    print("\n分析结果：\n")
    print(result)
    print("\n" + "="*50 + "\n")