import os
import requests
import smtplib
from celery import shared_task


@shared_task
def check_server_status():
    
    urls = ['https://rssbeta.mysita.com/?nocache=1',
            'https://tatavms.mysita.com/']

    for url in urls:
        try:
            headers = {                                                                                                                
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'                                                                                                         
            }                                                                                                                          
            page = requests.get(url=url, headers=headers, verify=False)                                                                    
            if page.status_code==200:                                                                         
                send_email_using_python(url)
        except:
            send_email_using_python(url) 

    return "Completed"                                                                                                


def send_email_using_python(website):
    # server = smtplib.SMTP(os.environ.get('SMTP_HOST'), os.environ.get('SMTP_PORT'))
    server = smtplib.SMTP("smtp.zeptomail.com", 587)
    server.starttls()
    server.login("watcher@mysita.com", "wSsVR60l8hfyD/p7lDyrL+5ukFxVBl6kEU5931L3viP1G/3L/cc9n0KbBAPyGflKFzM4QDYWoO4hm0pR0mcMi9p/nl8HCSiF9mqRe1U4J3x17qnvhDzNW2pekhOAKIgBwwhumGliFsgr+g==")
    message = """Subject: Urgent Email From Python Script

    \n\nThis website is down - {}\n\nPlease Check.
    """.format(website)
    server.sendmail("watcher@mysita.com", ["shubham@mysita.com"], message)
    server.quit()
    return True

