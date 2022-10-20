#!/bin/bash

sleep 5
systemctl stop discord-bot
sleep 5
echo 'Updating...'
git pull origin master
echo 'Finished. Starting bot...'
systemctl start discord-bot