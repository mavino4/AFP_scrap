#!/usr/bin/env python
# coding: utf-8

# In[19]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import datetime 
download_directory = "/media/F/sevima/CertificadosScrap"


print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠋⠉⠀⠀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⣀⣤⣤⣤⡾⠃⠀⠘⠷⠾⠿⠶⢾⠟⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠋⠁⣤⡄⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠈⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣠⣤⣴⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠿⠿⠿⠟⠛⠛⠛⠛⠛⠻⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠈⠻⢿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⣿⢷⡀⢀⠀⣀⣀⣠⣤⣴⣶⡿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠈⠙⠛⠿⢿⣶⣶⣶⣶⣶⣶⣶⡏⠀⣷⡌⢻⡿⠻⠛⠛⠛⠉⠁⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠾⠿⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

# INTRODUCCIÓN DE DATOS 


PATERNO = input("Apellido Paterno: ")
MATERNO = input("Apellido Materno: ")
NOMBRES = input("Nombre(s): ")

PATERNO = PATERNO.strip().title()
MATERNO = MATERNO.strip().title()
NOMBRES = NOMBRES.strip().title()

while True :
    try:
        CI      = int(input("Nro. CI (solo numeros):").strip())
    except ValueError:
        print("Porfavor ingrese solo números ")
        continue
    else:
        break


        
while True : 
    try:
        FEC_NAC = input("dd/mm/aaaa Fecha de nacimiento : \n ").strip()
        datetime.datetime.strptime(FEC_NAC, "%d/%m/%Y")
        break
    except ValueError:
        print("no es una fecha válida intente nuevamente") 




sexo_trys = 0 
while sexo_trys < 3 :
    SEXO   = input("Sexo: (M|F) :")
    SEXO   = SEXO.strip().upper()
    if  SEXO not in ("M","F"):
        print("introduzca un valor válido")
        sexo_trys += 1 
    else:
        break
else :
    SEXO = "M"
    print("Se asigna M por defecto")





ext_trys = 0 
while ext_trys < 3 :
    EXT_CI = input("(LP|CB|SC|BN|CH|OR|PN|PT|TR|PE) \n Ci expedido en : " ) 
    EXT_CI = EXT_CI.strip().upper()
    if  EXT_CI not in ("LP","CB","SC","BN","CH","OR","PN","PT","TR","PE"):
        print("introduzca un valor válido")
        ext_trys += 1 
    else:
        break
else :
    EXT_CI = "LP"
    print("Se asigna La Paz por defecto")
    
    


dict_sites = {
 "csbp"        : "https://noafiliacion.csbp.com.bo/"
,"cns"         : "https://www.cns.gob.bo/Servicios/NoAfiliacion"
,"cps"         : "https://afiliado.cps.org.bo/"
,"ssu"         : "http://190.181.13.35/siscanf/public/certificados"
,"afp_futuro"  : "https://www.afp-futuro.com/siswww/es/adt/asegurado/cerneg/bienvenida"
,"afp_prevision": "https://online.prevision.com.bo/CertificadosNegativoAsegurado.html"
}


# In[20]:



# Define browser preferences 
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip,application/pdf,document/pdf")
profile.set_preference("browser.link.open_newwindow", 3 )
profile.set_preference("browser.link.open_newwindow.restriction", 0 )


navegador = webdriver.Firefox(profile)
tabs = {}


# In[21]:



##############################
#### ObtenciOn de datos 
##############################


# In[22]:




# Bloque CNS 
driver = navegador.get(dict_sites["cns"])
tabs["cns"] = navegador.window_handles[0]

# Introducir Datos
ci_input = navegador.find_element_by_id("txtCI")
ci_input.send_keys(CI)

fecnac_input = navegador.find_element_by_id("txtFechaNacimiento")
fecnac_input.send_keys(FEC_NAC)



# In[23]:


# Bloque CSBP
navegador.execute_script("window.open('about:blank', '_blank');")
tabs["csbp"] = navegador.window_handles[1]
navegador.switch_to.window(tabs["csbp"])
navegador.get(dict_sites["csbp"])


nombre_input = navegador.find_element_by_id("nombre")
nombre_input.send_keys(NOMBRES)

