from bs4 import BeautifulSoup
from selenium import webdriver
import os
from urllib.request import urlopen
from urllib.parse import quote_plus
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="Type the filename. (ex. pokemon.txt)")

    args = parser.parse_args()
    filename = args.filename

    f = open(filename, encoding='utf-8')
    pokemon = []
    while True:
        line = f.readline().strip()
        if not line: break
        pokemon.append(line)
    f.close()

    k = 0
    while k < len(pokemon):
        path = os.getcwd() + '/chromedriver.exe'
        URL = 'https://www.google.co.in/search?q=' + pokemon[k] + '&source=lnms&tbm=isch'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36")

        driver = webdriver.Chrome(path, options=options)
        driver.implicitly_wait(3)
        driver.get(URL)
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}

        save_dir = os.getcwd() + '\img\\' + pokemon[k]
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir)
        size = 42
        count = 1
        for i in range(1, size):
            if i == 25:
                continue
            if i % 10 == 0:
                driver.execute_script("window.scrollBy(0,10000000)")
            # source = driver.find_element_by_class_name('rg_i')
            source = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
            img_url = source.get_attribute('src')
            try:
                with urlopen(img_url) as f:
                    with open(save_dir + '/' + pokemon[k] + '_' + str(count) + '.jpg', 'wb') as h:
                        img = f.read()
                        h.write(img)
                        count += 1
            except:
                pass
            driver.implicitly_wait(5)

        print(pokemon[k] + " is done.")
        k += 1

        driver.close()

if __name__ == "__main__":
    main()
