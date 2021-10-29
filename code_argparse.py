import argparse
import sys

NUM_PARAMETROS_ENTRADA=3

PARAMS_VALIDOS=(("A","B","C"),          # VALORES PERMITIDOS PARA PARAM1
                ("AA","BB","CC"),       # VALORES PERMITIDOS PARA PARAM2   
                ("AAA","BBB","CCC"))    # VALORES PERMITIDOS PARA PARAM3

######################################################################################
# Validación de parámetros de entrada en el caso de que el script los necesite 
#######################################################################################
# Función para validar que los parámetros están dentro de los valores previstos
# Atención args.parametros es una lista y evidentemente los elementos empiezan por el orden 0 por eso restamos 1
def control_parametros(orden_parametro,lista_ok,lista_parametros_script):
    if (lista_parametros_script[orden_parametro-1] not in lista_ok):
            print("Error en parámetro ",orden_parametro," : ")  
            print(" --> Valores posibles:", lista_ok)
            print("RC = ",orden_parametro)
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
    if len(args.parametros) < NUM_PARAMETROS_ENTRADA: 
        print("Error : Mínimo se han de informar",NUM_PARAMETROS_ENTRADA,"parámetros")
        retcode = 66 
        print("RC = ",retcode)
        sys.exit(retcode)
    else: 
        for parametro in args.parametros:
            for i in range(len(PARAMS_VALIDOS)):
                control_parametros(i+1,PARAMS_VALIDOS[i],args.parametros)

######################################################################################
# PROGRAMA PRINCIPAL 
#######################################################################################
if NUM_PARAMETROS_ENTRADA == 0:
    print("AVISO : Script sin parámetros de entrada")
    pass
else: 
    print("AVISO : Script con",NUM_PARAMETROS_ENTRADA,"parámetros de entrada")
    validar_parametros_entrada()

    