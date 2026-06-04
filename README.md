# claude-usage

xbar plugin showing your Claude.ai 5-hour and 7-day usage in the macOS menu bar.

![menu bar showing ⚡ 28% (3h 11m) · 18% (3d) in green](screenshot.png)

## Setup

1. Install [xbar](https://xbarapp.com)
2. Copy `claude_usage.5m.py` to your xbar plugins folder:
   ```bash
   cp claude_usage.5m.py ~/Library/Application\ Support/xbar/plugins/
   chmod +x ~/Library/Application\ Support/xbar/plugins/claude_usage.5m.py
   ```
3. Create your config file:
   ```bash
   mkdir -p ~/.claude-usage
   cp config.example.json ~/.claude-usage/config.json
   ```
4. Get your session key:
   - Open claude.ai in Firefox
   - DevTools (F12) > Storage > Cookies > claude.ai
   - Copy the value of `sessionKey`
   - Paste it into `~/.claude-usage/config.json`
5. Refresh xbar

## What it shows

`⚡ 28% (3h 11m) · 18% (3d)` in green by default, turning orange above 50% and red above 80% (based on the 5-hour window).

Click the menu bar item for a usage bar and exact reset times.

Refreshes every 5 minutes.

## Updating the session key

The session key typically lasts months. If you see a red warning, just grab a fresh one from DevTools and update `~/.claude-usage/config.json`.

## Note

This uses an undocumented internal Claude.ai endpoint. It may break if Anthropic changes their API. No data leaves your machine beyond the request to claude.ai itself.
