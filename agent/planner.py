from agent.action import Action


class Planner:
   
    def plan(self, user_input):
       
       if "天气" in user_input:
            return Action.TOOL
       
       if "销售" in user_input:
            return Action.TOOL

       if "制度" in user_input:
            return Action.RAG

       return Action.CHAT
       