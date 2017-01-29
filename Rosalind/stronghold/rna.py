'''
#####   Transcribing DNA into RNA
URL: http://rosalind.info/problems/rna/
'''
#funcao retorna contagem de nucleotideos da cadeia(s=String) de dna
def transcriptDnaToRna(s):
      return s.replace('T', 'U')

#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'rna'
#le dados para completar o exercicio
data = readDataset(id)

output = transcriptDnaToRna(data)

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, output)