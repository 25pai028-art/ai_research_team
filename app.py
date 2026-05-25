import streamlit as st

from agents import (
    research_agent,
    explainer_agent,
    quiz_agent
)

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Research Assistant")

topic = st.text_input("Enter a topic")

if st.button("Generate"):

    with st.spinner("Agents are working..."):

        # Research Agent
        research = research_agent.llm.call(
            f"""
            Research the topic: {topic}

            Include:
            - Definition
            - Applications
            - Advantages
            - Challenges
            """
        )

        # Explainer Agent
        explanation = explainer_agent.llm.call(
            f"""
            Explain {topic} in very simple beginner-friendly language.
            """
        )

        # Quiz Agent
        quiz = quiz_agent.llm.call(
            f"""
            Create 5 MCQs about {topic}.

            Format:
            Question
            A)
            B)
            C)
            D)
            Correct Answer:
            """
        )

        st.subheader("📘 Research")
        st.markdown(research)

        st.subheader("🧠 Simple Explanation")
        st.markdown(explanation)

        st.subheader("❓ Quiz")
        st.markdown(quiz)