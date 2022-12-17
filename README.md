
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
[+] Discovered > http://www.company.com
[+] Discovered > http://mail.company.com
[+] Discovered > http://autodiscover.company.com
[+] Discovered > http://dev.company.com
                    ....
[+] Discovered > http://support.company.com
[+] Discovered > http://c2.company.com
[+] Discovered > http://apt.company.com
[+] Discovered > http://c3.company.com
```
## Note
You have to install the python package Request using `pip install requests`
