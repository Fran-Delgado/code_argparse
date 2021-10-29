# settings.py
import os
import getpass
import datetime
import socket

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
