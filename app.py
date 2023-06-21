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

# class Streaming:

#     def __init__(self, nome, preco, logo):
#         self.nome = nome
#         self.preco = preco
#         self.logo = logo

#     def __repr__(self) -> str:
#         return self.nome+";"+self.preco+";"+self.logo

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
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[3]/p")        
        resultado = "Netflix:\n"        
        # "Padrão:"
        resultado = resultado + "*"+elem.text        
        # Premium
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div[1]/section[2]/div/div/div[3]/ul/li[4]/p")        
        resultado = resultado +"\n"+"*"+elem.text
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
    def disneyStarLionsgate(self) -> str:
        self.driver.get("https://www.disneyplus.com/pt-br?cid=DSS-Search-Google-71700000075038504-&s_kwcid=AL!8468!3!576459364510!e!!g!!disney%20plus&gad=1&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0zpeDuXapVVyPaZYnHuzmWK0EQ5nfh7WNk_cf-T2Dspmytoku_FKA4aAoKqEALw_wcB&gclsrc=aw.ds")
        elem = self.driver.find_element(By.XPATH, "/html/body/main/div/section/div/div[1]/div[1]/div[4]/div/a/span")
        # print("Combo (Disney+, Star+ e Lionsgate+):"+elem.text)
        return "Combo (Disney+, Star+ e Lionsgate+):"+elem.text
    
    def playplus(self) -> str:
        self.driver.get("https://www.playplus.com/flow/plans")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/form/div[1]/div/div/div/div/div/div[2]/div[1]/h3")
        # print("PlayPlus+:"+elem.text)
        return "PlayPlus+:"+elem.text

    def discovery(self) -> str:
        self.driver.get("https://www.discoveryplus.com/br/")
        elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/section[7]/div[3]/ul[1]/li[2]/div[3]")
        # print("Discovery+:"+elem.text)
        return "Discovery+:"+elem.text


# python3.10 app.py 
if __name__ == "__main__":          

    buscador = BuscadorPrecosStreaming()
    
    print("Obtendo valores...")
    print(buscador.primeVideo())
    print(buscador.hboMax())
    print(buscador.appleTv())
    print(buscador.paramount())
    # print(buscador.disneyStarLionsgate())
    print(buscador.playplus())
    print(buscador.discovery())
    print(buscador.netFlix())


    # from tkinter import *
    # from tkinter import ttk
    # from tkinter import messagebox
    # root = Tk()
    # root.geometry("400x400")
    # frm = ttk.Frame(root, padding=10)
    # frm.grid()
    # messagebox.showinfo("BuscadorPreçosStreaming", "Obtendo Valores (espere algum tempo)")
    # ttk.Label(frm, text=buscador.primeVideo()).grid(column=0, row=0)
    # ttk.Label(frm, text=buscador.hboMax()).grid(column=0, row=1)
    # ttk.Label(frm, text=buscador.appleTv()).grid(column=0, row=2)
    # ttk.Label(frm, text=buscador.paramount()).grid(column=0, row=3)
    # ttk.Label(frm, text=buscador.disneyStarLionsgate()).grid(column=0, row=4)
    # ttk.Label(frm, text=buscador.playplus()).grid(column=0, row=5)
    # ttk.Label(frm, text=buscador.discovery()).grid(column=0, row=6)
    # ttk.Label(frm, text=buscador.netFlix()).grid(column=0, row=7)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=8)
    # root.mainloop()

 
# import flet as ft
# def main(page: ft.Page):
#     buscador = BuscadorPrecosStreaming()
#     resultado = buscador.primeVideo()
#     resultado = resultado + "\n" + buscador.hboMax()  
#     resultado = resultado + "\n" + buscador.appleTv()
#     resultado = resultado + "\n" + buscador.paramount()
#     resultado = resultado + "\n" + buscador.disneyStarLionsgate()
#     resultado = resultado + "\n" + buscador.playplus()
#     resultado = resultado + "\n" + buscador.discovery()
#     resultado = resultado + "\n" + buscador.netFlix()    
#     t = ft.Text(value=resultado, color="black")
#     page.controls.append(t)
# ft.app(target=main)



