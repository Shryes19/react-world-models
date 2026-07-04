Key Observations
Synergy of Reasoning and Acting: While previous research treated reasoning (thinking) and acting (doing) as separate, ReAct combines them. Reasoning traces help the model track and update plans, while actions allow it to gather information from external sources like Wikipedia
.
Reduced Hallucination: In tasks like question answering, ReAct reduces the common issue of "hallucination" (making up facts) by allowing the model to interact with external knowledge bases to verify information
.
High Efficiency: ReAct is highly effective even with very little data. It outperformed complex methods that required thousands of training instances while using only one or two in-context examples
.
Human-Like Logic: The approach is inspired by how humans use "inner speech" to help them strategize, maintain a working memory, and realize when they need to look up new information
.
Potential Limitation
Difficulty of Learning in Large Action Spaces: Because the "language space" (the thoughts the model can generate) is unlimited, learning to reason and act at the same time is difficult and requires the model to have very strong language priors to start with
