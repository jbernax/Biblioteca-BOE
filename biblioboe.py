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
1. Constitucional
2. Administrativo General
3. Función Pública
4. Seguridad Vial, Transporte y Telecomunicaciones
5. Defensa
6. Tributario
7. Financiero
8. Procesal
9. Penal
10. Civil 
11. Mercantil
12. Sociedades
13. Mercado Bancario
14. Auditoría y Contabilidad
15. Legislación Social
16. Sanidad
17. Deporte 
18. Cultura
19. Energía
20. Agrario
21. Comunidades Autónomas
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





#Civil
urls10 = [


("Código de Responsabilidad Civil y Seguro en la Circulacion de Vehiculos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=185_Codigo_de_Responsabilidad_Civil_y_Seguro_en_la_Circulacion_de_Vehiculos_a_Motor.epub"),

("Código Civil y Legislacion Complementaria", f"hthttps://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=034_Codigo_Civil_y_legislacion_complementaria.epub"),

("Código de Contratos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=319_Codigo_de_Contratos.epub"),

("Leyes Civiles Forales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=048_Leyes_Civiles_Forales.epub"),

("Código de Propiedad Intelectual", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=087_Codigo_de_Propiedad_Intelectual_.epub"),

("Código de Propiedad Horizontal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=015_Codigo_de_Propiedad_Horizontal.epub"),

("Código de Derecho Nobiliario. Títulos del Reino", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=342_Codigo_de_Derecho_Nobiliario_y_Elenco_de_Titulos_del_Reino.epub"),

("Código de Legislación Registral", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=129_Codigo_de_Legislacion_Registral_.epub"),

("Código de Legislación Notarial", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=144_Codigo_de_Legislacion_Notarial.epub"),

("Código de Derecho Matrimonial", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=261_Codigo_de_Derecho_Matrimonial.epub"),


]





#Mercantil
urls11 = [


("Código de Comercio y Legislación Complementaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=035_Codigo_de_Comercio_y_legislacion_complementaria.epub"),

("Código de Comercio Interior", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=097_Codigo_de_Comercio__Interior.epub"),

("Código de Legislacion Concursal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=083_Codigo_de_Legislacion_Concursal.epub"),

("Propiedad Industrial", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=067_Propiedad_Industrial.epub"),

("Código del Derecho de la Competencia", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=216_Codigo_de_Derecho_de_la_Competencia.epub"),

("Código de Derecho de la Publicidad", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=248_Codigo_de_Derecho_de_la_Publicidad.epub"),

("Código de la Moda", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=297_Codigo_de_la_Moda.epub"),

("Código del Consejero", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=318_Codigo_del_Consejero.epub"),

]


#Sociedades
urls12 = [


("Código de Derecho de Sociedades", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=106_Codigo_de_Derecho_de_Sociedades.epub"),

("Código de Economia Colaborativa", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=312_Codigo_de_Economia_Colaborativa.epub"),

("Legislacion de la Empresa Familiar", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=217_Legislacion_de_la_Empresa_Familiar.epub"),

("Código de Financiación Empresarial", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=141_Codigo_de_Financiacion_Empresarial.epub"),

("Código de Gobierno Corporativo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=213_Codigo_de_Gobierno_Corporativo.epub"),

("Código de Segunda Oportunidad", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=190_Codigo_de_Segunda_Oportunidad.epub"),

("Código de Inversiones Extranjeras en España", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=147_Codigo_de_Inversiones_Extranjeras_en_Espana.epub"),




]



#Mercado Bancario
urls13 = [


("Código del Mercado Bancario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=041_Codigo_del_Mercado_Bancario.epub"),

("Código del Mercado del Seguro", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=045_Codigo_del_Mercado_del_Seguro.epub"),

("Código del Mercado de Valores", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=076_Codigo_del_Mercado_de_Valores.epub"),

("Código Titulos y Valores", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=109_Codigo_de_Titulos_y_Valores.epub"),

("Código Cumplimiento Normativo en Entidades Financieras", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=214_Codigo_de_Cumplimiento_Normativo_en_Entidades_Financieras.epub"),

("Código de la Ordenacion de los Mercados Financieros", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=215_Codigo_de_la_Ordenacion_de_los_Mercados_Financieros.epub"),

("Código de las Entidades de los Mercados Financieros", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=242_Codigo_de_las_Entidades_de_los_Mercados_Financieros.epub"),

("Código de la Operativa de los Mercados Financieros", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=243_Codigo_de_la_Operativa_de_los_Mercados_Financieros.epub"),

("Código de Fiscalidad de los Mercados Financieros", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=244_Codigo_de_Fiscalidad_de_los_Mercados_Financieros.epub"),

("Código de Normativa Complementaria de los Mercados Financieros", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=245_Codigo_de_Normativa_Complementaria_de_los_Mercados_Financieros.epub"),


]


#Auditoría y Contabilidad
urls14 = [


("Código de Auditoria de Cuentas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=090_Codigo_de_Auditoria_de_Cuentas.epub"),

("Código de Contabilidad Financiera y Sociedades", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=089_Codigo_de_Contabilidad_Financiera_y_Sociedades.epub"),





#Legislacion Social
urls15 = [

("Código de Legislacion Social", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=039_Codigo_de_Legislacion_Social.epub"),

("Cooperativas Sociedades Laborales y Trabajador Autonomo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=071_Cooperativas_Sociedades_Laborales_y_Trabajador_Autonomo.epub"),

("Código Laboral y Seguridad Social", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=093_Codigo_Laboral_y_de_la_Seguridad_Social_.epub"),

("Prevención de Riesgos Laborales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=037_Prevencion_de_riesgos_laborales.epub"),

("Trabajo Autonomo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=267_Trabajo_Autonomo.epub"),



]


#Sanidad
urls16 = [

("Código Sanitario Normativa Autonomica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=212_Codigo_Sanitario_Normativa_Autonomica.epub"),

("Código del Sistema Sanitario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=088_Codigo_del_Sistema_Sanitario.epub"),

("Código del Sistema Sanitario Normativa Autonomica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=224_Codigo_del_Sistema_Sanitario_Normativa_Autonomica.epub"),

("Código de Profesionales Sanitarios", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=115_Codigo_de_Profesionales_Sanitarios.epub"),

("Código de Profesionales Sanitarios Normativa Autonomica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=193_Codigo_de_Profesionales_Sanitarios_Normativa_Autonomica.epub"),

("Código del Control Sanitario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=146_Codigo_del_Control_Sanitario.epub"),

("Código del Control Sanitario Normativa Autonómica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=225_Codigo_del_Control_Sanitario_Normativa_Autonomica.epub"),

("Código de Derecho Farmaceutico", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=081_Codigo_de_Derecho_Farmaceutico.epub"),

("Código Sanitario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=084_Codigo_Sanitario.epub"),


]



#Deporte
urls17 = [


("Código de Derecho Deportivo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=103_Codigo_de_Derecho_Deportivo_.epub"),



]




#CUltura

urls18 = [

("Código de las Artes Escenicas y Musica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=181_Codigo_de_las_Artes_Escenicas_y_de_la_Musica.epub"),

("Patrimonio Cultural de las Administraciones Publicas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=175_Patrimonio_Cultural_de_las_Administraciones_Publicas.epub"),

("Código de Museos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=177_Codigo_de_Museos__.epub"),

("Código de Archivos y Patrimonio Documental", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=092_Codigo_de_Archivos_y_Patrimonio_Documental.epub"),

("Código de Legislacion Bibliotecaria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=024_Codigo_de_Legislacion_Bibliotecaria.epub"),

("Código de Legislacion Bibliotecaria Autonómica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=134_Codigo_de_Legislacion_Bibliotecaria_Autonomica.epub"),

("Código de Cinematografia y Artes Visuales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=220_Codigo_de_Cinematografia_y_Artes_Audiovisuales.epub"),





]



#Energia
urls19 = [

("Código de la Energia Electrica", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=014_Codigo_de_la_Energia_Electrica.epub"),

("Código del Gas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=130_Codigo_del_Gas.epub"),

("Código del Petroleo", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=152_Codigo_del_Petroleo.epub"),

("Código de Seguridad Nuclear", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=219_Codigo_de_Seguridad_Nuclear.epub"),

("Reglamento para baja tensión e ITC", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=326_Reglamento_electrotecnico_para_baja_tension_e_ITC.epub"),



]





#Agrario

urls20 = [


("Código de Derecho Agrario I. Marco Institucional", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=287_Codigo_de_Derecho_Agrario_I_Marco_institucional_de_la_agricultura.epub"),

("Código de Derecho Agrario II. Empresario Agrario", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=296_Codigo_de_Derecho_Agrario_II_Empresario_agrario.epub"),

("Código de Derecho Agrario III. Propiedad y explotaciones agrarias", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=276_Codigo_de_Derecho_Agrario_III_Propiedad_y_explotaciones_agrarias.epub"),

("Código de Derecho Agrario IV. Variedades vegetales", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=192_Codigo_de_Derecho_Agrario_IV_Variedades_vegetales_.epub"),

("Código de Derecho Agrario V. Sanidad vegetal y productos fitosanitarios", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=284_Codigo_de_Derecho_Agrario_V_Sanidad_vegetal_y_productos_fitosanitarios_.epub"),

("Código de Derecho Agrario VI. Animales y explotaciones ganaderas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=293_Codigo_de_Derecho_Agrario_VI_Animales_y_explotaciones_ganaderas.epub"),

("Código de Derecho Agrario VII. Operaciones con el ganado", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=274_Codigo_de_Derecho_Agrario_VII_Operaciones_con_el_ganado.epub"),

("Código de Derecho Agrario VIII. Enfermedades del ganado", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=294_Codigo_de_Derecho_Agrario_VIII_Enfermedades_del_ganado_y_medicamentos.epub"),

("Código de Derecho Agrario IX. Sistema agroinustrial y calidad de productos.", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=277_Codigo_de_Derecho_Agrario_IX_Sistema_agroindustrial_y_calidad_de_los_productos_agrarios.epub"),

("Código de Derecho Agrario X. Desarrollo rural", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=114_Codigo_de_Derecho_Agrario_X_Desarrollo_rural_.epub"),

("Código de Derecho Agrario XI. Comunidades Autonomas", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=285_Codigo_de_Derecho_Agrario_XI_Comunidades_Autonomas_.epub"),

("Derecho Agroalimentario, Agroalimentacion", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=226_Derecho_Agroalimentario_Agroalimentacion_y_Normativa_de_Desarrollo.epub"),

("Derecho Agroalimentario, Operaciones de la Industria", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=228_Derecho_Agroalimentario_Operaciones_en_la_Industria_Agroalimentaria.epub"),

("Derecho Agroalimentario, Contexto social", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=247_Derecho_Agroalimentario_Contexto_Sectorial_de_la_Industria_Agroalimentaria.epub"),

("Código del Sector Hortofruticola", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=191_Codigo_del_Sector_Hortofruticola.epub"),

("Código del Sector Hortofruticola. Frutos Rojos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=340_Codigo_del_Sector_Hortofruticola_Frutos_Rojos.epub"),

("Código del Sector Vinitícola", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=218_Codigo_del_Sector_Vitivinicola.epub"),

("Código de la Cerveza", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=265_Codigo_de_la_Cerveza.epub"),

("Código de la Sidra", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=263_Codigo_de_la_Sidra.epub"),

("Código del Sector de Productos Lacteos", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=197_Codigo_del_Sector_de_Productos_Lacteos.epub"),

("Código del Sector del Aceite", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=290_Codigo_del_Sector_del_Aceite_.epub"),

("Código de Protección y Bienestar Animal", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=204_Codigo_de_Proteccion_y_Bienestar_Animal.epub"),

("Código de Animales de Compañia", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=210_Codigo_de_Animales_de_Compania.epub"),

("Código de Caza", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=095_Codigo_de_Caza.epub"),



]




#Comunidades Autonomas
urls21 = [

("Código de Leyes Civiles de Cataluña", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=150_Codigo_de_Leyes_Civiles_de_Cataluna.epub"),

("Código de Derecho Publico de Cataluña. General", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=167_Codigo_de_Derecho_Publico_de_Cataluna__Parte_general.epub"),

("Código de Derecho Publico de Cataluña. Especial.", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=201_Codigo_de_Derecho_Publico_de_Cataluna__Parte_especial.epub"),

("Código del Principado de Asturias", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=028_Codigo_del_Principado_de_Asturias.epub"),

("Código de la Comunidad de Madrid", f"https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=208_Codigo_de_la_Comunidad_de_Madrid.epub"),



]














urls0 =(urls1 + urls2 + urls2 +  urls3 +  urls4 +  urls5 +  urls6 +  urls7 +  urls8 +  urls9 + urls10 + urls11 +urls12 +urls13 +urls14 +urls15 +urls16 +urls17 +urls18 +urls19 +urls20 +urls21)


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
elif (categories == "10"):
    urls = urls10
elif (categories == "11"):
    urls = urls11
elif (categories == "12"):
    urls = urls12   
elif (categories == "13"):
    urls = urls13
elif (categories == "14"):
    urls = urls14
elif (categories == "15"):
    urls = urls15   
elif (categories == "16"):
    urls = urls16
elif (categories == "17"):
    urls = urls17
elif (categories == "18"):
    urls = urls18   
elif (categories == "19"):
    urls = urls19
elif (categories == "20"):
    urls = urls20
elif (categories == "21"):
    urls = urls21
elif (categories == "0"):
    urls = urls0
else:
    print("Please select a number between 0 and 21")
    sys.exit()


start = time()

for x in tqdm(urls):

    url_response (x)

print(f"Time to download: {time() - start}")