import os
import sys 
import requests
from time import time
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


print ("¿Quieres descargar los archivos en Epub? y/n [Default=Pdf]")
formatpref= input ()
if (formatpref == "y"):
    epub="epub"
elif (formatpref == "n"):
    epub="pdf"
else:
    print("Please answer with y or n")
    sys.exit()

print ("""

Elige que categoría quieres descargar [0=All]""")
print ("""
0. Todas
1. Derecho Constitucional
2. Derecho Administrativo General
3. Función Pública
4. Seguridad Vial, Transporte y Telecomunicaciones
5. Defensa y Seguridad
6. Derecho Tributario
7. Derecho Financiero
8. Derecho Procesal
9. Derecho Penal

""")
categories= input ()


def url_response(url):

    path, url = url

    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:

        for ch in r:

            f.write(ch)





urls1 = [

#Constitucional
    
("Constitución Española", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=151_Constitucion_Espanola.{epub}"),

("Consejo de Estado", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=025_Consejo_de_Estado.{epub}"),

("Código Parlamentario, Normativa estatal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=246_Codigo_Parlamentario_Normativa_estatal.{epub}"),

("Codigo del Ministerio Fiscal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=280_Codigo_del_Ministerio_Fiscal.{epub}"),

("Código de Extranjería", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=070_Codigo_de_Extranjeria.{epub}"),

("Igualdad de Género", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=304_Igualdad_de_Genero_.{epub}"),

("Código de Derecho Eclesíastico", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=104_Codigo_de_Derecho_Eclesiastico.{epub}"),

("Protección de Datos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=055_Proteccion_de_Datos_de_Caracter_Personal.{epub}"),

("Código de Derecho al Olvido", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=094_Codigo_del_Derecho_al_Olvido.{epub}"),

("Código de la Discapacidad", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=125_Codigo_de_la_Discapacidad.{epub}"),

("Código de Derecho Eclesiastico", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=104_Codigo_de_Derecho_Eclesiastico.{epub}"),

("Código de Asociaciones", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=154_Codigo_de_Asociaciones.{epub}"),

("Código de Derecho Electoral", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=101_Codigo_de_Derecho_Electoral.{epub}"),

("Código de Tribunal Constitucional", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=012_Tribunal_Constitucional.{epub}"),

("Código de Derecho Publico de la Juventud", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=324_Codigo_de_Derecho_Publico_de_la_Juventud.{epub}"),

("Código de Legislacion de Menores", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=286_Legislacion_de_Menores.{epub}"),
]

urls2 = [

#Administrativo General

("Código de Derecho Administrativo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=044_Codigo_de_Derecho_Administrativo.{epub}"),

("Procedimiento Administrativo Común", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=282_Procedimiento_Administrativo_Comun.{epub}"),

("Código de Administración Electrónica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=029_Codigo_de_Administracion_Electronica.{epub}"),

("Código de Contratos del Sector Público", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=031_Codigo_de_Contratos_del_Sector_Publico.{epub}"),

("Patrimonio de las Administraciones Públicas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=170_Patrimonio_de_las_Administraciones_Publicas.{epub}"),

("Código de Expropiación Forzosa", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=118_Codigo_de_Expropiacion_Forzosa.{epub}"),

("Transparencia y Buen Gobierno", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=331_Transparencia_y_Buen_Gobierno.{epub}"),

("Código del Turismo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=325_Codigo_del_Turismo.{epub}"),

("Código de Fundaciones", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=338_Codigo_de_Fundaciones.{epub}"),

]

urls3 = [

#Función Pública


("Código de la Funcion Publica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=003_Codigo_de_la_Funcion_Publica.{epub}"),

("Código de la Función Pública Normativa Autonómica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=124_Codigo_de_la_Funcion_Publica_Normativa_Autonomica.{epub}"),

("Funcionarios de la Administración de Justicia", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=135_Funcionarios_de_la_Administracion_de_Justicia.{epub}"),

("Código de MUFACE, ISFAS y MUGEJU", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=011_Codigo_de_MUFACE_ISFAS_y_MUGEJU.{epub}"),

]

urls4 = [
#Seguridad Vial, Transporte y Telecomunicaciones

("Código de Tráfico", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=020_Codigo_de_Trafico_y_Seguridad_Vial.{epub}"),

("Código de las Telecomunicaciones", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=110_Codigo_de_las_Telecomunicaciones.{epub}"),

("Código de Derecho Audiovisual", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=168_Codigo_de_Derecho_Audiovisual.{epub}"),

("Código de Dercho de la Navegación", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=108_Codigo_de_Derecho_de_la_Navegacion_Maritima_y_Aerea.{epub}"),

("Código de Legislacion Aeroportuaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=256_Codigo_de_Legislacion_Aeroportuaria.{epub}"),

("Código de Legislacion Ferroviaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=120_Codigo_de_Legislacion_Ferroviaria.{epub}"),


]

urls5 =[


#Defensa y Seguridad


("Codigo de leyes administrativas de la Defensa", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=002_Codigo_de_leyes_administrativas_de_la_Defensa.{epub}"),

("Código de la Guardia Civil", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=007_Codigo_de_la_Guardia_Civil.{epub}"),

("Código de la Policia Nacional", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=018_Codigo_de_la_Policia_Nacional.{epub}"),

("Código de la Policia Local", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=119_Codigo_de_la_Policia_Local.{epub}"),

("Código de Seguridad Privada", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=058_Codigo_de_Seguridad_Privada.{epub}"),

("Código de Seguridad Ciudadana", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=100_Codigo_de_Seguridad_Ciudadana.{epub}"),

("Código de Derecho de la Ciberseguridad", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=173_Codigo_de_Derecho_de_la_Ciberseguridad.{epub}"),

("Código de Violencia de Genero y Domestica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=200_Codigo_de_Violencia_de_Genero_y_Domestica_.{epub}"),

("Código de Proteccion Civil", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=174_Codigo_de_Proteccion_Civil.{epub}"),

("Armas y Explosivos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=336_Armas_y_Explosivos.{epub}"),

]

urls6 =[
#Tributario

("Código de Legislacion Tributaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=049_Codigo_de_Legislacion_Tributaria.{epub}"),

("Ley General Tributaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=030_Ley_General_Tributaria_y_sus_reglamentos.{epub}"),

("Impuesto sobre Sociedades", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=062_Impuesto_sobre_Sociedades.{epub}"),

("Impuesto sobre la Renta de las Personas Físicas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=064_Impuesto_sobre_la_Renta_de_las_Personas_Fisicas.{epub}"),

("Impuesto sobre Sucesiones y Donaciones", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=061_Impuesto_sobre_Sucesiones_y_Donaciones.{epub}"),

("Impuesto sobre el Valor Añadido", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=057_Impuesto_sobre_el_Valor_Anadido.{epub}"),

("Impuesto sobre transmisiones Patrimoniales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=065_Impuesto_sobre_Transmisiones_Patrimoniales_y_Actos_Juridicos_Documentados.{epub}"),

("Impuestos Especiales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=063_Impuestos_especiales.{epub}"),

("Tasas y Precios Publicos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=066_Tasas_y_Precios_Publicos.{epub}"),

("Código de Normativa Catastral", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=113_Codigo_de_Normativa_Catastral.{epub}"),

("Regimen Fiscal de los Trabajadores Autonomos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=288_Regimen_Fiscal_de_los_Trabajadores_Autonomos.{epub}"),

]
urls7 =[
#Financiero


("Código de Legislación Financiera", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=050_Codigo_de_Legislacion_Financiera.{epub}"),

("Código de Normativa Presupuestaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=163_Codigo_de_Normativa_Presupuestaria.{epub}"),

("Ley General Presupuestaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=033_Ley_General_Presupuestaria_y_normas_complementarias.{epub}"),

("Código de Legislación Tributaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=049_Codigo_de_Legislacion_Tributaria.{epub}"),

("Control del gasto en la Administración del Estado", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=112_Control_del_Gasto_de_la_Administracion_del_Estado.{epub}"),

("Control del gasto en las Haciendas Locales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=227_Control_del_Gasto_en_las_Haciendas_Locales.{epub}"),

]
#Faltan Mercantil,etc
urls8 =[

#Procesal

("Código de Legislación Procesal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=040_Codigo_de_Legislacion_Procesal.{epub}"),

("Código de Subastas Electrónicas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=162_Codigo_de_Subastas_Electronicas.{epub}"),

]

urls9 = [
#Penal

("Código Penal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=038_Codigo_Penal_y_legislacion_complementaria.{epub}"),

("Código Penitenciario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_{epub}.php?fich=054_Codigo_Penitenciario.{epub}"),



]

urls0 =(urls1 + urls2 + urls2 +  urls3 +  urls4 +  urls5 +  urls6 +  urls7 +  urls8 +  urls9)


if (categories == "1"):
    urls = urls1
elif (categories == "2"):
    urls = urls2
elif (categories == "3"):
    urls = urls3
elif (categories == "4"):
    urls = urls4
elif (categories == "5"):
    urls = urls5
elif (categories == "6"):
    urls = urls6
elif (categories == "7"):
    urls = urls7
elif (categories == "8"):
    urls = urls8
elif (categories == "9"):
    urls = urls9
elif (categories == "0"):
    urls = urls0
else:
    print("Please select a number between 1 and 9")
    sys.exit()


start = time()

for x in tqdm(urls):

    url_response (x)

print(f"Time to download: {time() - start}")