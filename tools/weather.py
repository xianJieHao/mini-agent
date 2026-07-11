from tools.tool import Tool


class WeatherTool(Tool):
    @property
    def name(self):
        return "weather"

    @property
    def description(self):
        return "查询城市天气信息"

    def execute(self, city):
        return f"{city}今天30℃,晴天" 
   