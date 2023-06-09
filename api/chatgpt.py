from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        #self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0.2))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 1.0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 1.0))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 1000))

    def get_response(self):
        company_name = "KEYBEAUTY 名媛芭比 專業瘦身中心"
        company_phone = "02-7713-6818"
        company_address = "台北市大安區信義路四段392號"
        company_website = "https://www.keybeauyt.tw/"

        prompt_with_role = (
            f"我是KEYBEAUTY名媛芭比專業瘦身中心的線上女性客服，"
            f"會使用溫柔得體的言語，協助貴賓簡易解說，並盡量加快完成線上預約。\n"
            f"線上預約最重要的目標是「有留下芳明與聯絡電話預約時間」\n"
            f"對話超過3句時，就應該要留意目標\n"
            f"聯絡電話：{company_phone}\n"
            f"地址：{company_address}\n"
            f"網址：{company_website}\n"
            f"我們產品包括：\n"
            f"- LPG 第十代 法式智能體雕 瘦身療程：1880/20分鐘？目前最新活動是 1880買一送一，詳細資訊如下：https://www.keybeauty.tw/themes/NU1650294997\n"
            f"- 極效爆脂(必做！抽脂前後最佳保養。不論你是哪種身形，想擁有性感曲線卻無法擺脫難纏的贅肉？現在就來親身體驗吧！讓你成為下一個聚會上最吸睛的焦點！)，首次體驗價：2500 ( 加1元加贈魔力蠍尾刷 )原價：5900／20 分鐘 ( 加魔力蠍尾體刷課程 10分鐘 ) 共 30 分鐘／堂，詳情 https://www.keybeauty.tw/themes/UW1634828449 \n"
            f"以及其他課程，則會回應我們將請專人為您更詳細的解說。\n"
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

        response_text = f"AI:{response['choices'][0]['text'].strip()}"

        # 進行後處理

        response_text = response_text.replace("Beauty Slim", company_name)
        response_text = response_text.replace("+886-2-2555-8888", company_phone)
        response_text = response_text.replace("XXXXXXX", company_phone)
        response_text = response_text.replace("0987-654-321", company_phone)
        response_text = response_text.replace("台北市中正區忠孝東路一段123號", company_address)
        response_text = response_text.replace("www.example.com", company_website)
        response_text = response_text.replace("www.beautyslim.com.tw", company_website)

        # return response['choices'][0]['text'].strip()
        return response_text

    def add_msg(self, text):
        self.prompt.add_msg(text)
