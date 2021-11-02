#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import settings
import logging
import os

py_script= os.path.basename(__file__)


settings.init_settings()
settings.init_config_log()

settings.print_settings()

usuario     = settings.usuario
path_base   = settings.path_base
host        = settings.host
hora_inicio = settings.hora

######################################################################################
# Definición de niveles de criticidad de logging.
######################################################################################

def log_d(mensaje): logging.debug(f"{py_script} {mensaje}")
def log_i(mensaje): logging.info(f"{py_script} {mensaje}")
def log_w(mensaje): logging.warning(f"{py_script} {mensaje}")
def log_e(mensaje): logging.error(f"{py_script} {mensaje}")
def log_c(mensaje): logging.critical(f"{py_script} {mensaje}")

######################################################################################
# Validación de parámetros de entrada en el caso de que el script los necesite 
######################################################################################
NUM_PARAMS_ENTRADA=5
PARAMS_VALIDOS={"Nombre_parm_1 ": ("A","B","C"),          
                "Nombre_parm_2 ": ("AA","BB","CC"),       
                "Nombre_parm_3 ": ("AAA","BBB","CCC"),    
                "Nombre_parm_4 ": ("J","K"),              
                "Nombre_parm_5 ": ("B")}                  

if NUM_PARAMS_ENTRADA >0 :
    if (len(PARAMS_VALIDOS) != NUM_PARAMS_ENTRADA):
      print(f"ERROR. Numéro de parámetros validos inconsistente con posibles valores permitidos")
      log_e(f"ERROR. Numéro de parámetros validos inconsistente con posibles valores permitidos")
      sys.exit(8)

# Función para validar que los parámetros están dentro de los valores previstos
# Atención args.parametros es una lista y evidentemente los elementos empiezan por el orden 0 por eso restamos 1
def control_parametros(orden_parametro,key_lista_ok,lista_ok,lista_parametros_script):
    if (lista_parametros_script[orden_parametro-1] not in lista_ok):
            print(f"ERROR en parámetro {key_lista_ok}--> orden del parámetro / RC = {orden_parametro}")  
            print(f" --> Valores posibles:{lista_ok}")
            log_e(f"ERROR en parámetro {key_lista_ok}--> orden del parámetro / RC = {orden_parametro}")  
            log_e(f" --> Valores posibles: {lista_ok}")
            sys.exit(orden_parametro)
               

def validar_parametros_entrada():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('-v', '--version', action='version',
                        version='Versión del script %(prog)s : 1.0', help="Muestra la versión del programa.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Muestra este mensaje')
    parser.add_argument('parametros', type=str, nargs='+')

    args = parser.parse_args()
 
    # Controlamos que como mínimo hayan 3 parámetros, aunque solo validamos los tres primeros. 
    if len(args.parametros) < NUM_PARAMS_ENTRADA: 
        retcode = 66 
        print(f"Error : Mínimo se han de informar{NUM_PARAMS_ENTRADA}parámetros. RC = {retcode}")
        log_e(f"Error : Mínimo se han de informar{NUM_PARAMS_ENTRADA}parámetros. RC = {retcode}")
        sys.exit(retcode)
    else: 
        for parametro in args.parametros:
            # for i in range(len(PARAMS_VALIDOS)):
            for count,i in enumerate(PARAMS_VALIDOS):
                control_parametros(count+1,i,PARAMS_VALIDOS[i],args.parametros)
    parms_validados=[]
    resto_parametros=[]

    for count,i in enumerate(args.parametros):
        if count < NUM_PARAMS_ENTRADA:
            parms_validados.append(i)
        else:
            resto_parametros.append(i)
    
    return parms_validados,resto_parametros


######################################################################################
# PROGRAMA PRINCIPAL 
#######################################################################################


########## Validar parámetros de entrada al script.
if NUM_PARAMS_ENTRADA == 0:
    log_d("AVISO : Script sin parámetros de entrada")
    pass
else: 
    parms_val_ok,resto_parms=validar_parametros_entrada()
    log_d(" Validación correcta de parámetros de entrada")
    log_d("- Parámetros validados = "+str(parms_val_ok))
    log_d("- Parámetros no validados = "+str(resto_parms))


     