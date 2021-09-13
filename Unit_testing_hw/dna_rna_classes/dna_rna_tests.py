import unittest
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from dna_rna_classes import Dna, Rna


class DnaTest(unittest.TestCase):

    def test_dna_has_correct_seq_field(self):
        dna_sequence = Dna('ATGC')
        self.assertEqual('ATGC', dna_sequence.seq)

    def test_dna_seq_is_a_string(self):
        dna_sequence = Dna('ATGC')
        self.assertTrue(isinstance(dna_sequence.seq, str))

    def test_dna_raises_error_if_seq_is_not_a_string(self):
        with self.assertRaises(TypeError):
            Dna(12)

    def test_dna_raises_error_if_seq_is_empty(self):
        with self.assertRaises(ValueError):
            Dna('')

    def test_dna_seq_contains_correct_bases(self):
        dna_sequence = Dna('ATGC')
        self.assertTrue(base in ['A', 'T', 'G', 'C'] for base in dna_sequence.seq)

    def test_dna_raises_error_if_seq_contains_wrong_bases(self):
        with self.assertRaises(ValueError):
            Dna('ATGC3')

    def test_dna_equality(self):
        self.assertEqual(Dna('ATGC'), Dna('ATGC'))

    def test_dna_iterable(self):
        dna_sequence = Dna('ATGC')
        self.assertListEqual([base for base in dna_sequence.seq], ['A', 'T', 'G', 'C'])

    def test_dna_reverse_complement(self):
        """
        Testing if ours reverse_complement method implementation returns same result
        as Bio.Seq reverse_complement method
        """
        dna_sequence = Dna('ATGC')
        self.assertEqual(dna_sequence.reverse_complement(), Seq('ATGC').reverse_complement())

    def test_gc_content(self):
        """
        Testing if ours gc_content method implementation returns same result
        as Bio.SeqUtils GC function
        """
        dna_sequence = Dna('ATGC')
        self.assertEqual(dna_sequence.gc_content(), GC('ATGC'))

    def test_transcribe(self):
        """
        Testing if ours transcribe method implementation returns Rna class object
        and same result as Bio.Seq transcribe method
        """
        dna_sequence = Dna('ATGC')
        self.assertTrue(isinstance(dna_sequence.transcribe(), Rna))
        self.assertEqual(dna_sequence.transcribe().seq, Seq('ATGC').transcribe())


class RnaTest(unittest.TestCase):

    def test_rna_has_correct_seq_field(self):
        rna_sequence = Rna('AUGC')
        self.assertEqual('AUGC', rna_sequence.seq)

    def test_rna_seq_is_a_string(self):
        rna_sequence = Rna('AUGC')
        self.assertTrue(isinstance(rna_sequence.seq, str))

    def test_rna_raises_error_if_seq_is_not_a_string(self):
        with self.assertRaises(TypeError):
            Rna(12)

    def test_rna_raises_error_if_seq_is_empty(self):
        with self.assertRaises(ValueError):
            Rna('')

    def test_rna_seq_contains_correct_bases(self):
        rna_sequence = Rna('AUGC')
        self.assertTrue(base in ['A', 'U', 'G', 'C'] for base in rna_sequence.seq)

    def test_rna_raises_error_if_seq_contains_wrong_bases(self):
        with self.assertRaises(ValueError):
            Rna('AUGC3')

    def test_rna_equality(self):
        self.assertEqual(Rna('AUGC'), Rna('AUGC'))

    def test_rna_iterable(self):
        rna_sequence = Rna('AUGC')
        self.assertListEqual([base for base in rna_sequence.seq], ['A', 'U', 'G', 'C'])

    def test_rna_reverse_complement(self):
        """
        Testing if ours reverse_complement method implementation returns same result
        as Bio.Seq reverse_complement_rna method
        """
        rna_sequence = Rna('AUGC')
        self.assertEqual(rna_sequence.reverse_complement(), Seq('AUGC').reverse_complement_rna())

    def test_gc_content(self):
        """
        Testing if ours gc_content method implementation returns same result
        as Bio.SeqUtils GC function
        """
        rna_sequence = Rna('AUGC')
        self.assertEqual(rna_sequence.gc_content(), GC('AUGC'))


if __name__ == '__main__':
    unittest.main()
