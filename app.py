import streamlit as st
from google import genai
import os

st.title("Engineering Mathematics Tutor 📚")
st.write("Ask any B.Tech first-year Mathematics question.")

question = st.text_area("Enter your question:")

if st.button("Get Solution"):
    if question.strip():
        try:
            client = genai.Client(
                api_key=os.environ["GEMINI_API_KEY"]
            )

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=f"""
                Solve this Engineering Mathematics question
                step by step in simple Hinglish:
                {question}
                """
            )

            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
