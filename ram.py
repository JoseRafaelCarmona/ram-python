# PRORAMA OARA SABER LA RAM OCUPADA POR LA COMPUTADORA
from subprocess import Popen, PIPE, STDOUT

def salidaComando(comando):
	event = Popen(comando, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	output = event.communicate()
	salida = output[0].decode('utf-8')
	return salida

ramTotal = int(salidaComando('vmstat -s | grep "total memory"')[:-16])/100000
ramOCupada = int(salidaComando('vmstat -s | grep "used memory"')[:-16])/10000
ocupado = (ramOCupada * 100)/ramTotal
print("Total: {0}".format(int(ramTotal)))
print("ramOCupado: {0}".format(int(ramOCupada)))
print("Porcentaje ocupado: {0}%	".format(int(ocupado)))
