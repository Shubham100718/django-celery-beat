import smtplib

def send_email_using_python(website):
    s = smtplib.SMTP('smtp.zeptomail.com', 587)
    s.starttls()
    s.login("watcher@mysita.com", "wSsVR60l8hfyD/p7lDyrL+5ukFxVBl6kEU5931L3viP1G/3L/cc9n0KbBAPyGflKFzM4QDYWoO4hm0pR0mcMi9p/nl8HCSiF9mqRe1U4J3x17qnvhDzNW2pekhOAKIgBwwhumGliFsgr+g==")
    message = """Subject: Urgent Email From Python Script

    \n\nThis website is down - {}\n\nPlease Check.
    """.format(website)
    s.sendmail("watcher@mysita.com", ["rakesh.verma@sitanet.in","jaeeme.khan@sitanet.in","shubham@mysita.com"], message)
    s.quit()
    return True

