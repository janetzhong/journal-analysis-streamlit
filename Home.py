import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# 📝 Journal Analysis Demos")

st.sidebar.success("Select a demo above.")

# Link to view the source code
source_code_url = "https://github.com/janetzhong/journal-analysis-streamlit"
st.markdown(f"[View Source Code]({source_code_url})", unsafe_allow_html=True)


st.write("""
## Discover Insights into Your Journal Entries

This interactive platform offers a suite of tools designed to provide you with deeper insights into your personal journal entries. Whether you're looking to understand your emotional landscape over time or uncover the predominant themes occupying your thoughts, our analysis demos are here to guide you.

### How It Works

- **Journal Emotion Radar with Huggingface**: Dive into the emotional depth of your journal entries. Our emotion analysis demo utilizes advanced natural language processing techniques to classify and visualize the emotions conveyed in your text.

- **Brain Real Estate with Anthropic**: Explore the thematic distribution of your journal content. This demo parses your entries to identify and quantify the main themes, offering you a unique perspective on what occupies your mind space.

👈  To get started, simply select a demo from the sidebar.
""")