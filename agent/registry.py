# registry.py

class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.values())
    
    def build_prompt(self):
        result = ""
        for tool in self.list_tools():
            result += f"工具：{tool.name}\n功能：{tool.description}\n参数：{tool.parameters}\n"
        return result

