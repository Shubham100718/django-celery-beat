import requests
import smtplib
from celery import shared_task


@shared_task
def check_server_status(id):

    urls = ['https://rssbeta.mysita.com/?nocache=1',
            'https://tatavms.mysita.com/']

    for url in urls:
        headers = {                                                                                                                
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'                                                                                                         
        }                                                                                                                          
        page = requests.get(url=url, headers=headers, verify=False)                                                                    
        if page.status_code==404:                                                                         
            send_email_using_python(url)                                                                                                      


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

