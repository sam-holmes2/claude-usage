#!/usr/bin/env python3
# <xbar.title>Claude Usage</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Sam Holmes</xbar.author>
# <xbar.desc>Shows Claude.ai 5-hour and 7-day usage from menu bar</xbar.desc>
# <xbar.refreshOnOpen>true</xbar.refreshOnOpen>

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

CONFIG_PATH = Path.home() / ".claude-usage" / "config.json"
ORG_ID = "04eb98a0-b66a-4da0-b550-3004e59753d0"
URL = f"https://claude.ai/api/organizations/{ORG_ID}/usage"

def load_config():
    if not CONFIG_PATH.exists():
        print("Claude | color=red")
        print("---")
        print("config.json not found")
        print(f"Create it at: {CONFIG_PATH}")
        exit()
    with open(CONFIG_PATH) as f:
        return json.load(f)

def format_reset(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    diff = dt - now
    hours = int(diff.total_seconds() // 3600)
    mins = int((diff.total_seconds() % 3600) // 60)
    if hours >= 24:
        days = hours // 24
        return f"{days}d"
    elif hours > 0:
        return f"{hours}h {mins}m"
    else:
        return f"{mins}m"

def usage_bar(pct, width=10):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)

def main():
    config = load_config()
    session_key = config.get("sessionKey", "")

    headers = {
        "Cookie": f"sessionKey={session_key}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:151.0) Gecko/20100101 Firefox/151.0",
        "anthropic-client-platform": "web_claude_ai",
        "content-type": "application/json",
    }

    try:
        req = urllib.request.Request(URL, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            print("Claude ⚠ | color=red")
            print("---")
            print("Session expired. Update sessionKey in config.json | color=red")
        else:
            print(f"Claude ⚠ | color=orange")
            print("---")
            print(f"HTTP error {e.code}")
        return
    except Exception as e:
        print("Claude ⚠ | color=orange")
        print("---")
        print(f"Error: {e}")
        return

    five = data.get("five_hour", {})
    seven = data.get("seven_day", {})

    five_pct = five.get("utilization") or 0
    seven_pct = seven.get("utilization") or 0
    five_reset = format_reset(five["resets_at"]) if five.get("resets_at") else "?"
    seven_reset = format_reset(seven["resets_at"]) if seven.get("resets_at") else "?"

    # Green by default, orange/red when high
    if five_pct >= 80:
        color = "color=red"
    elif five_pct >= 50:
        color = "color=orange"
    else:
        color = "color=#00FF41"

    # Menu bar line
    print(f"⚡ {five_pct:.0f}% ({five_reset}) · {seven_pct:.0f}% ({seven_reset}) | {color}")
    print("---")
    print(f"5-hour:  {usage_bar(five_pct)} {five_pct:.0f}%  (resets in {five_reset})")
    print(f"7-day:   {usage_bar(seven_pct)} {seven_pct:.0f}%  (resets in {seven_reset})")
    print("---")
    print("Open Claude Usage Page | href=https://claude.ai/settings/billing")
    print("Refresh | refresh=true")

main()
