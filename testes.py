from buscador import *

if __name__ == "__main__":          
    buscador = BuscadorPrecosStreaming(False)    
    print(buscador.disneyPlus())

#     # method_list = [method for method in dir(BuscadorPrecosStreaming) if method.startswith('__') is False]
#     # method_list = ["primeVideo", "appleTvPlus", "hboMax", "playplus", "netFlix"]    
#     # streamings = []
#     # for method in method_list:
#     #     streamings.append(dict(name = method, price = float(eval("buscador."+method+"()"))))
#     # print(streamings)
#     # streamings = sorted(streamings, key=lambda k: k['price'])
#     # print(streamings)
#     print("Obtendo valores...")
#     print(buscador.primeVideo())
#     print(buscador.appleTvPlus())
#     print(buscador.hboMax())     
#     print(buscador.playplus())        
#     print(buscador.netFlix())       
    # bugs
    # print(buscador.starplus())   
    # print(buscador.paramount())    
    # print(buscador.disneyStarLionsgate())        
    # print(buscador.discovery())    