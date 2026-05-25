from crewai import Task
from agents import (
    research_agent,
    explainer_agent,
    quiz_agent
)

def create_tasks(topic):

    research_task = Task(
        description=f"""
        Research the topic: {topic}

        Give:
        1. Definition
        2. Key Concepts
        3. Real-world Applications
        4. Advantages
        5. Challenges

        Keep the answer concise and structured.
        """,
        expected_output="Structured research notes",
        agent=research_agent
    )

    explanation_task = Task(
        description=f"""
        Explain {topic} to a beginner.

        Use:
        - simple language
        - short paragraphs
        - real-life examples
        """,
        expected_output="Beginner-friendly explanation",
        agent=explainer_agent
    )

    quiz_task = Task(
        description=f"""
        Create exactly 5 MCQs about {topic}.

        Rules:
        - Each question must have 4 options
        - Mention the correct answer
        - Keep questions short
        - Avoid repetition
        """,
        expected_output="5 multiple-choice questions",
        agent=quiz_agent
    )

    return [research_task, explanation_task, quiz_task]