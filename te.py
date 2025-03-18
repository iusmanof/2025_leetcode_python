import requests
from bs4 import BeautifulSoup

def check_ip_abuse(ip_address):
    url = f"https://www.abuseipdb.com/check/{ip_address}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Ошибка доступа к AbuseIPDB: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ищем рейтинг злоупотреблений (Abuse Confidence Score)
    score = soup.find("div", class_="progress-bar bg-danger")
    
    if score:
        return f"IP: {ip_address}, Abuse Score: {score.text.strip()}"
    else:
        return f"IP: {ip_address}, информация не найдена."

# Пример использования
ip = "8.8.8.8"
print(check_ip_abuse(ip))
