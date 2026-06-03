from openai import OpenAI

client = OpenAI(
    base_url="https://www.zeoapi.com/v1",
    api_key="sk-2i8gFll062IYg0SQ12gEGcOhooGFaEym0vCrEmuSLJQvxJzH"
)

resp = client.chat.completions.create(
    model="claude-opus-4-6-thinking",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=1024
)
print(resp)