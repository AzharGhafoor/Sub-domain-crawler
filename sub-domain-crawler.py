import requests

discovered_subdomains = []
url = 'cytomate.net' # main domain

def url_test(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

with open("words_list.txt", "r") as words:
    for word in words:
        test_url = "http://"+word.strip()+"."+url
        
        response = url_test(test_url)
        if(response):
            print("[+] Discovered >",test_url)
            discovered_subdomains.append(test_url)
        else:
            pass
        
print(discovered_subdomains) # to see all discovered sub domains
print("Done")
