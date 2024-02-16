import requests

def fetch_data_from_local_server():
    try:
        response = requests.post("http://localhost:8501/analyze", json={"text": user_input})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error fetching data from local server"}
    except requests.RequestException as e:
        return {"error": f"Error: {e}"}
