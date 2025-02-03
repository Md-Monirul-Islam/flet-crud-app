import requests

BASE_URL = "http://127.0.0.1:8000/api/items/"

def get_items():
    """Fetch all items from the API."""
    response = requests.get(BASE_URL)
    return response.json()

def create_item(data):
    """Create a new item."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(BASE_URL, json=data, headers=headers)
    return response.json()

def update_item(item_id, data):
    """Update an existing item."""
    headers = {"Content-Type": "application/json"}
    response = requests.put(f"{BASE_URL}{item_id}/", json=data, headers=headers)
    return response.json()

def delete_item(item_id):
    """Delete an item from the backend."""
    headers = {"Content-Type": "application/json"}
    response = requests.delete(f"{BASE_URL}{item_id}/", headers=headers)
    
    if response.status_code == 204:
        return True
    else:
        print(f"Failed to delete item. Status code: {response.status_code}, Response: {response.text}")
        return False
