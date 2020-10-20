#!/usr/bin/env bash

deactivate							# Deactivates VirtualEnv
echo "Virtual Environment Deactivated"

pkill -x Safari
#pkill -x Google\ Chrome
osascript -e 'quit app "Google Chrome"'
osascript -e 'quit app "Visual Studio Code"'


cd /Users/ben/LocalDocuments/Coding/Code/RadiantPromises	# Move Directory
echo "Changed Directory"

echo "Shell Complete"