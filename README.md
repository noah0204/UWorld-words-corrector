#!/usr/bin/env python3
import sqlite3
import datetime
import os

DB_PATH = "/home/noah/words.db"
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
<tr><th>Word</th><th>Count</th><th>Translation</th><th>Tag</th><th>Date</th></tr>
"""

HTML_FOOT = """
</table>
</body>
</html>
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT word, count, translation, tag, created_at FROM words ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    html = [HTML_HEAD]

    for word, count, translation, tag, created_at in rows:
        html.append(f"<tr>")
        html.append(f"<td>{word}</td>")
        html.append(f"<td>{count}</td>")
        html.append(f"<td>{translation}</td>")
        html.append(f"<td>{tag}</td>")
        html.append(f"<td>{created_at}</td>")
        html.append("</tr>")

    html.append(HTML_FOOT)

    with open(OUTPUT_PATH, "w") as f:
        f.write("\n".join(html))

    print("HTML updated:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
