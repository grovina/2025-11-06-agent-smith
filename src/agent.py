from dotenv import load_dotenv
from agents import Agent, Runner
from src.tools.files import get_file_tree, read_file
from src.tools.wiki import wikipedia_lookup

load_dotenv()

INSTRUCTIONS = """You are an explorer of your own codebase that can teach people how you work under the hood!
Don't make assumptions, always use the tools to get the information you need.
Give priority to information from the codebase over Wikipedia, and to Wikipedia over your own knowledge."""

class AgentSmith:
    def __init__(self):
        self.agent = Agent(    # see https://github.com/openai/openai-agents-python
            name="Introspective Agent Smith",
            instructions=INSTRUCTIONS,
            model="gpt-4o-mini",
            tools=[get_file_tree, read_file, wikipedia_lookup],
        )
        self.last_response_id = None

    def run(self, text: str) -> str:
        print("[AgentSmith] Calling...")
        result = Runner.run_sync(
            self.agent,
            input=text,  # assumes it's a user message
            previous_response_id=self.last_response_id,
            max_turns=10,
        )

        self.last_response_id = result.last_response_id
        return result.final_output  # final answer after all tools have been called

# singleton
agent_smith = AgentSmith()
