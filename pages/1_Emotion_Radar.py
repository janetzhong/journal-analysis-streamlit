import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests

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

def plot_emotion_radar(scores, labels):
    """Plot the emotion radar chart based on classification scores."""
    scores = np.array(scores)
    scores = np.concatenate((scores, [scores[0]]))  # Close the radar chart
    labels = np.array(labels)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]  # Close the radar chart

    fig, ax = plt.subplots(figsize=(3, 3), subplot_kw=dict(polar=True))
    ax.fill(angles, scores, color='magenta', alpha=0.6)
    ax.plot(angles, scores, color='magenta', marker='o')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='navy', size=8)
    ax.set_yticks([])
    plt.title('Emotion Radar', size=14, color='navy', y=1.1)
    return fig

def main():
    """Run the main Streamlit app."""
    st.title('Journal Emotion Radar')

    with st.expander("Example journal entry"):
        st.write("""
    
Today has been a whirlwind of emotions. This morning, I woke up to a stunning sunrise that filled my heart with sheer delight. The vibrant colors painted across the sky were a reminder of the beauty that surrounds us every day, and it set a positive tone for the hours ahead. I was very happy!

However, as the day unfolded, a heavy cloud of sadness descended. It's the anniversary of a significant loss in my life, a day that always brings a profound sense of longing and grief. Memories of happier times mingled with the weight of absence, leaving me with a profound sense of melancholy. I was very sad.

Life has this unique way of weaving joy and sorrow into the tapestry of our days, and today was a poignant reminder of this delicate balance. Amidst the highs and lows, I'm learning to appreciate the full spectrum of emotions that define our human experience.
        """)
    # Main area for user text input
    user_input = st.text_area("Enter your journal entry or text here:", height=150)

    # Button to classify text
    submit = st.button('Submit')

    if submit and user_input:
        # Classify the emotion without needing to ask for an API key
        try:
            results = classify_emotion(user_input)
            
            # Extract labels and scores for plotting
            labels = [result['label'] for result in results[0]]
            scores = [result['score'] for result in results[0]]

            # Plot and display the radar chart
            fig = plot_emotion_radar(scores, labels)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error in emotion classification: {e}")

if __name__ == "__main__":
    main()