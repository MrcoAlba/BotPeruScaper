from DrissionPage                       import ChromiumPage, ChromiumOptions
from datetime                           import datetime
from webScripting.WebScriptingModels    import Product
from webScripting.skuReader             import getSKUcodes
from support.Write                      import append_to_csv
from pyvirtualdisplay                   import Display # type: ignore
import time
import re
import traceback
import csv

class Passer :
    def __init__ (OOO0OO0OO0OOO000O ,O0O0O000OO0O0OOOO :ChromiumPage ): OOO0OO0OO0OOO000O .driver =O0O0O000OO0O0OOOO
    def cc (OO000O0OOO0O0000O ):
        if OO000O0OOO0O0000O .driver .wait .ele_displayed ('.spacer',timeout =1.5 ):
            time .sleep (1.5 )
            OO000O0OOO0O0000O .driver .ele (".spacer",timeout =2.5 ).click ()
    def ib (OOO0OOOOOOOOO0OOO ):
        O000O0O000O00OO0O =OOO0OOOOOOOOO0OOO .driver .title .lower ()
        return "just a moment"not in O000O0O000O00OO0O
    def bp (OOO0O00OO0O0000OO ):
        while not OOO0O00OO0O0000OO .ib ():
            time .sleep (2 )
            time .sleep (2 )
            OOO0O00OO0O0000OO .cc ()

def extract_prices(texto):
    patron = r"S/(\d+\.\d+)"
    coincidencias = re.findall(patron, texto)
    if len(coincidencias) == 2: return float(coincidencias[0]), float(coincidencias[1])
    else: return 0.0,0.0

def WebScripBP(file, sleep_time, file_export, file_errors):
    with Display(visible=False, size=[1200,1500]):
        products = getSKUcodes(file)
        try:
            opt = ChromiumOptions()
            opt.set_paths(browser_path="/usr/bin/google-chrome")
            args = [
                "-no-first-run","-force-color-profile=srgb","-metrics-recording-only","-password-store=basic",
                "-use-mock-keychain","-export-tagged-pdf","-no-default-browser-check","-disable-background-mode",
                "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
                "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage","-deny-permission-prompts",
                "-disable-gpu","-accept-lang=en-US",
            ]

            for arg in args:
                opt.set_argument(arg)

            driver = ChromiumPage(addr_or_opts=opt)
            driver.get("https://boticasperu.pe/neutrogena-hydro-boost-water-gel-frasco-50-g.html")
            bp = Passer(driver)
            bp.bp()
            for product in products:
                try:
                    driver.get(product[4])
                    if "404" in driver.title:
                        continue
                    contenido = driver.ele('.product-info-main').text
                    if "Disponible" in contenido:
                        indice_disponible = contenido.find("\nDisponible")
                        contenido = contenido[:indice_disponible]
                    elif "Fuera de stock" in contenido:
                        indice_disponible = contenido.find("\nFuera de stock")
                        contenido = contenido[:indice_disponible]
                    contenido_en_lista = list(contenido.split("\n"))
                    contenido_en_lista.pop(0)
                    valores_finales = "|".join(contenido_en_lista)
                    
                    especial = 0.0
                    normal = 0.0
                    if "Precio" in valores_finales:
                        especial, normal = extract_prices(valores_finales)
                    else:
                        normal = re.findall(r"S/(\d+\.\d+)", valores_finales)[0]

                    productFound = Product(
                        description        = product[3],
                        idResultadoBusqueda= product[0],
                        idProducto         = product[1],
                        idCompetencia      = product[2],
                        Precio             = normal,
                        PrecioOferta       = especial,
                        PrecioTarjeta      = 0.0,
                        FechaRegistroS     = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                    )
                    with open(file_export, 'a', encoding='UTF8') as f:
                        writer = csv.writer(f,delimiter="|")
                        writer.writerow([
                            productFound.description        ,
                            productFound.idResultadoBusqueda,
                            productFound.idProducto         ,
                            productFound.idCompetencia      ,
                            productFound.Precio             ,
                            productFound.PrecioOferta       ,
                            productFound.PrecioTarjeta      ,
                            productFound.FechaRegistroS                 
                            ])
                        f.close()
                except Exception as e:
                    traceback_str = traceback.extract_tb(e.__traceback__)
                    filename, line_num, func_name, line_text = traceback_str[-1]
                    append_to_csv(file_errors,f"Hubo un error fatal con el producto {product[5]}. La excepción fue en la siguiente linea:{line_num}")
            time.sleep(5)
            driver.quit()
            return True
        except Exception as e:
            time.sleep(5)
            driver.quit()
            return False