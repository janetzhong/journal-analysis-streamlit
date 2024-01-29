import streamlit as st
import anthropic
import matplotlib.pyplot as plt

# Attempt to access the Anthropics API key from secrets.toml
try:
    anthropic_api_key = st.secrets["anthropic"]["api_key"]
except KeyError:
    with st.sidebar:
        anthropic_api_key = st.text_input("Anthropic API Key", key="journal_api_key", type="password")
        st.markdown("[View the source code](https://github.com/janetzhong/brain-real-estate-website)")

st.title("📝 Brain Real Estate with Anthropic")

# Text area for journal input
journal_text = st.text_area("Input your journal, recommended ~200+ words", placeholder="Type your journal here...", height=300)


# Brain real estate
submit_button = st.button('Get brain real estate')

def make_brain_real_estate_plot(analysis_text):
    # Initialize lists to hold themes and percentages
    themes = []
    percentages = []
    
    # Split the analysis text into lines
    lines = analysis_text.split('\n')
    
    # Loop through each line to find themes and percentages
    for line in lines:
        # Find lines that start with a number, indicating a new theme entry
        if line.strip().startswith(tuple(str(i) for i in range(1, 10))):
            try:
                # Extract the percentage, assuming it's always enclosed in parentheses
                percentage_start = line.find('(') + 1
                percentage_end = line.find('%)')
                percentage = int(line[percentage_start:percentage_end])
                
                # Extract the theme name, which comes before the percentage
                theme_name = line.split('.')[1].split('(')[0].strip()
                
                # Append the extracted theme and percentage
                themes.append(theme_name)
                percentages.append(percentage)
            except ValueError:
                # Handle cases where parsing fails
                st.error(f"Error parsing line: {line}")
                return
    
    # Check if we have data to plot
    if not themes or not percentages:
        st.error("No data available for plotting.")
        return
    
    # Plot the pie chart using matplotlib
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=themes, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    ax.axis('equal')  # Ensures the pie chart is drawn as a circle.

    # Display the pie chart in the Streamlit app
    st.pyplot(fig)

# Brain Real Estate App code
if submit_button and journal_text and anthropic_api_key:
    # Updated prompt with specific instructions for output format and to exclude closing remarks
    question = "if you had to make a pie chart of my brain real estate over the week, what are the five themes you would classify it as? Include as numbered list with theme title, percentages and description, without other remarks"
    prompt = f"{anthropic.HUMAN_PROMPT} Here's a journal entry:\n\n{journal_text}\n\n{question}\n\n{anthropic.AI_PROMPT}"

    # Initialize the Anthropics client with the provided API key
    client = anthropic.Client(api_key=anthropic_api_key)

    try:
        # Request a completion from the Anthropics API
        response = client.completions.create(
            prompt=prompt,
            stop_sequences=[anthropic.HUMAN_PROMPT],
            model="claude-2.1",  # Adjust the model version if needed
            max_tokens_to_sample=300,  # Adjust based on your requirements
        )
        
        # Display the response from the API
        st.write("### Brain Real Estate") # Just a title
        # Call the function to plot the pie chart based on the API response
        make_brain_real_estate_plot(response.completion)
        # Display the detailed text response from the API
        st.write(response.completion)
        st.text("For debugging:")
        st.text(response.completion)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")