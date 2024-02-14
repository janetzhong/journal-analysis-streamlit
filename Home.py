import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# 📝 Mindstorm Demos")

st.sidebar.success("Select a demo above.")

# Link to view the source code
source_code_url = "https://github.com/janetzhong/journal-analysis-streamlit"
st.markdown(f"[View Source Code]({source_code_url})", unsafe_allow_html=True)


st.write("""

This demo offers tools designed to provide you with deeper insights into your personal journal entries. It aims to help you understand your emotional landscape over time or uncover the predominant themes occupying your thoughts.

### How It Works

- 📡 **Journal Emotion Radar with Huggingface**: Gives you an emotional radar plot from an input journal entry of six emotions from huggingface model `michellejieli/emotion_text_classifier'.

- 🍰 **Brain Real Estate with Anthropic**: Categorizes an input journal entry into five main themes using Claude model from Anthropic and plots % brain real estate for each theme in a pie chart.

- 🧠 **Claude Journal Analysis**: Get a response in best friend mode in different tones or CBT-guided mode using Claude.

- 📈 **Multiple Journal Entry Analysis**: (coding in progress)

- 🎨 **Journal Cover Art Generator**: (coding in progress)


👈  To get started, simply select a demo from the sidebar.
""")