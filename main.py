# main.py


from agent.agent import Agent



def main():


    agent = Agent()


    while True:


        user_input = input(
            "You:"
        )


        if user_input == "exit":
            break


        answer = agent.chat(
            user_input
        )


        print(
            "AI:",
            answer
        )



if __name__ == "__main__":

    main()