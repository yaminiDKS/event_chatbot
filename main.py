import streamlit as st
from groq import Groq

st.set_page_config(page_title="Event Suggestion AI", layout="wide")

# ---- TOP BAR ----
left, right = st.columns([6, 1])

with right:
    st.link_button(
        "Vendor Recommendation",
        "https://vendor-recommendation-chatbot-jtmxjffyqsp4qxwtfu9dql.streamlit.app/",
        use_container_width=True
    )

# ---- LOAD API KEY FROM SECRETS ----
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.title("MakeYourDream")

user_input = st.text_area(
    "Enter event details (theme, type, location, audience, etc.)"
)

if st.button("Generate Suggestions"):
    if not user_input.strip():
        st.warning("Enter something.")
    else:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a model built for a startup that wants you to give personalized "
                    "suggestions on events like color schemes, seating arrangements, budget aspects, "
                    "and current trends for more reach based on the user's input. "
                    "Do NOT ask the user questions."
                ),
            },
            {"role": "user", "content": user_input},
        ]

        response_area = st.empty()
        result = ""

        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=1,
            max_completion_tokens=8192,
            top_p=1,
            reasoning_effort="medium",
            stream=True,
            stop=None,
        )

        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            result += content
            response_area.markdown(result)
