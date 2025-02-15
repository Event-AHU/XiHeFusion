# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import os
client = OpenAI(
        api_key="your_api_key",
        base_url=f"http://localhost:{os.environ.get('API_PORT', 8005)}/v1",
    )

system_prompt_file_path = 'prompt/siwei.txt'
with open(system_prompt_file_path, 'r', encoding='utf-8') as file:
    system_prompt = file.read().strip()
messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': "Hello!"},
]

response = client.chat.completions.create(
    model="test",
    messages=messages,
)

print(response.choices[0].message.content)

