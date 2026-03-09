#!/bin/bash

# Define the script to run
MAIN_SCRIPT="godlawbot.py"

echo "------------------------------------------------"
echo "[*] Launching Godlawbot..."
echo "------------------------------------------------"

# Run the Python script with any passed arguments
python3 $MAIN_SCRIPT "$@"

# Check if the bot exited with an error
if [ $? -ne 0 ]; then
    echo "[!] Godlawbot encountered an error during execution."
    exit 1
fi

# 6. Clean Exit
echo "[*] Shutting down and deactivating environment..."
deactivate


Run +X Godlawbot.sh