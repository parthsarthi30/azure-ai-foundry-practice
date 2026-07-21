import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

print("Endpoint:", endpoint)
print("Key loaded:", api_key is not None)

client = AzureOpenAI(azure_endpoint=endpoint, api_key=api_key, api_version="2024-10-21")

response = client.chat.completions.create(
    reasoning_effort="minimal",
    model="gpt-5-mini",
    messages=[
        {"role": "user", "content": "Explain what Azure AI Foundry is in one sentence."}
    ],
)

print(response.choices[0].message.content)
