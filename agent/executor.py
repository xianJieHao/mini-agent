import json


class ToolExecutor:


    def __init__(self, registry):

        self.registry = registry



    def execute(self, tool_call):


        function = tool_call["function"]


        name = function["name"]


        arguments = function["arguments"]


        try:

            result = self.registry.execute(
                name,
                **arguments
            )


            return {

                "tool_call_id":
                    tool_call["id"],

                "content":
                    json.dumps(
                        result,
                        ensure_ascii=False
                    )

            }


        except Exception as e:


            return {

                "tool_call_id":
                    tool_call["id"],

                "content":
                    json.dumps(
                        {
                            "error":str(e)
                        },
                        ensure_ascii=False
                    )

            }