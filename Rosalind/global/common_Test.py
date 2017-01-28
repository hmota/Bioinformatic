import unittest
from common import *

class Test_common_Test(unittest.TestCase):  
    def testReadDataset(self):
        fileID = 'test1'
        expected = '100 200'
        output = readDataset(fileID) 
        self.assertEqual(output, expected)

    def testReadDatasetAsLines(self):
        fileID = 'test2'
        output = readDatasetAsLines(fileID)
        expected = ['line one\n', 'line two\n', 'line three\n', 'line four']
        self.assertEquals(output, expected)

    def testWriteOutput(self):
        fileID = 'test3'
        writeOutput(fileID, 'ok')
        expected = 'ok'
        currentFolder = os.getcwd()
        with open(currentFolder+'/output/rosalind_'+fileID+'_output.txt', 'r') as f:
            output = f.read()
        f.closed
        self.assertEquals(output, expected)

if __name__ == '__main__':
    unittest.main()