'''
#####   Counting DNA Nucleotides
URL: http://rosalind.info/problems/ini1/
'''

id = 'dna'
file = open('./rosalind_'+id+'.txt', 'r')
string = file.read()

print qt(string)

def qt(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")