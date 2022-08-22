
# Sub-domain-crawler

A python script to discover all sub domains of any domain

## Steps

1. In this simple script you will type the domain name such as `target.com` 
2. This script will use a file `words_list.txt` that contains a list of words to create multiple sub domains
3. Each time a new domain is created it will be tested for `response 200`
4. In the end it will create a list of all discovered sub-domains
5. To run the script use command ``python sub-domain-crawler.py``


## output
```
[+] Discovered > http://www.cytomate.net
[+] Discovered > http://mail.cytomate.net
[+] Discovered > http://autodiscover.cytomate.net
[+] Discovered > http://dev.cytomate.net
                    ....
[+] Discovered > http://support.cytomate.net
[+] Discovered > http://c2.cytomate.net
[+] Discovered > http://apt.cytomate.net
[+] Discovered > http://c3.cytomate.net
```
