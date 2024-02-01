# Journal analysis demos

Demonstrations for CS224G sprints on Streamlit

The demos may be viewed at the following URL: [https://mindstorm-journal-analysis.streamlit.app/](https://mindstorm-journal-analysis.streamlit.app/)

## Streamlit App Guide

This guide will help you set up and run the app on your local machine.

Installation
------------

1.  **Clone the Repository**  
    Start by cloning the app repository to your local machine:
    
        git clone https://github.com/janetzhong/journal-analysis-streamlit
        cd your-streamlit-app-repo
    
2.  **Create a Virtual Environment (Optional but Recommended)**  
    It's a good practice to create a virtual environment for Python projects. Use the following command to create one:
    
        python -m venv venv
    
    Activate the virtual environment:
    *   On Windows:
        
            venv\Scripts\activate
        
    *   On macOS and Linux:
        
            source venv/bin/activate
        
3.  **Install Dependencies**  
    Install the required Python packages using `pip`:
    
        pip install -r requirements.txt
    

Configuration
-------------

To use certain features of the app, you may need to provide an API key or other sensitive information. This is handled securely through the `secrets.toml` file located in the `.streamlit` folder.

1.  **Create `secrets.toml`**  
    Inside the root directory of your project, navigate to the `.streamlit` folder. If this folder does not exist, create it:
    
        mkdir -p .streamlit
    
    Within this folder, create a file named `secrets.toml`.
2.  **Add Your API Key**  
    Depending on the services your app interacts with, you might need to add specific API keys or configuration settings. Open `secrets.toml` in a text editor and add your configurations. For example, if using an API from Hugging Face, you might add:
    
        [HuggingFace]
        api_key = "YOUR_HUGGING_FACE_API_KEY_HERE"
    
The structure within `secrets.toml` allows for multiple services to be configured securely and separately.

**Note on Using `secrets.toml`**  
Streamlit automatically recognizes and securely uses the information stored in `secrets.toml` when running your app. This method ensures sensitive information is not hardcoded into your app's source code, providing a secure way to handle API keys and other confidential data.

Ensure each service or API key is correctly defined in the `secrets.toml` file as shown above, adhering to the required format for each specific service your app integrates with.

Running the App
---------------

With the installation and configuration done, you're ready to run the app.

1.  **Launch Streamlit**  
    Run the following command in your terminal:
    
        streamlit run Home.py
    
2.  **Access the App**  
    Streamlit will start the app and open it in your default web browser. If it doesn't, you can manually navigate to the URL provided in the terminal output (usually `http://localhost:8501`).

Troubleshooting
---------------

If you encounter any issues, make sure all steps were followed correctly. Check that:

*   Your virtual environment is activated.
*   All dependencies are installed.
*   The `secrets.toml` file is correctly set up with your API key.

For more help, consider checking the [Streamlit Documentation](https://docs.streamlit.io).
