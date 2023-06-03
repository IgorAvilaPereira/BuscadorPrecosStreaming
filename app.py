from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

class BuscadorPrecosStreaming:

    def __init__(self, assistir = False):
        # se quiser não ver nada
        if (assistir is False):
            options = Options()
            options.add_argument("--headless=new")
            self.driver = webdriver.Chrome(options=options)
        else: 
            # se quiser ver a execucao no navegador
            self.driver = webdriver.Chrome()

    def primeVideo(self):        
        self.driver.get("https://www.primevideo.com/")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/p")
        result = elem.text[elem.text.find("R$"):elem.text.find("ano")]+")"
        print("PrimeVideo:"+result.replace("month", "mês").replace("year", "ano").replace("or", "ou").replace(". Cancel anytime)", ""))
    
    def hboMax(self):        
        self.driver.get("https://www.hbomax.com/br/pt")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[4]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[1]/span[1]")
        print("HBOMax:"+elem.text+"/mês")

    def netFlix(self):
        self.driver.get("https://help.netflix.com/pt/node/24926")        
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[3]/p")
        print("Netflix (Padrão):"+elem.text)
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[4]/p")        
        print("Netflix (Premium):"+elem.text)
    
    # bug
    def appleTv(self):
        self.driver.get("https://tv.apple.com/br/channel/tvs.sbd.4000")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/div[3]/section[3]/div/ul/li[2]/h3/button")
        elem.click()
        elem = self.driver.find_element(By.XPATH, "/html/body/main/div[3]/section[3]/div/ul/li[2]/div")
        print("AppleTv+:"+elem.text)

if __name__ == "__main__":            
    buscador = BuscadorPrecosStreaming()
    buscador.primeVideo()
    buscador.hboMax()
    buscador.netFlix()
    # bug
    # buscador.appleTv()



