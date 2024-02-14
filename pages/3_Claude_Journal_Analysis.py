import streamlit as st
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# ------------------------ Environment and API Setup ------------------------ #

# #env_path = os.path.join('model', '.env')
# env_path = '/Users/sonyashijin/CS224G/MindStorm/model/.env'
# load_dotenv(dotenv_path = env_path) 

# anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
# anthropic = Anthropic(api_key = anthropic_api_key)

# if anthropic_api_key is None:
#     st.error("Anthropic API key is not loaded.")

# Attempt to access the Anthropics API key from secrets.toml
try:
    anthropic_api_key = st.secrets["anthropic"]["api_key"]
except KeyError:
    with st.sidebar:
        anthropic_api_key = st.text_input("Anthropic API Key", key="journal_api_key", type="password")
anthropic = Anthropic(api_key=anthropic_api_key)
# ------------------------ Function Definitions ------------------------ #

def get_ai_response(user_input, response_mode, tone=None, name = ""):
    # update conversation history
    st.session_state.conversation_history += f"\n{HUMAN_PROMPT} {user_input}"

    # Modify the prompt based on the chosen response mode
    if response_mode == "best_friend":
        tone_prompt = {
            "funny": "in a funny way",
            "tough_love": "with tough love, tiger mom style, and don't be comforting (be as harsh as possible),",
            "gen-z": "using gen-z tone and slang, but not too much,",
            "comforting": "in a comforting way"
        }.get(tone, "")
        mode_prompt = f"My name is {name}. I want someone to talk to about my feelings. Respond as my best friend giving a pep talk {tone_prompt} and personalize response considering my story:"
    elif response_mode == "existential_therapy":
        mode_prompt = f"My name is {name}. I want someone to talk to about my feelings. Respond with existential therapy advice and personalize response considering my story:"
    elif response_mode == "cbt":
        mode_prompt = f"My name is {name}. I want someone to talk to about my feelings. Respond using Cognitive Behavioral Therapy (CBT) and personalize response considering my story:"

    full_prompt = f"{st.session_state.conversation_history}\n{mode_prompt}{AI_PROMPT}"
    return full_prompt

def center_buttons():
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        display: block;
        margin: 0 auto;
    }
    </style>""", unsafe_allow_html=True)

# ------------------------ Streamlit App Interface ------------------------ #

st.title("🧠 Claude's Journal Analysis")

# Text area for journal input
name = st.text_area("Tell me about yourself.", placeholder = "Your name and any background info we should know")

user_input = st.text_area("Input your journal entry", placeholder="How are you feeling today?", height=200)

response_mode = st.selectbox("Choose the response mode:", ["best_friend", "existential_therapy", "cbt"])

tone = None
if response_mode == "best_friend":
    tone = st.selectbox("Choose the tone:", ["funny", "tough_love", "gen-z", "comforting"])

submit_button = st.button("Respond to my thoughts")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = ""

if submit_button:
    if not user_input.strip():
        st.error("Write something in the text box pls")

if submit_button and user_input and anthropic_api_key:
    ai_response = get_ai_response(user_input, response_mode, tone, name)
    try:
        # Request a completion from the Anthropics API
        response = anthropic.completions.create(
            prompt=ai_response,
            model="claude-2.1",  # Adjust the model version if needed
            max_tokens_to_sample=300,  # Adjust based on your requirements
        )
        st.session_state.conversation_history += f" {response.completion}"

        # Display the response from the API
        st.write(response.completion)

        col1, col2 = st.columns(2)  # Create two columns

        center_buttons()

        with col1:
            st.button("Hits 🥹")

        with col2:
            st.button("Ain't hittin 😥")

        if st.button("Clear Journal History"):
            st.session_state.conversation_history = ""
            st.success("Journal history cleared.")       
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")