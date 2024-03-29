import sys
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

from selenium import webdriver                  
from selenium.webdriver.common.keys import Keys 
import geckodriver_autoinstaller             

class BuscadorPrecosStreaming:            

    def __init__(self, assistir = True):         
        geckodriver_autoinstaller.install()             
        # se quiser não ver nada
        if (assistir is False):
            fireFoxOptions = webdriver.FirefoxOptions()            
            # fireFoxOptions.headless = True
            fireFoxOptions.add_argument('-headless')
            self.driver = webdriver.Firefox(options=fireFoxOptions)                            
        else:                                     
            self.driver = webdriver.Firefox()                  
            # se quiser ver a execucao no navegador
            # self.driver = webdriver.Chrome()

    # def primeVideoStreaming(self) -> Streaming:
    #     # nome
    #     nome = "PrimeVideo"

    #     self.driver.get("https://www.primevideo.com/")
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/p")
    #     result = elem.text[elem.text.find("R$"):elem.text.find("ano")]+")"
        
    #     # preco
    #     preco = result.replace("month", "mês").replace("year", "ano").replace("or", "ou").replace(". Cancel anytime)", "")        
        
    #     # logo
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div/div/div/a/img")
    #     logo = elem.get_attribute("outerHTML")
        
    #     return Streaming(nome, preco, logo)
    
    def globoPlay(self) -> float:
        try:
            self.driver.get("https://vitrine.globo.com/globoplay")
            sleep(5)
            elem = self.driver.find_element(By.XPATH,"/html/body/app-root/main/app-product/app-offer-list[1]/section/div/app-offer-list-carousel/div/app-offer-toggle/div/div/button[1]")
            elem.click()            
            elem = self.driver.find_element(By.XPATH, "/html/body/app-root/main/app-product/app-offer-list[1]/section/div/app-offer-list-carousel/div/splide/div/div/div/div[1]/app-offer-card/article/div[2]/app-parcel-value/span/span[2]")
            return elem.text.replace("R$", "").replace(",",".").replace("/mês", "").strip()
        except:
            print("Problema com o GloboPlay")
            # print(elem.text)
            return -1

    def primeVideo(self) -> float:        
        try:
            self.driver.get("https://www.primevideo.com/")
            elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/p")
            result = elem.text[elem.text.find("R$"):elem.text.find("ano")]+")"                
            return result.replace("month", "mês").replace("year", "ano").replace("or", "ou").replace(". Cancel anytime)", "").split("/mês")[0].replace("R$","").replace(",", ".")
        except:
            print("Problema com o PrimeVideo")
            return -1

    # def hboMaxStreaming(self) -> Streaming:        
    #     nome = "HBOMax"

    #     self.driver.get("https://www.hbomax.com/br/pt")
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[4]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[1]/span[1]")
    #     preco = elem.text

    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[1]/div/div/div/nav/div[1]/a/img")
    #     logo = elem.get_attribute("outerHTML")

    #     return Streaming(nome, preco, logo)

    def hboMax(self) -> float:     
        try:   
            self.driver.get("https://www.hbomax.com/br/pt")
            elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[4]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[1]/span[1]")
            # print("HBOMax:"+elem.text+"/mês")
            # return "HBOMax:"+elem.text
            return elem.text.replace(",", ".").replace("R$","").strip()
        except:
            print("Problema com a HboMax")
            return -1


    # bug
    # def netFlixStreaming(self) -> Streaming:
    #     #  nome
    #     nome = "Netflix"

    #     self.driver.get("https://help.netflix.com/pt/node/24926")        
        
    #     # preco
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[3]/p")
    #     preco = "Netflix (Padrão):"+elem.text 
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[4]/p")        
    #     preco = preco + "Netflix (Premium):"+elem.text
        
    #     # logo
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/svg[1]")
    #     logo = elem.get_attribute("outerHTML")
        
    #     return Streaming(nome, preco, logo)


    def netFlix(self) -> float:
        try:  
            self.driver.get("https://help.netflix.com/pt/node/24926")        
            elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[2]/p")        
        # resultado = "Netflix:\n"        
        # "Padrão:"        
        # Premium
        # elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[4]/p")        
        # resultado = resultado +"\n"+"*"+elem.text
            return elem.text.replace("Padrão:", "").replace("R$","").replace(",", ".").split("/mês")[0].strip()      
        except:
            print("Problema com a NetFlix")
            return -1
    

    # def appleTvStreaming(self) -> Streaming:
    #     nome = "AppleTv"
    #     self.driver.get("https://www.apple.com/br/apple-tv-plus/#:~:text=Ap%C3%B3s%20o%20teste%20gratuito%20de,TV%2B%20com%20sua%20fam%C3%ADlia%202.")
        
    #     elem = self.driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/h3")
    #     preco = elem.text.replace("por mês", "").strip()    

    #     elem = self.driver.find_element(By.XPATH, "/html/body/main/section[5]/div/div[1]/figure")
    #     logo = elem.get_attribute("outerHTML")
        
    #     return Streaming(nome, preco, logo)
    
    def appleTvPlus(self) -> float:
        try:
            self.driver.get("https://www.apple.com/br/apple-tv-plus/#:~:text=Ap%C3%B3s%20o%20teste%20gratuito%20de,TV%2B%20com%20sua%20fam%C3%ADlia%202.")
            elem = self.driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/h3")
            # print("AppleTv+:"+elem.text.replace("por mês", "").strip())
            return elem.text.replace("por mês", "").replace("R$","").replace(",", ".").strip()
        except:
            print("Problema com a AppleTv+")
            return -1
    # bug
    def paramountPlus(self) -> float:
        try:
            self.driver.get("https://www.paramountplus.com/br/?ftag=IPP-02-10aab2c&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zskUAbnnSwmUK_vYhtiL9AQYHabEJ0jugYJl114p1m_P7pxhMTSakaAvIAEALw_wcB")
            # sleep(3)
            elem = self.driver.find_element(By.XPATH, "/html/body/main/section[1]/section/div/div/div[1]/strong[2]")
            # print("Paramount+:"+elem.text.replace("Cancele a qualquer momento.", "").strip())
            return elem.text.split("R$")[1].split("/mês")[0].replace(",",".").strip()
        except:
            print("Problema com o Paramount")
            return -1
     
    def disneyPlus(self) -> float:
        try:
            self.driver.get("https://www.minhaconexao.com.br/planos/streaming/disney-plus#:~:text=Atualmente%2C%20o%20Disney%20Plus%20oferece,mais%20sobre%20o%20Disney%2B%20abaixo!")        
            elem = self.driver.find_element(By.XPATH, "/html/body/section[4]/div/div/div/p[1]/strong")        
            return elem.text.split("R$")[1].replace(".","").replace(",",".").strip()        
        except:
            print("Problema com o Disney+")
            return -1
    
    def playplus(self) -> float:
        try:
            self.driver.get("https://www.playplus.com/flow/plans")
            elem = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/div/div/div/div/div[2]/div[1]/h3")
            # print("PlayPlus+:"+elem.text)
            return elem.text.replace("R$", "").replace(",",".").replace("**", "").strip()
        except:
            print("Problema com a PlayPlus")
            return -1
    
    def discoveryPlus(self) -> float:
        try:
            self.driver.get("https://www.discoveryplus.com/br")
            elem = self.driver.find_element(By.XPATH, "/html/body/div/main/section[7]/div[3]/ul[1]/li[2]/div[3]")        
            return elem.text.replace("R$","").replace(",", ".").replace("/mês", "").strip()
        except:
            print("Problema com o Discovery+")
            return -1
    
    # bug
    def starplus(self) -> str:        
        self.driver.get("https://help.starplus.com/pt-BR/article/starplus-pt-br-how-much-does-star-plus-cost")
        # elem = self.driver.find_element(By.XPATH,"//*[@id=\"main-8\"]/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout/div/webruntime-component-container[2]/community_layout-section/div[3]/community_layout-column[1]/div/webruntime-component-container/c-dtcvx_article/div/div[1]/p/p[8]/strong[1]")
        elem = self.driver.find_element(By.CSS_SELECTOR, "#main-8 > slot > webruntime-router-container > dxp_data_provider-user-data-provider > dxp_data_provider-data-proxy > community_layout-slds-flexible-layout > div > webruntime-component-container:nth-child(2) > community_layout-section > div.lwc-6j9an5vbrcd.columns-content > community_layout-column.col-size_12-of-12.lwc-48aostf02bd-host.col-large-size_8-of-12 > div > webruntime-component-container > c-dtcvx_article > div > div.slds-rich-text-editor__output.uiOutputRichText.forceOutputRichText.article-content.plus-brands-article-content > p > p:nth-child(10) > strong:nth-child(1)")
        return "Star+:"+elem.text.strip()