import requests
import openai

def request_chatgpt_function():

    url="https://api.openai.com/v1/chat/completions"   #可以替换为任何代理的接口
    OPENAI_API_KEY="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"  # openai官网获取key
    header={"Content-Type": "application/json","Authorization": "Bearer " +OPENAI_API_KEY}
    data={
        "model": "gpt-5.4",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "Hello!"
          }
        ],
        "temperature":0,
        "stream":False
      }
    response=requests.post(url=url,headers=header,json=data).json()
    print(response)
    return response



def openai_chatgpt_function():
    question="西游记是谁写的？"
    print("问题:{}".format(question))
    url="https://api.openai.com/v1"   #可以替换为任何代理的接口
    OPENAI_API_KEY="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"  # openai官网获取key
    openai.api_key = OPENAI_API_KEY
    openai.api_base = url
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",messages=[{"role": "user", "content": question}],stream=False)
    print("完整的响应结果:{}".format(response))
    answer=response.choices[0].message.content
    print("答案:{}".format(answer))

if __name__ == "__main__":
    # openai_chatgpt_function()  # 利用openai正常调用
    request_chatgpt_function()