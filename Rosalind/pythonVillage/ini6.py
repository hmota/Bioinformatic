'''
#####   Dictionaries
URL: http://rosalind.info/problems/ini6/
'''
#funcao retorna contagem de repeticoes de cada palavra
def countWords(text):
    words = text.split()
    dict={} 
    for word in words:
        dict[word]=words.count(word)
    return dict

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'ini6'
#le dados para completar o exercicio
data = readDataset(id)

dict = countWords(data)

output = ''

for word, count in dict.items():
    output = output+(word + ' ' + str(count) + '\n')

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)