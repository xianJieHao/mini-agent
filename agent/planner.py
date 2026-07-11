
class Planner:


    def plan(self, message):


        if "天气" in message:


            city = self.extract_city(message)


            return {
                "action":"weather",
                "params":{
                    "city":city
                }
            }



        if "销售" in message:


            return {
                "action":"sales",
                "params":{}
            }



        return {
            "action":"chat",
            "params":{}
        }



    def extract_city(self, message):


        cities = [
            "广州",
            "深圳",
            "北京",
            "上海"
        ]


        for city in cities:

            if city in message:

                return city


        return "未知城市"