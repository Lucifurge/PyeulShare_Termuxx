import requests
import time
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ✅ Your approved Facebook Developer App Token
APP_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"

banner = Panel(
    "[bold yellow]PYEUL BOT SHARE[/bold yellow]",
    width=60,
    title="[bold cyan]APP TOKEN MODE[/bold cyan]",
    border_style="blue",
    expand=False
)
console.print(banner)

def share_post(share_url, share_count):
    url = "https://graph.facebook.com/me/feed"
    headers = {"User-Agent": "Mozilla/5.0"}
    data = {
        "link": share_url,
        "privacy": '{"value":"SELF"}',
        "no_story": "true",
        "published": "false",
        "access_token": APP_TOKEN
    }
    for i in range(1, share_count + 1):
        try:
            response = requests.post(url, json=data, headers=headers)
            response_data = response.json()
            post_id = response_data.get("id", None)
            if post_id:
                console.print(f"[bold cyan]({i}/{share_count})[/bold cyan] [green]Shared successfully!")
            else:
                console.print(f"[red]({i}/{share_count}) Failed: {response_data}")
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Error: {e}")
        time.sleep(0.5)

def bot_share():
    share_url = input("🔗 Enter the post link to share: ").strip()
    share_count = int(input("🔁 How many times to share?: ").strip())
    share_post(share_url, share_count)

def main_menu():
    while True:
        console.print(Panel("""
[1] Share Post (No Login)
[2] Exit
""", width=60, style="bold bright_white"))
        choice = input("Select an option: ").strip()
        if choice == "1":
            bot_share()
        elif choice == "2":
            console.print("[red]Exiting... Goodbye!")
            break
        else:
            console.print("[red]Invalid choice!")

if __name__ == '__main__':
    main_menu()
