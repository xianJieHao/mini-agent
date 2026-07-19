from tools.tool import Tool


class WeatherTool(Tool):

    @property
    def schema(self):

        return {

            "type":"function",

            "function":{

                "name":"weather",

                "description":"查询城市天气",

                "parameters":{

                    "type":"object",

                    "properties":{

                        "city":{

                            "type":"string",

                            "description":"城市名称"
                        }

                    },

                    "required":[
                        "city"
                    ]

                }

            }

        }


    def execute(self, city):

        return f"{city}今天晴天，32度"