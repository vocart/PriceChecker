import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.ceneo.pl/97698185#'
expected_price = 4000
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0)\
 Gecko/20100101 Firefox/82.0'}


def pricechecker():
    
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    current_price = int(soup.find_all(class_="value")[0].get_text())

    if current_price > expected_price:
        print('Sending mail.')
        log_and_send_mail()
    else:
        print('It\'s still too expensive.')


def log_and_send_mail():
    get_pass()
    get_mail_address()
    login()
    

def get_pass():
    password_file = open('password_PC.txt')
    text_pass = password_file.read()
    password_file.close()
    return text_pass


def get_mail_address():
    mail_file = open('mail_PC.txt')
    text_mail = mail_file.read()
    mail_file.close()
    return text_mail


def login():
    global server 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(get_mail_address(), get_pass())
    send_mail()


def send_mail():
    mail_message()
    server.sendmail(get_mail_address(), 'vocart@gmail.com', msg)
    print('Mail sent!')
    server.quit()


def mail_message():
    subject = 'Finally! CV35/1.2 has really good price!'
    body = 'https://www.ceneo.pl/97698185#'
    global msg
    msg = f"Subject:{subject}\n\n{body}"


pricechecker()
