'''
#####   Working with Files
URL: http://rosalind.info/problems/ini5/
'''
#funcao retorna texto com somente linhas impares do texto original
def evenLines(lines):
    evenText = ''
    for line in range(len(lines)):
        if (line+1) % 2 == 0:
            evenText = evenText + lines[line]
    return evenText

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDatasetAsLines, writeOutput
#usado para referenciar o arquivo
id = 'ini5'
#le dados para completar o exercicio
lines = readDatasetAsLines(id)

output = evenLines(lines)

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)