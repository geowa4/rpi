# Raspberry Pi 3 Configuration

Starting with a new Raspberry Pi 3, get it to a useful state.
All of the following assumes OS X since that what I happen to be using.

## Booting the Pi

Before we can do anything, we need to get an SD card with Raspbian Lite on it.
With a new 16GB card, format it to FAT32.
To do this, I used SDFormatter (`brew cask install sdformatter`) to overwrite the whole thing.
I could use the command line, but this is tool is too easy.
Once the card is formatted, run `./flash https://downloads.raspberrypi.org/raspbian_lite_latest`.
Now, you're ready to boot your Raspberry Pi.

The default hostname is `raspberrypi` so after the Pi has had enough time to boot, it's ready to accept SSH connections.
The user is `pi` and the password is `raspberry`.

```
ssh pi@raspberrypi.local
```

If you want to find the exact IP, use `nmap` on your IP range.

```
nmap -p 22 192.168.0.0/24
```

## Laying the Foundation

To install all the tools I want and configure them, I choose Ansible.
We'll have to break down the playbooks into two runs.
The first playbook ensures the default user has the right SSH key, kernal modules, and WiFi configuration.
Next, we'll need to SSH in to manually run `raspi-config` to resize the filesystem and set the locale.
Finally, we can lay a useful foundation.

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
