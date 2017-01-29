'''
#####   Counting DNA Nucleotides
URL: http://rosalind.info/problems/dna/
'''
#funcao retorna contagem de nucleotideos da cadeia(s=String) de dna
def countNucleotides(s):
      return str(s.count('A')) +" "+ str(s.count('C')) +" "+ str(s.count('G')) +" "+ str(s.count('T'))

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'dna'
#le dados para completar o exercicio
data = readDataset(id)

output = countNucleotides(data)

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)