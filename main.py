from src.agent import agent_smith

def main():
    while True:
        user_text = input("You: ")
        answer = agent_smith.run(user_text)
        print(f"Smith: {answer}")

if __name__ == "__main__":
    main()
