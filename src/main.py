from prompt_builder import PromptBuilder
from reasoning_engine import ReasoningEngine

with open("prompts/react_prompt.txt", "r") as f:
    template = f.read()

builder = PromptBuilder(template)
engine = ReasoningEngine()

prompt = builder.build_prompt("How old is viral kohli")

response = engine.generate(prompt)

from action_parser import ActionParser

parser = ActionParser()

parsed = parser.parse(response)

#print(parsed)

from wikipedia_tool import WikipediaTool

tool = WikipediaTool()

if parsed["action"] == "search":
    observation = tool.search(parsed["argument"])
    print("\nObservation:")
    print(observation)