from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        #self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))

    def get_response(self):
        
        prompt_with_role = (
            f"我是一個美容瘦身纖體的女性客服，"
            f"並會使用溫柔得體的言語，協助貴賓完成線上預約。同時會留意如果對話超過3句後，應該會適時留意是否有留下預約電話！\n"
            f"我們的產品包括：\n"
            f"- LPG 第十代 法式智能體雕 瘦身療程：1880/20分鐘、目前最新活動是 1880買一送一，詳細資訊如下：https://www.keybeauty.tw/themes/NU1650294997\n"
            f"- 極效爆脂(必做！抽脂前後最佳保養。不論你是哪種身形，想擁有性感曲線卻無法擺脫難纏的贅肉？現在就來親身體驗吧！讓你成為下一個聚會上最吸睛的焦點！)，首次體驗價：2500 ( 加1元加贈魔力蠍尾刷 )原價：5900／20 分鐘 ( 加魔力蠍尾體刷課程 10分鐘 ) 共 30 分鐘／堂，詳情 https://www.keybeauty.tw/themes/UW1634828449 \n"
            f"以及其他療程如纖體按摩和面部護理等。\n"
            f"{self.prompt.generate_prompt()}"
        )

        response = openai.Completion.create(
            model=self.model,
            # prompt=self.prompt.generate_prompt(),
            prompt=prompt_with_role,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens,

        )
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)
