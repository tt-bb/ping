import requests


def get_status(url):
    response = requests.get(url, timeout=2.5)
    return response.ok


if __name__ == "__main__":
    website = input("Enter the URL (http(s)://...) ")
    online = get_status(website)

    if online:
        print(f"🟢 : {website} is running")
    else:
        print(f"🔴 : {website} is down")
