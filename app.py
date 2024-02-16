import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

def main():
    st.title("Hate and offensive text detection")

    # User input
    user_input = st.text_area("Enter text:", "")

    if st.button("Analyze"):
        if user_input:
            # Perform sentiment analysis
            result = classifier(user_input)

            # Display the result
            st.subheader("Result:")
            st.write(f"Text: {result[0]['label']}")
            st.write(f"Confidence: {result[0]['score']:.4f}")

if __name__ == "__main__":
    main()
