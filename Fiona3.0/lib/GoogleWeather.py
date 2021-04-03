from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
import os

import time


#driver = webdriver.Chrome("D:\\Dokumente\\web_scraping\\chromedriver.exe")
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#driver.get("https://www.google.at/")

class GoogleWeather():

    def __init__(self, location="desselbrunn"):
        global driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--enable-javascript")
        driver = webdriver.Chrome("/usr/bin/chromedriver" ,options=chrome_options)
        #cwd = os.getcwd()
        #driver = webdriver.Firefox(executable_path=cwd + "\\Fiona2.1\\resources\\geckodriver.exe" ,options=firefox_options)
        driver.get("https://www.google.com/search?q=weather+" + location)
        time.sleep(1)

    def get_actual_weather(self):
        
        global driver
        loc = driver.find_element_by_id("wob_loc").text # Ort
        day_time = driver.find_element_by_id("wob_dts").text # Wochentag und Uhrzeit
        weather = driver.find_element_by_id("wob_dc").text # Wetter
        temp = driver.find_element_by_id("wob_tm").text + "°C" # Temperatur
        rain = driver.find_element_by_id("wob_pp").text # Niederschlag
        hm = driver.find_element_by_id("wob_hm").text # Luftfeuchtigkeit
        ws = driver.find_element_by_id("wob_ws").text # Windstärke
        wi = driver.find_element_by_id("wob_tci").get_attribute("src") # Wetter Icon
        return {"location": loc, "day_time": day_time, "weather": weather, "temp": temp,
                "rain": rain, "humidity": hm, "wind_strength": ws, "weather_icon": wi}

    def get_weather_prediction(self):
        
        global driver
        # temp, hum and windsgth of next two weeks 
        element = driver.find_elements_by_id("wob_gsvg")[0]
        all_children_by_xpath = element.find_elements_by_xpath(".//*")

        temps = []
        humidity = []
        wind_strength = []
        for i in range(int((len(all_children_by_xpath)-3) / 2)):
            temps.append(all_children_by_xpath[i*2].get_attribute("aria-label"))
            #print(all_children_by_xpath[i*2].get_attribute("aria-label"))
            humidity.append(driver.find_element_by_xpath("//*[@id='wob_pg']/div["+str(i+1)+"]/div[2]").get_attribute("aria-label"))
            #print(driver.find_element_by_xpath("//*[@id='wob_pg']/div["+str(i+1)+"]/div[2]").get_attribute("aria-label"))
        for i in range(int((len(all_children_by_xpath)) / 6)):
            wind_strength.append(driver.find_element_by_xpath("//*[@id='wob_wg']/div["+str(i+1)+"]/div[1]/span[1]").get_attribute("aria-label"))
            #print(driver.find_element_by_xpath("//*[@id='wob_wg']/div["+str(i+1)+"]/div[1]/span[1]").get_attribute("aria-label"))

        # weather for next week
        element = driver.find_elements_by_id("wob_dp")[0]
        source = element.get_attribute("outerHTML")
                
        start = 0
        while start != -1:
            start = source.find("//ssl", start, len(source))
            if start != -1:
                source = source[:start] + "https:" + source[start:]
                start = start + 10

        all_children_by_xpath = element.find_elements_by_xpath(".//*")

        days = []
        weather = []
        pics = []
        tempmax = []
        tempmin = []
        for i in range(7):
            days.append(driver.find_element_by_xpath("//*[@id='wob_dp']/div["+str(i+1)+"]/div[1]").get_attribute("aria-label"))
            weather.append(driver.find_element_by_xpath("//*[@id='wob_dp']/div["+str(i+1)+"]/div[2]/img").get_attribute("alt"))
            pics.append(driver.find_element_by_xpath("//*[@id='wob_dp']/div["+str(i+1)+"]/div[2]/img").get_attribute("src"))
            tempmax.append(driver.find_element_by_xpath("//*[@id='wob_dp']/div["+str(i+1)+"]/div[3]/div[1]/span[1]").text + "°C")
            tempmin.append(driver.find_element_by_xpath("//*[@id='wob_dp']/div["+str(i+1)+"]/div[3]/div[2]/span[1]").text + "°C")

        return {"temps": temps, "humiditys": humidity, "wind_strengths": wind_strength, "days": days, "weather": weather, "pics": pics, "tempmax": tempmax, "tempmin": tempmin, "source": source}

if __name__ == "__main__":

    a = Weather("gmunden")
    print(a.get_actual_weather())
    print(a.get_weather_prediction())

