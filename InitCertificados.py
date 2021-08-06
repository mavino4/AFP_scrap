from selenium import webdriver
import time 
download_directory = "/media/F/sevima/CertificadosScrap"


# iNTRODUCCIÒN DE DATOS 

PATERNO = "QUISPE"                              #input("Apellido Paterno: ")
MATERNO = "AQUISE"                             #input("Apellido Materno: ")
NOMBRES = "JHONATAN"                              #input("Nombre(s): ")
CI      = "456137"                              #input("Nro. CI (solo numeros):")
FEC_NAC = "31/03/1985"                              #input("dd/mm/aaaa Fecha de nacimiento : \n ")

PATERNO = PATERNO.upper()
MATERNO = MATERNO.upper()
NOMBRES = NOMBRES.upper()


dict_sites = {
 "csbp"        : "https://noafiliacion.csbp.com.bo/"
,"cns"         : "https://www.cns.gob.bo/Servicios/NoAfiliacion"
,"cps"         : "https://afiliado.cps.org.bo/"
,"ssu"         : "http://190.181.13.35/siscanf/public/certificados"
,"afp_futuro"  : "https://www.afp-futuro.com/siswww/es/adt/asegurado/cerneg/bienvenida"
}




# Define browser preferences 
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip,application/pdf,document/pdf")
profile.set_preference("browser.link.open_newwindow", 3 )
profile.set_preference("browser.link.open_newwindow.restriction", 0 )


navegador = webdriver.Firefox(profile)
tabs = {}


##############################
#### ObtenciOn de datos 
##############################


# Bloque CNS 
driver = navegador.get(dict_sites["cns"])
tabs["cns"] = navegador.window_handles[0]

# Introducir Datos
ci_input = navegador.find_element_by_id("txtCI")
ci_input.send_keys(CI)

fecnac_input = navegador.find_element_by_id("txtFechaNacimiento")
fecnac_input.send_keys(FEC_NAC)



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


# Bloque CPS
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

fecnac_input = navegador.find_element_by_id("fecha")




# Bloque SSU
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

fecnac_input = navegador.find_element_by_id("fecha_nacimiento")
fecnac_input.send_keys(FEC_NAC)


# Bloque afp_futuro

navegador.execute_script("window.open('about:blank', '_blank');")
tabs["afp_futuro"] = navegador.window_handles[4]
navegador.switch_to.window(tabs["afp_futuro"])
navegador.get(dict_sites["afp_futuro"])


nombre_input = navegador.find_element_by_id("NBRCOMPLETO")
nombre_input.send_keys(" ".join(NOMBRES))


ci_input = navegador.find_element_by_id("NROIDASEG")
ci_input.send_keys(CI)


# Potenciales errores 




