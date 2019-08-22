import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    message = f"< h3 > New feedback Submission </h3> <ul><li> Customer: {customer} </li ><li > Dealer: {dealer} < /li > <li > Rating: {rating} < /li > <li > Comments: {coments} < /li ></ul>"

    sender_email = ''
    receiver_email = ''
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lamborghini Feedback'
    msg['From]'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
