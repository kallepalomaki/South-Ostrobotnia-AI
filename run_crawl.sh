#!/bin/bash
venv/bin/python3 crawl_pohopekka.py
venv/bin/python3 crawl_helmia.py
cat pohopekka.txt helmia.txt > ep.txt
