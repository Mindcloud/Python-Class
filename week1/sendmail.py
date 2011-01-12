import smtplib

fromaddr = "jeff@neckpuncher.com"
toaddrs  = ("jeff.boschee@gmail.com","jeff@mindcloud.com")
subj = prompt("Subject: This is a mail merge app")
print "Enter message, end with Blank line or Cntrl-D"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n"
       % (fromaddr, ", ".join(toaddrs), subj))
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

