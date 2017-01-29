import unittest
from rna import transcriptDnaToRna

dataset = 'GATGGAACTTGACTACGTAAATT'

expected = 'GAUGGAACUUGACUACGUAAAUU'

class Test_dna_Test(unittest.TestCase):
    def testTranscriptDnaToRna(self):
        output = transcriptDnaToRna(dataset)
        self.assertEquals(output, expected)

#if __name__ == '__main__':
#    unittest.main()
