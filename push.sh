#!/bin/bash
cd /home/noah/UWorld-words-corrector

./generate_html.py

git add words.html
git commit -m "Auto update $(date)"
git push origin main
