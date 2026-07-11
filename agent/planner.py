import json


class Planner:


    def __init__(self, llm):

        self.llm = llm

    def plan(self, message):


        prompt = f"""
你是一个任务规划器。

你有以下工具：

1.weather
功能：查询天气
参数：
city


2.sales
功能：查询销售数据


根据用户输入，
选择需要调用的工具。


只返回JSON。

格式：

{{
"action":"",
"params":{{}}
}}


用户输入：

{message}

"""


        response = self.llm.chat(
            prompt 
        )



        print(
            "Planner response:",
            response)

        return json.loads(self.clean_json(response))
    

    def clean_json(self, text):


        text = text.strip()


        if text.startswith("```"):


            text = text.replace(
                "```json",
                ""
            )


            text = text.replace(
                "```",
                ""
            )


        return text.strip()