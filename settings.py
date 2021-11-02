# settings.py
import os
import getpass
import datetime
import socket
import logging

py_script = os.path.basename(__file__)

def init_config_log():
    logging.basicConfig(filename="fichero_de_logging.log", \
                    filemode='w', \
                    level=logging.DEBUG, \
                    format=' %(asctime)s -  %(levelname)s - %(message)s')

def init_settings():
    global usuario,    \
           path_base,  \
           hora,       \
           host,       \
           script
    usuario = getpass.getuser()
    path_base = os.getcwd()
    hora = datetime.datetime.now()
    host=socket.gethostname()
    script=os.path.basename(__file__)

def print_settings():
    print('----------------------------------------------------------------------------------------------------------')
    print(' Variables de entorno : ')
    print("--> Host :             ",host)
    print("--> Usuario :          ",usuario)
    print("--> Directorio :       ",path_base)
    print("--> Hora inicio :      ",hora)
    print("--> Script settings :  ",script)
    print('----------------------------------------------------------------------------------------------------------')
    
    logging.debug('----------------------------------------------------------------------------------------------------------')
    logging.debug(' Variables de entorno : ')
    logging.debug("--> Host :             "+ host)
    logging.debug("--> Usuario :          "+ usuario)
    logging.debug("--> Directorio :       "+ path_base)
    logging.debug("--> Hora inicio :      "+ str(hora))
    logging.debug("--> Script settings :  "+ script)
    logging.debug('----------------------------------------------------------------------------------------------------------')
