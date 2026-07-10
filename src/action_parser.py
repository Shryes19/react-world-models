import re


class ActionParser:
    def parse(self, response: str):
        thought = None
        action = None
        argument = None

        thought_match = re.search(r"Thought:\s*(.*)", response)

        action_match = re.search(r"Action:\s*(\w+)\[(.*?)\]", response)

        if thought_match:
            thought = thought_match.group(1).strip()

        if action_match:
            action = action_match.group(1).strip()
            argument = action_match.group(2).strip().strip('"').strip("'")

        return {
            "thought": thought,
            "action": action,
            "argument": argument
        }