# Sample Discord Bot with self update

## Prerequisites

- Python 3.8 or higher
- Git
- (optional) systemd or equivalent, restarting the bot might be a bit messy otherwise

## Installation

- Just clone the repository to wherever you like
- If you run systemd, create a service. For example:
```
# discord-bot.service

[Unit]
Description=Test Discord Bot
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/home/marco/Projects/DiscordBot
ExecStart=/usr/bin/python3.10 /home/marco/Projects/DiscordBot/bot.py

[Install]
WantedBy=multi-user.target
```
- If you don't run systemd, you have to edit the update script to something like
```
pkill -f 'bot.py'
git pull origin master
python3 bot.py
```

### (optional) Setting up systemd user service

Systemd only allows system wide services out of the box. Those require root access though.
If you don't wanna run the bot on an account with root access, here's what you can do:

On an account with root access run:

```
loginctl enable-linger <username>           // This will enable a user specific service manager
```
More on that [here](https://www.freedesktop.org/software/systemd/man/loginctl.html#enable-linger%20USER%E2%80%A6).

Now reboot your system and log in to the non-root account.

You have to check two environment variables:
```
echo $XDB_RUNTIME_DIR               // should return something like /run/user/1001
echo $DBUS_SESSION_BUS_ADDRESS      // should return something like /run/user/1001/bus
```

Now you can create user services under /home/\<username\>/.config/systemd/user.

To control the service you then can do:
```
systemctl --user [start/stop/restart] <service name>
```

To have the service start on boot do:
```
systemctl --user enable <service name>
```