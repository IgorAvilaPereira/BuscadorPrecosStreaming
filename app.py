from buscador import *
import flet as ft

def main(page):
    page.title = "BuscadorPrecosStreaming - Desenvolvido por Igor Avila Pereira"
    page.padding = 50
    
    tx = ft.Text("Atualizando Preços dos Streamings. Espere um pouco...")
    
    images_loading = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5
    )
    images_loading.controls.append(ft.Image(src=f"assets/icons/loading.gif", width=100, height=100, fit=ft.ImageFit.CONTAIN))    
    page.add(tx)
    page.add(images_loading)
    page.update()

    buscador = BuscadorPrecosStreaming(False)    
    # method_list = [method for method in dir(BuscadorPrecosStreaming) if method.startswith('__') is False]        
    # method_list = ["primeVideo", "appleTvPlus"]    
    method_list = ["primeVideo", "appleTvPlus", "playplus", "hboMax", "netFlix", "paramountPlus", "globoPlay", "discoveryPlus", "disneyPlus"]    
    streamings = []
    for method in method_list:
        streamings.append(dict(name = method, price = float(eval("buscador."+method+"()"))))                        
    streamings = sorted(streamings, key=lambda k: k['price'])          

    tx.visible = False
    images_loading.visible = False

    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
  
    def slider_changed(e):
        t.value = f"Orçamento Mensal para Entretenimento: R$ {int(e.control.value)}"   
        images.controls = []        
        if (int(e.control.value) == 0):
            page.update()
            return "" 
        sum = 0
        i = 0
        name = ""
        price = 0        
        while (sum <= int(e.control.value) and i < len(streamings)):                       
            for key, val in streamings[i].items():
                if key == 'name':
                    name = val
                elif key == 'price':
                    price = float(val)  
            sum = sum + price
            if (sum <= int(e.control.value)):            
                images.controls.append(
                    ft.Image(
                        # src=f"https://picsum.photos/150/150?{i}",
                        src=f"assets/"+name+".png",
                        fit=ft.ImageFit.NONE,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.border_radius.all(10),
                    )
                )
                images.controls.append(ft.Text("R$ "+str(price)))

            i = i + 1  
        page.update()
        
    # t = ft.Text(style  = ft.FontWeight.BOLD)
    t = ft.Text()

    page.add(
        ft.Text("Qual é seu orçamento mensal para Streamings?"),
        ft.Slider(min=0, max=500, divisions=100, label="R$ {value}", on_change=slider_changed), t)    
    page.add(images)
    page.update()

# desktop
# pipreqs ./
ft.app(target=main, assets_dir="assets")

# web
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)