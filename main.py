import requests

bot_token = "6313038374:AAFJQH-bhWbUP5h1n0mPMcFCRiToJjOwMmw"

file_path = input("Введите путь к TXT файлу: ").strip()
chat_id = input("Введите chat_id: ").strip()

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
data = {
    "chat_id": chat_id,
    "text": text
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Сообщение отправлено.")
else:
    print("Ошибка отправки:", response.text)
