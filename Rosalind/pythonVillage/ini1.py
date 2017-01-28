'''
#####   Installing Python
URL: http://rosalind.info/problems/ini1/
'''
#minhas funcoes de leitura e escrita para nao repetir codigo a cada exercicio
from common import readDataset, writeOutput
#usado para referenciar o arquivo
id = 'ini1'

# transfere o poema do import this para variavel zen
import sys, cStringIO
zen = cStringIO.StringIO()
old_stdout = sys.stdout
sys.stdout = zen
# The Zen of Python
import this
sys.stdout = old_stdout

#escreve arquivo de saida para anexar resposta no site
writeOutput(id, zen.getvalue())