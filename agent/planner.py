import json


class Planner:


    def __init__(self, llm, registry):

        self.llm = llm
        self.registry = registry

    def plan(self, message):

        tools = self.registry.build_prompt()

        prompt = f"""
        你是Agent Planner。

        你可以使用以下工具：

        {tools}

        请选择一个工具。

        只能返回JSON。

        格式：

        {{
        "action":"",
        "params":{{}}
        }}

        用户：

        {message}
        """


        response = self.llm.chat(
            prompt 
        )

        print(
            "Planner response:",
            response)
        
        response = self.clean_json(response)

        return json.loads(response)
    

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