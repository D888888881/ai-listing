import json
from openai import OpenAI

# ================== 配置 ==================
API_KEY = "sk-vzcf3MNFhMoveatXo88kt74Cspu1CB5ao4Uh4reoulooV2cI"  # 请替换成你自己的 key
BASE_URL = "https://api.openai-proxy.org/v1"
MODEL = "gpt-5.1"


# # ================== 读取 VOC 数据 ==================
# with open(VOC_FILE, "r", encoding="utf-8") as f:
#     voc_data = json.load(f)

# ================== 构造提示词 ==================
system_prompt = (
    "你是一位资深亚马逊产品分析师、消费者洞察专家"
)

user_prompt = f"""帮我分析"https://www.amazon.com/dp/B0FWJ8HNCB"这个链接的产品
"""

# ================== 调用 API ==================
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    model=MODEL
)

# ================== 输出结果 ==================
print(chat_completion.choices[0].message.content)
