# Sample Discord Bot with self update

## Prerequisites

- Python 3.8 or higher
- Git
- (optional) systemd or equivalent, restarting the bot might be a bit messy otherwise

## Installation

- Just clone the repository to wherever you like

### (optional) Setting up systemd user service

Systemd only allows system wide services out of the box. Those require root access though.
If you don't wanna run the bot on an account with root access, here's what you can do:

On an account with root access run:

```
loginctl enable-linger <username>
export XDG_RUNTIME_DIR=/run/user/$(id -u)
```

Reboot your system and log in to the non-root account.

Afterwards you have to check two environment variables:
```
echo $XDB_RUNTIME_DIR               // should return something like /run/user/1001
echo $DBUS_SESSION_BUS_ADDRESS      // should return something like /run/user/1001/bus
```

Now you can create user services under /home/\<username\>/.config/systemd/user.
The bot service should look something like this:
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

To control the service you then can do:
```
systemctl --user [start/stop/restart] <service name>
```

To have the service start on boot do:
```
systemctl --user enable <service name>
```