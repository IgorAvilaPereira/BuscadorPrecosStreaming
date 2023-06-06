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
    
    
    def appleTv(self):
        self.driver.get("https://www.apple.com/br/apple-tv-plus/#:~:text=Ap%C3%B3s%20o%20teste%20gratuito%20de,TV%2B%20com%20sua%20fam%C3%ADlia%202.")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/h3")
        print("AppleTv+:"+elem.text)

    def paramount(self):
        self.driver.get("https://www.paramountplus.com/br/?ftag=IPP-02-10aab2c&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zskUAbnnSwmUK_vYhtiL9AQYHabEJ0jugYJl114p1m_P7pxhMTSakaAvIAEALw_wcB")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/section[1]/section/div/div/div[1]/strong[1]")
        print("Paramount+:"+elem.text)

    def disneyStarLionsgate(self):
        self.driver.get("https://www.disneyplus.com/pt-br?cid=DSS-Search-Google-71700000075038504-&s_kwcid=AL!8468!3!576459364510!e!!g!!disney%20plus&gad=1&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zpeDuXapVVyPaZYnHuzmWK0EQ5nfh7WNk_cf-T2Dspmytoku_FKA4aAoKqEALw_wcB&gclsrc=aw.ds")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/div/section/div/div[1]/div[1]/div[4]/div/a/span")
        print("Combo (Disney+, Star+ e Lionsgate+):"+elem.text)

if __name__ == "__main__":            
    buscador = BuscadorPrecosStreaming()
    # buscador.primeVideo()
    # buscador.hboMax()
    # buscador.netFlix()    
    # buscador.appleTv()
    # buscador.paramount()
    buscador.disneyStarLionsgate()



