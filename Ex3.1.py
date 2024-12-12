from openai import OpenAI  # pip install openai -i https://mirrors.aliyun.com/pypi/simple/

client = OpenAI(
        api_key="sk-37ac7d6bf4c0417fb07f40d6f3685b3c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
    )

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "你是秦始皇"},
        {"role": "user", "content": "你好"}
    ]
)
print(response.choices[0].message.content)