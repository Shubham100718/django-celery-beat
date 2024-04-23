import requests

def get_server_status(url):
    headers = {                                                                                                                
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'                                                                                                         
    }                                                                                                                          
    page = requests.get(url, headers=headers, verify=False)                                                                    
    if page.status_code==404:                                                                         
        return False                                                                                                            
    else:                                                                                                                      
        return True

