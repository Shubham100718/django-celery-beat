import requests
import smtplib
from celery import shared_task


@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id


def get_server_status(url):
    headers = {                                                                                                                
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'                                                                                                         
    }                                                                                                                          
    page = requests.get(url, headers=headers, verify=False)                                                                    
    if page.status_code==404:                                                                         
        return False                                                                                                            
    else:                                                                                                                      
        return True


def send_email_using_python(website):
    s = smtplib.SMTP('smtp.zeptomail.com', 587)
    s.starttls()
    s.login("watcher@mysita.com", "wSsVR60l8hfyD/p7lDyrL+5ukFxVBl6kEU5931L3viP1G/3L/cc9n0KbBAPyGflKFzM4QDYWoO4hm0pR0mcMi9p/nl8HCSiF9mqRe1U4J3x17qnvhDzNW2pekhOAKIgBwwhumGliFsgr+g==")
    message = """Subject: Urgent Email From Python Script

    \n\nThis website is down - {}\n\nPlease Check.
    """.format(website)
    s.sendmail("watcher@mysita.com", ["shubham@mysita.com"], message)
    s.quit()
    return True


# def task():
#     urls = ['https://rssbeta.mysita.com/?nocache=1',
#             'https://tatavms.mysita.com/']

#     for url in urls:
#         website_status = get_server_status(url)
#         print(url, website_status)
#         if website_status == False:
#             send_email_using_python(url)

# schedule.every(1800).seconds.do(task)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

