import smtplib as sm 
my_file = open("README.md","rt")
txt = my_file.read()
emails = ["mohamed.elmeziani@outlook.com","elmezianimohamed45@gmail.com", "kaferzain@gmail.com","macinessa365@gmail.com"]
#using google mail
server = sm.SMTP_SSL("smtp.gmail.com",465)
server.login("movis4dow@gmail.com","macinessa63216")
server.sendmail("movis4dow@gmail.com", emails,txt)
server.quit()
