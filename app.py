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

    def primeVideo(self) -> str:        
        self.driver.get("https://www.primevideo.com/")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/p")
        result = elem.text[elem.text.find("R$"):elem.text.find("ano")]+")"
        # print("PrimeVideo:"+result.replace("month", "mês").replace("year", "ano").replace("or", "ou").replace(". Cancel anytime)", ""))
        return "PrimeVideo:"+result.replace("month", "mês").replace("year", "ano").replace("or", "ou").replace(". Cancel anytime)", "")

    # def hboMaxStreaming(self) -> Streaming:        
    #     nome = "HBOMax"

    #     self.driver.get("https://www.hbomax.com/br/pt")
    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[4]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[1]/span[1]")
    #     preco = elem.text

    #     elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[1]/div/div/div/nav/div[1]/a/img")
    #     logo = elem.get_attribute("outerHTML")

    #     return Streaming(nome, preco, logo)

    def hboMax(self) -> str:        
        self.driver.get("https://www.hbomax.com/br/pt")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/article/section[4]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[1]/span[1]")
        # print("HBOMax:"+elem.text+"/mês")
        # return "HBOMax:"+elem.text
        return "HBOMax:"+elem.text+"/mês"

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


    def netFlix(self) -> str:
        self.driver.get("https://help.netflix.com/pt/node/24926")        
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[2]/p")        
        resultado = "Netflix:\n"        
        # "Padrão:"
        resultado = resultado + "*"+elem.text        
        # Premium
        # elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[4]/p")        
        # resultado = resultado +"\n"+"*"+elem.text
        return resultado
    

    # def appleTvStreaming(self) -> Streaming:
    #     nome = "AppleTv"
    #     self.driver.get("https://www.apple.com/br/apple-tv-plus/#:~:text=Ap%C3%B3s%20o%20teste%20gratuito%20de,TV%2B%20com%20sua%20fam%C3%ADlia%202.")
        
    #     elem = self.driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/h3")
    #     preco = elem.text.replace("por mês", "").strip()    

    #     elem = self.driver.find_element(By.XPATH, "/html/body/main/section[5]/div/div[1]/figure")
    #     logo = elem.get_attribute("outerHTML")
        
    #     return Streaming(nome, preco, logo)
    
    def appleTv(self) -> str:
        self.driver.get("https://www.apple.com/br/apple-tv-plus/#:~:text=Ap%C3%B3s%20o%20teste%20gratuito%20de,TV%2B%20com%20sua%20fam%C3%ADlia%202.")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/h3")
        # print("AppleTv+:"+elem.text.replace("por mês", "").strip())
        return "AppleTv+:"+elem.text.replace("por mês", "").strip()

    def paramount(self) -> str:
        self.driver.get("https://www.paramountplus.com/br/?ftag=IPP-02-10aab2c&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zskUAbnnSwmUK_vYhtiL9AQYHabEJ0jugYJl114p1m_P7pxhMTSakaAvIAEALw_wcB")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/section[1]/section/div/div/div[1]/strong[1]")
        # print("Paramount+:"+elem.text.replace("Cancele a qualquer momento.", "").strip())
        return "Paramount+:"+elem.text.replace("Cancele a qualquer momento.", "").strip()
    
    # bug
    def starplus(self) -> str:
        self.driver.get("https://help.starplus.com/pt-BR/article/starplus-pt-br-how-much-does-star-plus-cost")
        elem = self.driver.find_element(By.XPATH,"/html/body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-dtcvx_support-theme/div/section/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout/div/webruntime-component-container[2]/community_layout-section/div[3]/community_layout-column[1]/div/webruntime-component-container/c-dtcvx_article/div/div[1]/p/p[8]/text()[1]")
        return "Star+:"+elem.text.strip()
    
    # bug
    def disneyStarLionsgate(self) -> str:
        self.driver.get("https://www.disneyplus.com/pt-br?cid=DSS-Search-Google-71700000075038504-&s_kwcid=AL!8468!3!576459364510!e!!g!!disney%20plus&gad=1&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zpeDuXapVVyPaZYnHuzmWK0EQ5nfh7WNk_cf-T2Dspmytoku_FKA4aAoKqEALw_wcB&gclsrc=aw.ds")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/div/section/div/div[1]/div[1]/div[4]/div/a/span")
        # print("Combo (Disney+, Star+ e Lionsgate+):"+elem.text)
        return "Combo (Disney+, Star+ e Lionsgate+):"+elem.text
    
    def playplus(self) -> str:
        self.driver.get("https://www.playplus.com/flow/plans")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/div/div/div/div/div[2]/div[1]/h3")
        # print("PlayPlus+:"+elem.text)
        return "PlayPlus+:"+elem.text

    def discovery(self) -> str:
        self.driver.get("https://www.discoveryplus.com/br/")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/section[7]/div[3]/ul[1]/li[2]/div[3]")
        # print("Discovery+:"+elem.text)
        return "Discovery+:"+elem.text

if __name__ == "__main__":          
    buscador = BuscadorPrecosStreaming(False)    

    print("Obtendo valores...")
    print(buscador.primeVideo())
    print(buscador.appleTv())
    print(buscador.hboMax())     
    print(buscador.playplus())        
    print(buscador.netFlix())       

    # bug
    # print(buscador.starplus())   
    # print(buscador.paramount())    
    # print(buscador.disneyStarLionsgate())        
    # print(buscador.discovery())    

# bom
# import flet as ft

# def main(page):
#     # page.title = "GridView Example"
#     page.padding = 50
  
#     images = ft.GridView(
#         expand=1,
#         runs_count=5,
#         max_extent=150,
#         child_aspect_ratio=1.0,
#         spacing=5,
#         run_spacing=5,
#     )
  
#     def slider_changed(e):
#         t.value = f"Orçamento Mensal para Entretenimento: R$ {e.control.value}"
#         images.controls = []
#         for i in range(0, int(e.control.value)):
#             images.controls.append(
#                 ft.Image(
#                     # src=f"https://picsum.photos/150/150?{i}",
#                     src=f"assets/netflix.png",
#                     fit=ft.ImageFit.NONE,
#                     repeat=ft.ImageRepeat.NO_REPEAT,
#                     border_radius=ft.border_radius.all(10),
#                 )
#             )  
#         page.update()

#     t = ft.Text()

#     page.add(
#         ft.Text("Qual é seu orçamento mensal para Streamings?"),
#         ft.Slider(min=0, max=500, divisions=100, label="{value}", on_change=slider_changed), t)
    
#     page.add(images)
#     page.update()


# ft.app(target=main)