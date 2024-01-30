import streamlit as st
import pandas as pd
import requests

st.title("📝 Multiple Journal Entry Analysis")

st.write("This demo requires multiple entries. Upload your own, otherwise you may use this demo csv file below:")
# Assuming 'multiple_entries_demo.csv' is in the 'app' directory of your Streamlit app
# Path to the file (Update this path if your file is located in a different directory)
file_path = 'pages/multiple_entries_demo.csv'

# Button to download example demo entries 
with open(file_path, "rb") as file:
    btn = st.download_button(
            label="Download demo journal entries",
            data=file,
            file_name="multiple_entries_demo.csv",
            mime="text/csv",
            help="Click to download the journal entries as a CSV file"
        )

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"],
                                 help="The CSV file should have two columns: one with the date (YYYY-MM-DD) and another with entries.")

# Process the uploaded file, gives the dictionary in an expander
if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    entries_df = pd.read_csv(uploaded_file)
    
    # Convert the DataFrame to a dictionary
    entries_dict = {}
    for index, row in entries_df.iterrows():
        date = row['Date']
        entry = row['Entry']
        entries_dict[date] = entry
    
    # Use an expander to display the entire dictionary
    with st.expander("Click to view loaded journal entries"):
        # Display the entire dictionary
        for date, entry in entries_dict.items():
            st.text(f"Date: {date}, Entry: {entry}")
else:
    st.write("Please upload a CSV file to proceed.")


# now classify emotions of csv file
def classify_emotion(text):
    """Classify the emotion of the given text using the Hugging Face Inference API."""
    api_url = "https://api-inference.huggingface.co/models/michellejieli/emotion_text_classifier"
    
    # Directly include the API token in the headers
    api_token = "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"  # Replace with your actual API key
    headers = {"Authorization": f"Bearer {api_token}"}

    # Prepare the payload
    payload = {"inputs": text, "options": {"wait_for_model": True}, "parameters": {"return_all_scores": True}}

    # Make the request
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to classify emotion: {response.text}")


if st.button('Classify Emotions'):
    # Applying the classifier to each entry and adding the scores
    for date, entry in entries_dict.items():
        if isinstance(entry, dict):
            # If the entry is already a dictionary (with possibly previous emotion scores), extract the text
            text = entry['entry']
        else:
            text = entry  # Directly use the text for classification
        
        # Apply the classifier
        result = classify_emotion(text)
        
        # Assuming we want to keep the entire structure of the result which is a list of dictionaries for each emotion
        if isinstance(entry, dict):
            # If the entry is already a dictionary, just update the emotion_scores key
            entries_dict[date]['emotion_scores'] = result
        else:
            # Convert the entry to a dictionary and add an emotion_scores key
            entries_dict[date] = {'entry': entry, 'emotion_scores': result}
        # Use an expander to display the entire dictionary
    with st.expander("Click to view loaded journal entries with emotion classification"):
        # Display the entire dictionary
        for date, data in entries_dict.items():
            st.text(f"Date: {date}, Data: {data}")