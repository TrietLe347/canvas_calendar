

from config import CANVAS_API_TOKEN, CANVAS_BASE_URL
import requests

HEADERS = {
    "Authorization": f"Bearer {CANVAS_API_TOKEN}"
}

def get_me():
    url = f"{CANVAS_BASE_URL}/api/v1/users/self/profile"
    response = requests.get(url,headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_future_assign():
    url = f"{CANVAS_BASE_URL}/api/v1/users/self/upcoming_events"
    response = requests.get(url,headers=HEADERS)
    response.raise_for_status()
    

    events = response.json()
    

    future_assignments = [e for e in events
                          if e.get("type") == "assignment"
                          ]
    
    return future_assignments


