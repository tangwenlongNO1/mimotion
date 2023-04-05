import os
import requests

# 获取当前最新版本的 Clash For Windows 下载链接和更新日志
response = requests.get("https://api.github.com/repos/Fndroid/clash_for_windows_pkg/releases/latest")
data = response.json()
latest_version = data['tag_name']
latest_download_url = data['assets'][0]['browser_download_url']
latest_changelog = data['body']

# 推送更新通知到 Telegram
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
message_text = f"Clash For Windows 更新至 {latest_version}nn{latest_changelog}"
params = {
    "chat_id":telegram_chat_id,
    "text":message_text
}
response = requests.post(telegram_api_url, data=params)
