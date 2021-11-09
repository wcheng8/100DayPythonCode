import smtplib

my_email = 'medemo760@gmail.com'
to_addrs = 'mdemo6659@gmail.com'
password = 'AAAaaa111pass'
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_addrs,
        msg='Subject:Hello\n\n This is the body of the Hi email'
    )
