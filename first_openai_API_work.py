from openai import OpenAI, OpenAIError # OpenAI 官方套件
import getpass # 保密輸入套件
api_key = getpass.getpass("請輸入金鑰：")
client = OpenAI(api_key = api_key) # 建立 OpenAI 物件
reply = client.chat.completions.create(
     model = "gpt-3.5-turbo",
    # model = "gpt-4o",
    # model = "gpt-4o-2024-11-20",
    # model = "chatgpt-4o-latest",
    # model = "gpt-4-turbo-preview",
    messages = [
        {"role":"user", "content": "你知道截至今天2024年8月2日台灣的總統是誰嗎？"}
    ]
)
print(reply)