#!/usr/bin/env python3
import sqlite3
import os

DB_PATH = "/home/noah/UWorld-words-corrector/words.html"
OUTPUT_PATH = "/home/noah/UWorld-words-corrector/words.html"

HTML_HEAD = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Word List</title>
<style>
body { font-family: sans-serif; padding: 20px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #888; padding: 8px; }
th { background-color: #eee; }
</style>
</head>
<body>
<h1>Word List</h1>
<table>
<tr><th>Word</th><th>Count</th><th>Translation</th><th>Tag</th><th>Updated</th><button onclick="this. closest('tr'.remove())">削除</button></tr>
"""

HTML_FOOT = """
</table>
</body>
</html>
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT word, count, translation, tag, created_at FROM words ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()

    html = [HTML_HEAD]
    for row in rows:
        html.append("<tr>" + "".join(f"<td>{col}</td>" for col in row) + "</tr>")
    html.append(HTML_FOOT)

    with open(OUTPUT_PATH, "w") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    main()

