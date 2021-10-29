import sys, getopt

opcion = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"ho:",["opcion="])
    # print(opts)
    # print(args)
except getopt.GetoptError:
    print('parms.py -o <opcion>' )
    sys.exit(1)

for opt, arg in opts:
    if opt == '-h':
        print('parms.py -o <opcion>')
        sys.exit()
    elif opt in ("-o", "--opcion"):
        opcion = arg
    
print('Opción de trabajo: "', opcion)