paterno_input = navegador.find_element_by_id("paterno")
paterno_input.send_keys(PATERNO)

materno_input = navegador.find_element_by_id("materno")
materno_input.send_keys(MATERNO)

ci_input = navegador.find_element_by_id("ci")
ci_input.send_keys(CI)

fecnac_input = navegador.find_element_by_id("Fec")
fecnac_input.send_keys(FEC_NAC)

navegador.find_element_by_id("CaptchaInputText").click()


# In[24]:


# Bloque CPS
cps_dict_sexo = {"F" : "Femenino", 
                 "M" : "Masculino"}


cps_dict_ext = {  "BN" : "Beni"
                , "CH" : "Chuquisaca"
                , "CB" : "Cochabamba"
                , "LP" : "La Paz"
                , "OR" : "Oruro"
                , "PN" : "Pando"
                , "PT" : "Potosi"
                , "SC" : "Santa Cruz"
                , "TR" : "Tarija"
                , "PE" : "Exterior" }




navegador.execute_script("window.open('about:blank', '_blank');")
tabs["cps"] = navegador.window_handles[2]
navegador.switch_to.window(tabs["cps"])
navegador.get(dict_sites["cps"])



nombre_input = navegador.find_element_by_id("nombre")
nombre_input.send_keys(NOMBRES)

paterno_input = navegador.find_element_by_id("paterno")
paterno_input.send_keys(PATERNO)

materno_input = navegador.find_element_by_id("materno")
materno_input.send_keys(MATERNO)

ci_input = navegador.find_element_by_id("numero")
ci_input.send_keys(CI)

sexo_input = Select(navegador.find_element_by_id("sexo"))
sexo_input.select_by_visible_text(cps_dict_sexo[SEXO])

ext_ci_input = Select(navegador.find_element_by_id("expedido"))
ext_ci_input.select_by_visible_text(cps_dict_ext[EXT_CI])



# fecnac_input = navegador.find_element_by_id("fecha")
# fecnac_input.click()
# 
# fecnac_input.clear()
# fecnac_input.send_keys("05")


# In[ ]:





# In[ ]:





# In[25]:



# Bloque SSU

ssu_dict_exp = {
  "BN" : "BENI" 
, "CH" : "CHUQUISACA"
, "CB" :"COCHABAMBA"
, "LP" : "LA PAZ"
, "OR" : "ORURO"
, "PN" : "PANDO"
, "PT" : "POTOSI"
, "SC" : "SANTA CRUZ"
, "TR" : "TARIJA"
, "PE" : "LA PAZ"  # Atendiendo casos por defecto 
}


navegador.execute_script("window.open('about:blank', '_blank');")
tabs["ssu"] = navegador.window_handles[3]
navegador.switch_to.window(tabs["ssu"])
navegador.get(dict_sites["ssu"])

paterno_input = navegador.find_element_by_id("ap_paterno")
paterno_input.send_keys(PATERNO)

materno_input = navegador.find_element_by_id("ap_materno")
materno_input.send_keys(MATERNO)

nombre_input = navegador.find_element_by_id("nombre")
nombre_input.send_keys(NOMBRES)

ci_input = navegador.find_element_by_id("ci")
ci_input.send_keys(CI)

ext_ci_input = Select(navegador.find_element_by_id("departamento"))
ext_ci_input.select_by_visible_text(ssu_dict_exp[EXT_CI])


# In[26]:


# Bloque afp_futuro

navegador.execute_script("window.open('about:blank', '_blank');")
tabs["afp_futuro"] = navegador.window_handles[4]
navegador.switch_to.window(tabs["afp_futuro"])
navegador.get(dict_sites["afp_futuro"])


nombre_input = navegador.find_element_by_id("NBRCOMPLETO")
nombre_input.send_keys(" ".join([NOMBRES,PATERNO, MATERNO]))


ext_ci_input = Select(navegador.find_element_by_id("TIPOIDASEG"))
ext_ci_input.select_by_visible_text("CI")


ci_input = navegador.find_element_by_id("NROIDASEG")
ci_input.send_keys(CI)


# Potenciales errores 


input("Presione cualquier tecla para terminar")
navegador.close()




