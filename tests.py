import unittest

from pydna import seq_utils

class TestSeqUtils(unittest.TestCase):
	def test_is_codon_correct(self):
	    codon = 'ATG'
	    result = seq_utils.is_codon_correct(codon)
	    expected = True
	    self.assertEqual(expected, result)
