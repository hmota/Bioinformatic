'''
#####   Conditions and Loops
URL: http://rosalind.info/problems/ini4/
'''
import unittest
#funcao retorna soma de todos impares de a-b
def sumOdd(num1, num2):
    sum = 0
    for i in range(num1, num2):
        if i % 2 != 0:
            sum += i
    return sum
        

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'ini4'
#le dados para completar o exercicio
data = readDataset(id)
#indices a-b
values = data.split()
output = sumOdd(int(values[0]), int(values[1]))

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)