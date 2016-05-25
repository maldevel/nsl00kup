"""
    This file is part of nsl00kup
    Copyright (C) 2016 @maldevel
    
    nsl00kup - DNS lookups

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = "maldevel"
__copyright__ = "Copyright (c) 2016 @maldevel"
__credits__ = ["maldevel"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "maldevel"



#####################
import argparse
import sys

from termcolor import colored
from dns.resolver import dns
from argparse import RawTextHelpFormatter
from sys import platform as _platform
#####################

 
################################
if _platform == 'win32':
    import colorama
    colorama.init()


def yellow(text):
    return colored(text, 'yellow', attrs=['bold'])

def green(text):
    return colored(text, 'green', attrs=['bold'])

def red(text):
    return colored(text, 'red', attrs=['bold'])

def cyan(text):
    return colored(text, 'cyan', attrs=['bold'])
###################################################################


###################################################################
def query(domain, qtype, server):
    try:            
        ADDITIONAL_RDCLASS = 65535
        request = dns.message.make_query(domain, dns.rdatatype._by_text[qtype.upper()])
        request.flags |= dns.flags.AD | dns.flags.RD | dns.flags.RA
        request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
                       dns.rdatatype.OPT, create=True, force_unique=True)       
        response = dns.query.udp(request, server)
        
        print green('[+] Server: ')
        print cyan('{}'.format(server))
            
        print
            
        print green('[+] Question: ')
        for question in response.question:
            print cyan('{}'.format(question))
        
        print
        
        print green('[+] Answer: ')
        for answer in response.answer:
            print cyan('{}'.format(answer))
            
        print
        
        print green('[+] Authority: ')
        for authority in response.authority:
            print cyan('{}'.format(authority))
        
        print
        
        print green('[+] Additional: ')
        for additional in response.additional:
            print cyan('{}'.format(additional))
        
        print
        
    except Exception,e:
        print(red('[-] Error: {}'.format(e)))


###################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""
               _  ___   ___  _                
              | |/ _ \ / _ \| |               
     _ __  ___| | | | | | | | | ___   _ _ __  
    | '_ \/ __| | | | | | | | |/ / | | | '_ \ 
    | | | \__ \ | |_| | |_| |   <| |_| | |_) |
    |_| |_|___/_|\___/ \___/|_|\__\__,_| .__/ 
                                        | |    
                                        |_|    
                                        
A tool for querying the Domain Name System (DNS) | @maldevel
                {}: {}
""".format(red('Version'), yellow(__version__)),                                 
                                     formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('-d', '--domain', action="store", metavar='DOMAIN', dest='domain', 
                        default=None, type=str, help="Select a Host/Domain.")
    
    parser.add_argument('-t', '--type', action="store", metavar='RECORD_TYPE', dest="qtype",
            type=str, default='A', help="Select a DNS record type.")
    
    parser.add_argument('-s', '--server', action="store", metavar='SERVER', dest="server",
            type=str, default='8.8.8.8', help="Select a DNS server. (default: 8.8.8.8)")
        
    
    if len(sys.argv) is 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    
    if not args.domain:
        print(red("[-] Please specify a domain."))
        sys.exit(2)
        
        
    query(args.domain, args.qtype, args.server)
    