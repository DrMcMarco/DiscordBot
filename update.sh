#!/bin/bash

sleep 5
pkill -f 'bot.py'
echo 'Updating...'
git pull origin master
echo 'Finished. Starting bot...'
python3.10 bot.py