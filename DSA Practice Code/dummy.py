import requests

url = "https://2chat.co/_next/data/HYjl-GuAC1tLV6gKywkpX/en/tools/whatsapp-checker.json"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises an exception for 4xx/5xx responses

    data = response.json()

    print("Status Code:", response.status_code)
    print("Overall Status:", data["status"]["description"])
    print("Indicator:", data["status"]["indicator"])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)