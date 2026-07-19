# agent/registry.py

from tools.tool import Tool


class ToolRegistry:

    def __init__(self):
        """
        保存所有 Tool
        key: tool name
        value: Tool对象
        """
        self.tools: dict[str, Tool] = {}

    def register(self, tool: Tool):
        """
        注册一个Tool
        """
        name = tool.schema["function"]["name"]
        self.tools[name] = tool

    def get_tool(self, name: str) -> Tool | None:
        """
        根据名字获取Tool
        """
        return self.tools.get(name)

    def get_all_schemas(self):
        """
        返回所有Tool Schema
        给LLM使用
        """
        return [
            tool.schema
            for tool in self.tools.values()
        ]

    def execute(self, name: str, **kwargs):
        """
        根据Tool名称执行
        """
        tool = self.get_tool(name)

        if tool is None:
            raise ValueError(f"Tool '{name}' 不存在")

        return tool.execute(**kwargs)

    def list_tools(self):
        """
        调试使用
        """
        return list(self.tools.keys())