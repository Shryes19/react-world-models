class PromptBuilder:
    def __init__(self, prompt_template: str):
        self.prompt_template = prompt_template

    def build_prompt(self, question: str, history: str = "") -> str:
        prompt = self.prompt_template
        prompt += f"\n\nQuestion: {question}\n"
        if history:
            prompt += history
        return prompt