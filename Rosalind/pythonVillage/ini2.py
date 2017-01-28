'''
#####   Variables and Some Arithmetic 
URL: http://rosalind.info/problems/ini2/
'''
#funcao retorna quadrado da hipotenusa de ab
def square(data):
	array = data.split()
	return int(array[0])**2 + int(array[1])**2

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'ini2'
#le dados para completar o exercicio
data = readDataset(id)

output = square(data)

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)
