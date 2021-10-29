import argparse
import sys

#######################################################################################
# Gestión de una lista variable de parámetros de entrada:
#######################################################################################
#Captura de parámetros con argparse

NUM_PARAMETROS_ENTRADA=0

# Función para validar que los parámetros están dentro de los valores previstos
# Atención args.parametros es una lista y evidentemente los elementos empiezan por el orden 0 por eso restamos 1
def control_parametros(orden_parametro,lista_ok):
    if (args.parametros[orden_parametro-1] not in lista_ok):
            print("Error en parámetro ",orden_parametro," : ")  
            print(" --> Valores posibles:", lista_ok)
            print("RC = ",orden_parametro)
            sys.exit(orden_parametro)

if NUM_PARAMETROS_ENTRADA == 0:
    print("soy un script sin parámetros de entrada")
    pass
else: 
    print("soy un script con parámetros de entrada")
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('-v', '--version', action='version',
                        version='Versión del script %(prog)s : 1.0', help="Muestra la versión del programa.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Muestra este mensaje')
    parser.add_argument('parametros', type=str, nargs='+')

    args = parser.parse_args()
    # Listas de valores válidos para los parámetros 

    param_1_valido=("A","B","C")
    param_2_valido=("AA","BB","CC")
    param_3_valido=("AAA","BBB","CCC")

    # Controlamos que como mínimo hayan 3 parámetros, aunque solo validamos los tres primeros. 
    if len(args.parametros) < NUM_PARAMETROS_ENTRADA: 
        print("Error : Mínimo se han de informar",NUM_PARAMETROS_ENTRADA,"parámetros")
        retcode = 66 
        print("RC = ",retcode)
        sys.exit(retcode)
    else: 
        for parametro in args.parametros:
            control_parametros(1,param_1_valido)
            control_parametros(2,param_2_valido)
            control_parametros(3,param_3_valido)
        

