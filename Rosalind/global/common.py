import sys
import os

def readDataset(id):
    currentFolder = os.getcwd()
    with open(currentFolder+'/dataset/rosalind_'+id+'.txt', 'r') as f:
        data = f.read()
    f.closed
    return data

def writeOutput(id, output):
    currentFolder = os.getcwd()
    with open(currentFolder+'/output/rosalind_'+id+'_output.txt', 'w+') as f:
        f.write(str(output))
    f.closed
    print '##### output '+id+' #####\n\n'
    print output
    print '\n\n##### completed #####\n\n'