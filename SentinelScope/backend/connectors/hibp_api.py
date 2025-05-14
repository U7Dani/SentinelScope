import requests

def check_email(email: str):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": "YOUR_HIBP_API_KEY",
        "user-agent": "SentinelScope OSINT"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return []
    else:
        return {"error": response.status_code}
