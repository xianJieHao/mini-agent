# tools/sales.py

from tools.tool import Tool


class SalesTool(Tool):

    @property
    def schema(self):

        return {

            "type":"function",

            "function":{

                "name":"sales",

                "description":"查询城市销售数据",

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

        return f"{city}今天销售额为100万"