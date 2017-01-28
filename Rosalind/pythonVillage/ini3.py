'''
#####   Strings and Lists
URL: http://rosalind.info/problems/ini3/
'''
#funcao retorna texto recortado entre os indices a-b c-d
def slice(data):
        values = data.split()
        #texto para recorte
        string = values[0]
        #texto recortado de acordo com indices passados
        return string[int(values[1]):1 + int(values[2])] +" "+ string[int(values[3]):1 + int(values[4])]


#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'ini3'
#le dados para completar o exercicio
data = readDataset(id)

output = slice(data)

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)
