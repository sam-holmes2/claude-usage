# claude-usage

xbar plugin showing Claude.ai 5-hour and 7-day usage in the macOS menu bar.

## Setup

1. Install xbar: https://xbarapp.com
2. Open xbar, go to Plugin Browser or open the plugins folder directly
3. Symlink or copy `claude_usage.5m.py` into your xbar plugins folder:
   ```
   ln -s "$(pwd)/claude_usage.5m.py" ~/Library/Application\ Support/xbar/plugins/claude_usage.5m.py
   ```
4. Make it executable:
   ```
   chmod +x claude_usage.5m.py
   ```
5. Edit `config.json` and paste your `sessionKey` cookie value (from Firefox DevTools on claude.ai)
6. Refresh xbar

## Updating the session key

If the plugin shows a red warning (session expired):
1. Open Firefox, go to claude.ai
2. DevTools (F12) > Storage > Cookies > claude.ai
3. Copy the value of `sessionKey`
4. Paste into `config.json`

The session key typically lasts months. You should rarely need to do this.

## What it shows

`⚡ 20% · 17%` in the menu bar (5-hour % · 7-day %)

Colour: green below 50%, orange above 50%, red above 80% (based on 5-hour window).

Dropdown shows a usage bar for each limit plus time until reset.

Refreshes every 5 minutes (the `.5m.` in the filename controls this).
