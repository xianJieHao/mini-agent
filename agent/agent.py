from agent.action import Action


class Agent:
    def __init__(self, client, planner, registry):
        self.client = client
        self.planner = planner
        self.registry = registry

    def chat(self, user_input):
        messages = []
        action = self.planner.plan(user_input)
        if action == Action.CHAT:
             messages = [
                {
                    "role": "user",
                    "content": user_input
                }
             ]
             return self.client.chat(messages)
        elif action == Action.TOOL:
             return self.handle_tool_action(user_input)

    def handle_tool_action(self, user_input):
        if "天气" in user_input:
            tool = self.registry.get("WeatherTool")
            if tool:
                result = tool.execute(city="广州")
            else:
                return "天气工具未注册。"
        elif "销售" in user_input:
            tool = self.registry.get("SalesTool")
            if tool:
                result = tool.execute(month="7")
            else:
                return "销售工具未注册。"
        else:
            result = "未找到匹配的工具。"
        
        messages = [
            {
                "role": "user",
                "content": user_input
            },
            {
                "role": "tool",
                "content": result
            }
        ]
        return self.client.chat(messages)
