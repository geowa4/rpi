# Raspberry Pi 3 Configuration

As soon as I heard about the Raspberry Pi 3, I knew I wanted one.
The onboard Bluetooth and WiFi, more powerful processor, and maturity of the maker culture around the Pi tipped me over the edge.
Once I got it in hand, I had to lay a good foundation on which I could build my little projects.
As someone who works on server automation, I need to do a little more laying that foundation than most would consider necessary.
I also need to have Docker installed.
With Docker, I get a simple way to experiment and blow everything away if things go badly.

This repository assumes the use of OS X, but converting should be easy.

## Booting the Pi

Before I could do anything, I needed to get an SD card with Raspbian Lite on it.
I took a new 16GB card and formatted it to FAT32.
To do this, I used SDFormatter (`brew cask install sdformatter`) to overwrite the whole thing.
Most of the time, I would choose a command line option, but this is just too easy.
Once the card was formatted, I ran `./flash https://downloads.raspberrypi.org/raspbian_lite_latest`.
With everything ready to go, I plugged everything in and booted it up.

The default hostname is `raspberrypi` so after a brief wait, it's ready to accept SSH connections.
The user is `pi` and the password is `raspberry`.

```
ssh pi@raspberrypi.local
```

This worked for SSH, but not with my automation tool of choice, Ansible.
To get the real IP address, I could probably log in to my router, but I chose to use the more general solution, `nmap`.

```
nmap -p 22 192.168.0.0/24
```

## Laying the Foundation

To install all the tools I want and configure them, I always choose Ansible for its operational simplicity.
For the Pi, I had to break down the playbooks into two runs.
The first playbook ensures the default user has the right SSH key, kernal modules, and WiFi configuration.
Next, I needed to SSH in to manually run `raspi-config` to resize the filesystem and set the locale.
I might investigate removing this step in the future, but having to run this terminal UI isn't that big of a deal since I only have one of these things.
Finally, I can install all the goodies I want, including Docker.

```
ansible-playbook --ask-pass playbooks/new_server.yml
ssh pi@raspberrypi.local
sudo raspi-config
sudo shutdown -r
ansible-playbook playbooks/site.yml
```

## Credits

Much of my inspiration and the `flash` script came from the [Hypriot blog](http://blog.hypriot.com/post/run-docker-rpi3-with-wifi/).
I couldn't have gotten to this state as easily without their effort.
