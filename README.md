EmailHarvester
====
* A tool for querying the Domain Name System (DNS)
* Check the [License](https://github.com/maldevel/nsl00kup/blob/master/LICENSE)


Requirements
=====
* Python 2.x
* termcolor
* colorama
* dnspython


Download/Installation
====
* git clone https://github.com/maldevel/nsl00kup
* pip install -r requirements.txt --user


Usage
=====
```
usage: nsl00kup.py [-h] [-d DOMAIN] [-t RECORD_TYPE] [-s SERVER]

               _  ___   ___  _
              | |/ _ \ / _ \| |
     _ __  ___| | | | | | | | | ___   _ _ __
    | '_ \/ __| | | | | | | | |/ / | | | '_ \
    | | | \__ \ | |_| | |_| |   <| |_| | |_) |
    |_| |_|___/_|\___/ \___/|_|\__\__,_| .__/
                                        | |
                                        |_|

A tool for querying the Domain Name System (DNS) | @maldevel
                Version: 0.1

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Select a Host/Domain.
  -t RECORD_TYPE, --type RECORD_TYPE
                        Select a DNS record type.
  -s SERVER, --server SERVER
                        Select a DNS server. (default: 8.8.8.8)
```


Examples
=====
**MX records**
* ./nsl00kup.py -d example.com -t MX

**SOA**
* ./nsl00kup.py -d example.com -t SOA -s 8.8.4.4
