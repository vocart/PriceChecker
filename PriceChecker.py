import requests
from bs4 import BeautifulSoup
import smtplib

# here is the watched URL
URL = 'https://www.ceneo.pl/97698185#'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}


# it checks the price of an object from the address, then shows three first prices, if the first one
# is lower than expected it sends email
def price_checker():
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price1 = int(soup.find_all(class_="value")[0].get_text())
    price2 = soup.find_all(class_="value")[1].get_text()
    price3 = soup.find_all(class_="value")[2].get_text()

    print(int(price1), int(price2), int(price3))

    if price1 < 4000:
        print('sending')
        send_mail()


# it gets password from a txt file
def get_pass():
    password_file = open('password_PC.txt')
    text = password_file.read()
    password_file.close()
    return text


# logs on an account and sends an email with a certain message to another account
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vocart33@gmail.com', get_pass())

    subject = 'Finally! CV35/1.2 has really good price!'
    body = 'https://www.ceneo.pl/97698185#'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('vocart33@gmail.com', 'vocart@gmail.com', msg)

    print('Mail sent!')

    server.quit()


price_checker()
