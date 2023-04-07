import os
import requests
from dotenv import load_dotenv
load_dotenv()

# 获取当前最新版本的 Clash For Windows 下载链接和更新日志
response = requests.get("https://api.github.com/repos/Fndroid/clash_for_windows_pkg/releases/latest")
print(response.status_code)
data = response.json()
latest_version = data['tag_name']
latest_download_url = data['assets'][0]['browser_download_url']
latest_changelog = data['body']

# 推送更新通知到 Telegram
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
current_version = os.getenv('version')
telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
if latest_version != current_version:

    message_text = f"🎉*Clash For Windows 更新至 {latest_version}*\n{latest_changelog}\n[下载链接](https://github.com/Fndroid/clash_for_windows_pkg/releases/latest)"
    params = {
        "chat_id":telegram_chat_id,
        "text":message_text,
        "parse_mode":'Markdown',
        "disable_web_page_preview":True

    }
    response = requests.post(telegram_api_url, data=params)
    print(response.status_code)
    set_key('.env', 'version', latest_version)

