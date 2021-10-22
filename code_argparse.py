import argparse
import sys
#######################################################################################
# Gestión de una lista variable de parámetros de entrada:
#######################################################################################
#Captura de parámetros con argparse
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-v', '--version', action='version',
                    version='Versión del script %(prog)s : 1.0', help="Muestra la versión del programa.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Muestra este mensaje')
parser.add_argument('parametros', type=str, nargs='+')

args = parser.parse_args()

# Función para validar que los parámetros están dentro de los valores previstos
def control_parametros(orden_lista,lista_ok):
    if (args.parametros[orden_lista] not in lista_ok):
            print("Error en parámetro ",orden_lista+1," : ")  
            print(" --> Valores posibles:", lista_ok)
            print("RC = ",orden_lista+1)
            sys.exit(orden_lista+1)

# Listas de valores válidos para los parámetros 
param_1_valido=("A","B","C")
param_2_valido=("AA","BB","CC")
param_3_valido=("AAA","BBB","CCC")

# Controlamos que como mínimo hayan 3 parámetros, aunque solo validamos los tres primeros. 
if len(args.parametros) < 3: 
    print("Error : Mínimo se han de informar 3 parámetros")
    retcode = 66 
    print("RC = ",retcode)
    sys.exit(retcode)
else: 
    for parametro in args.parametros:
        control_parametros(0,param_1_valido)
        control_parametros(1,param_2_valido)
        control_parametros(2,param_3_valido)
        

