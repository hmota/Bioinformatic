import unittest
from dna import countNucleotides

dataset = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

expected = '20 12 17 21'

class Test_dna_Test(unittest.TestCase):
    def testCountNucleotides(self):
        output = countNucleotides(dataset)
        self.assertEquals(output, expected)

#if __name__ == '__main__':
#    unittest.main()
