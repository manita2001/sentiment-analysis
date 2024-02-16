import streamlit as st
import requests  # For making HTTP requests

# Streamlit app setup
st.title("Hate and Offensive Text Detection")

# User input
user_input = st.text_area("Enter text:", "")

if st.button("Analyze"):
    if user_input:
        # Make an HTTP request to your local server
        try:
            response = requests.post("http://localhost:8501/analyze", json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                st.subheader("Result:")
                st.write(f"Text: {result['label']}")
                st.write(f"Confidence: {result['score']:.4f}")
            else:
                st.error("Error fetching data from local server")
        except requests.RequestException as e:
            st.error(f"Error: {e}")
from sentiment_analysis import analyze_sentiment
from api_requests import fetch_data_from_local_server

def main():
    st.title("Hate and Offensive Text Detection")
    user_input = st.text_area("Enter text:", "")

    if st.button("Analyze"):
        if user_input:
            result = analyze_sentiment(user_input)
            st.subheader("Result:")
            st.write(f"Text: {result['label']}")
            st.write(f"Confidence: {result['score']:.4f}")

if __name__ == "__main__":
    main()
