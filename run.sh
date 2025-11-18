#!/bin/bash

# Tor proxy settings set karna
export http_proxy="socks5h://127.0.0.1:9050"
export https_proxy="socks5h://127.0.0.1:9050"
export HTTP_PROXY="socks5h://127.0.0.1:9050"
export HTTPS_PROXY="socks5h://127.0.0.1:9050"

# User ko nayi shell mein daalna jahan proxy set ho
echo "Starting Faizan Cyber Phantom..."

# Python script ko background mein chalaayein
python3 main.py & 

# Last executed background process ka PID save karein (Tor process ka parent)
PHANTOM_PID=$!

echo "--------------------------------------------------------"
echo "Phantom is active. Any command (curl, wget) will use Tor."
echo "Use 'exit' to close the shell and stop the Phantom."
echo "--------------------------------------------------------"

# User ko nayi shell mein daalna (taaki user direct commands chala sake)
/bin/bash

# Jab user 'exit' kare, toh background process ko band kar dein
echo "[!] Shutting down Phantom..."
kill $PHANTOM_PID
