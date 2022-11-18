import main
import argparse
from celery import Celery

parser = argparse.ArgumentParser(description=" -f Directorio, -c Funcion a ingresar: raiz, pot, log")

parser.add_argument("-f", "--inputfile", type=str, required=True, help="string")
parser.add_argument("-c", "--calc", type=str, required=True, help="string")

global args
args = parser.parse_args()

print('File: %s' % args.inputfile)
print('Command: %s' % args.calc)

print(main.funcion_calculo.delay(args.inputfile, args.calc).result)