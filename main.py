import time
import schedule
from check_server_status import get_server_status
from send_email_using_python import send_email_using_python


def task():
    urls = ['https://rssbeta.mysita.com/?nocache=1',
            'https://tatavms.mysita.com/']

    for url in urls:
        website_status = get_server_status(url)
        print(url, website_status)
        if website_status == False:
            send_email_using_python(url)

schedule.every(1800).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)

