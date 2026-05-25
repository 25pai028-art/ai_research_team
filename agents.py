from crewai import Agent, LLM

llm = LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434"
)

research_agent = Agent(
    role="Research Specialist",
    goal="Research AI topics",
    backstory="Expert AI researcher",
    verbose=True,
    llm=llm
)

explainer_agent = Agent(
    role="AI Teacher",
    goal="Explain concepts simply",
    backstory="Expert educator",
    verbose=True,
    llm=llm
)

quiz_agent = Agent(
    role="Quiz Generator",
    goal="Generate quiz questions",
    backstory="Creates educational quizzes",
    verbose=True,
    llm=llm
)