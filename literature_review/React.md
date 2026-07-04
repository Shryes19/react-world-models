ReAct
Paper Information
Title: REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS
.
Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao
.
Conference: The provided source is an arXiv preprint (and was later published at ICLR 2023)
.
Year: 2022
.
Problem Statement
The paper aims to solve the problem of Large Language Models (LLMs) treating reasoning (like thinking) and acting (doing tasks) as separate things
. When reasoning is done in isolation, models often "hallucinate" or make up facts because they aren't connected to the outside world
. When acting is done without reasoning, models struggle to plan for complex goals or track their progress
.
What dataset(s) does it use? The researchers tested ReAct on four datasets: HotpotQA (multi-hop question answering), Fever (fact verification), ALFWorld (a text-based household game), and WebShop (online shopping navigation)
.
What model does it propose? It proposes ReAct, a paradigm that prompts LLMs to generate verbal reasoning traces and task-specific actions in an interleaved (back-and-forth) manner
. The experiments primarily use the PaLM-540B model, as well as GPT-3
.
How is performance evaluated? Performance is measured by Exact Match (EM) scores for question answering, accuracy for fact-checking, and success rates for interactive decision-making tasks
.
Motivation
Previous methods are insufficient because reasoning-only methods (like Chain-of-Thought) are a "black box" that cannot access or update knowledge from the external world
. This makes them prone to errors and misinformation
. Conversely, acting-only methods lack the ability to reason abstractly about high-level goals or maintain a working memory, which makes it harder for them to handle unexpected situations or complex plans
.