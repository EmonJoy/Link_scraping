import requests
import bs4
import time
import pyfiglet
from colorama import Fore, Back, Style

#______________________________________________POWERED BY TEAM TIGER FORCE_________________________________
#Coder - MR.Morningstar
banner = pyfiglet.figlet_format("Link Scrapping", font = "digital")
print(banner)
print(Fore.YELLOW+"__Powered by TTF___\nscrap-V1")
print(Fore.RED + Style.DIM + "___Coded by: MR. Morningstar___\n ")

url = input(Fore.LIGHTMAGENTA_EX+ Style.BRIGHT+ "Enter url ==> ")
get_html = requests.get(url).text

soup = bs4.BeautifulSoup(get_html, "html.parser")
anchor = soup.find_all("a")

print("++++++ Collecting Information+++++++")
time.sleep(3)
for link in anchor:
    links = link.get("href")
    if links != "#":
        main_url = (url + links)
        time.sleep(1)
        with open("lists.txt", 'a') as f:
            f.write(main_url + "\n")
        print(main_url)
