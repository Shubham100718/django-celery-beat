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
            if page.status_code==404:                                                                         
                send_email_using_python(url)
        except:
            send_email_using_python(url) 

    return "Completed"                                                                                                


def send_email_using_python(website):
    server = smtplib.SMTP(os.environ.get('SMTP_HOST'), os.environ.get('SMTP_PORT'))
    server.starttls()
    server.login(os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASSWORD'))
    message = """Subject: Urgent Email From Python Script

    \n\nThis website is down - {}\n\nPlease Check.
    """.format(website)
    server.sendmail(os.environ.get('SMTP_USER'), [os.environ.get('SMTP_RECEIVER')], message)
    server.quit()
    return True

