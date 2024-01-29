import streamlit as st
import pandas as pd

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

