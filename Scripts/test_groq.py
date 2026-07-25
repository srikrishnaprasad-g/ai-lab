import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="qwen/qwen3.6-27b",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: OK"
        }
    ],
)

print("Model:", response.model)
print("Response:", response.choices[0].message.content)