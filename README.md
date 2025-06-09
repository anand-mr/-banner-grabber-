Banner Grabber

A simple Python tool that connects to a host/port and displays the service banner.  
For learning, penetration-testing on **machines you own or have explicit permission to scan**.

## Features
- Works with any TCP port (defaults: 21, 22, 25, 80, 443, 8080)
- Five-second timeout so it doesn’t hang
- Clean error handling

## Usage
```bash
python banner_grabber.py --ip 192.168.1.100 --ports 21,22,80
