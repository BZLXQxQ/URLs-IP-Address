import json
import re
import socket
from urllib.parse import urlparse

import requests

banner = ("""
-------------------------------------------------------------
 _   _ ___    _      ____
| | | |_ _|  / \    / ___|  ___ __ _ _ __  _ __   ___ _ __
| | | || |  / _ \   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |_| || | / ___ \   ___) | (_| (_| | | | | | | |  __/ |
 \___/|___/_/   \_\ |____/ \___\__,_|_| |_|_| |_|\___|_|   Version:Beta By_BZLX

----------------------------Start----------------------------
""")
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
def URL_IP():
    with open("urls.txt", "r") as f:
        for line in f:
            try:
                l = line.strip("\n")
                url = urlparse(l)
                hostname = url.hostname
                if re.match(
                        r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        hostname):
                    print(l + "\t" + "---->" + "\t" + hostname)
                    with open("URL_IP.txt", "a") as f:
                        f.write(hostname + "\n")
                else:
                    try:
                        getIP = socket.gethostbyname(hostname)
                        print(l + "\t" + "---->" + "\t" + getIP)
                        with open("URL_IP.txt", "a") as f:
                            f.write(getIP + "\n")
                        # print(hostname)
                    except Exception as e:
                        with open("URL_IP.txt", "a") as f:
                            f.write("\n")
            except Exception as e:
                print(e)


def IP_Address():
    with open("URL_IP.txt", "r") as f:
        for line in f:
            if line in ['\n', '\r\n']:
                with open("IP_Address.txt", "a") as f:
                    f.write("\n")
            try:
                l = line.strip("\n")
                r = requests.get(
                    "http://opendata.baidu.com/api.php?query=%s&co=&resource_id=6006&oe=utf8"
                    % l,
                    headers=header)
                results = r.text
                # print(results)
                jsresults = json.loads(results)
                # print(jsresults['data'])
                datadict = jsresults.get('data')
                for i in datadict:
                    with open('IP_Address.txt', 'a') as f:
                        f.write(i['location'] + '\n')
                        print(l +"\t" + "---->" + "\t" + i['location'])
            except Exception as e:
                print(e)


if __name__ == '__main__':
    print(banner)
    URL_IP()
    IP_Address()
    print("-----------------------------END-----------------------------")