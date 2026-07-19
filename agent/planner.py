import json


class Planner:

    def __init__(self, llm, registry):
        self.llm = llm
        self.registry = registry

    def plan(self, message: str):

        schemas = self.registry.get_all_schemas()

        prompt = self.build_prompt(
            schemas,
            message
        )

        print("\nPlanner prompt:")
        print(prompt)

        response = self.llm.chat(prompt)

        print("\nPlanner response:")
        print(response)

        response = self.clean_json(response)

        return json.loads(response)

    def build_prompt(self, schemas, message):

        return f"""
你是一个AI Agent的Planner。

你的任务是分析用户的问题。

下面是当前系统拥有的工具。

{json.dumps(schemas, ensure_ascii=False, indent=2)}

如果需要调用工具，请返回：

{{
    "action":"工具名称",
    "params":{{
        ...
    }}
}}

如果不需要工具，请返回：

{{
    "action":"chat",
    "params":{{}}
}}

注意：

1、只能返回JSON
2、不要解释
3、不要使用 Markdown
4、不要输出 ```json

用户问题：

{message}
"""

    def clean_json(self, text):

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")

        if text.startswith("```"):
            text = text.replace("```", "")

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()