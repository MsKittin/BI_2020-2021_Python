from Bio.Seq import Seq  # for checking
from Bio.SeqUtils import GC  # for checking


class Rna:
    def __init__(self, seq) -> None:
        if isinstance(seq, str):
            for base in seq:
                if base not in ['A', 'U', 'G', 'C']:
                    raise ValueError("Unexpected base in sequence: {}".format(base))
            self.seq = seq
            self.current = 0
        else:
            raise TypeError('Sequence must be a string')

    def __repr__(self):
        return 'Rna(seq=%s)' % self.seq

    def __str__(self) -> str:
        return self.seq

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.seq):
            self.current += 1
            return self.seq[self.current - 1]
        raise StopIteration

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Rna) \
               and self.seq == o.seq

    def __hash__(self) -> int:
        return hash(tuple(self.seq))

    def gc_content(self) -> float:
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq) * 100

    def reverse_complement(self) -> str:
        complement = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A'}
        return "".join(complement[base] for base in self.seq[::-1])


class Dna:
    def __init__(self, seq) -> None:
        if isinstance(seq, str):
            for base in seq:
                if base not in ['A', 'T', 'G', 'C']:
                    raise ValueError("Unexpected base in sequence: {}".format(base))
            self.seq = seq
            self.current = 0
        else:
            raise TypeError('Sequence must be a string')

    def __repr__(self):
        return 'Dna(seq=%s)' % self.seq

    def __str__(self) -> str:
        return self.seq

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.seq):
            self.current += 1
            return self.seq[self.current - 1]
        raise StopIteration

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Dna) \
               and self.seq == o.seq

    def __hash__(self) -> int:
        return hash(tuple(self.seq))

    def gc_content(self) -> float:
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq) * 100

    def reverse_complement(self) -> str:
        complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
        return "".join(complement[base] for base in self.seq[::-1])

    def transcribe(self) -> Rna:
        transcript = {'A': 'A', 'G': 'G', 'C': 'C', 'T': 'U'}
        return Rna("".join(transcript[base] for base in self.seq))


# Checking my implementation

if __name__ == '__main__':

    dna_seq = 'ATCGGAGTT'
    dna_seq2 = 'TACGCTTAC'
    rna_seq = 'AUUCGAU'

    print("My result of ATCGGAGTT reverse_complement: {}".format(Dna(dna_seq).reverse_complement()))
    print("Bio package result of ATCGGAGTT reverse_complement: {}".format(Seq(dna_seq).reverse_complement()))
    print("My result of AUUCGAU reverse_complement: {}".format(Rna(rna_seq).reverse_complement()))
    print("Bio package result of AUUCGAU reverse_complement: {}".format(Seq(rna_seq).reverse_complement_rna()))

    print("\nMy result of ATCGGAGTT transcribe: {}".format(Dna(dna_seq).transcribe()))
    print("Bio package result of ATCGGAGTT transcribe: {}".format(Seq(dna_seq).transcribe()))
    res_transcript = Dna(dna_seq).transcribe()
    print("Type of my resulting transcript: {}".format(type(res_transcript)))

    print("\nMy result of ATCGGAGTT gc_content: {}".format(Dna(dna_seq).gc_content()))
    print("Bio package result of ATCGGAGTT gc_content: {}".format(GC(dna_seq)))

    print("\nIf ATCGGAGTT is equal to ATCGGAGTT: {}".format(Dna(dna_seq) == Dna(dna_seq)))
    print("If ATCGGAGTT is equal to TACGCTTAC: {}".format(Dna(dna_seq) == Dna(dna_seq2)))
    print("If GCGGC (Rna) is equal to GCGGC (Rna): {}".format(Rna('GCGGC') == Rna('GCGGC')))
    print("If GCGGC (Rna) is equal to GCGGC (Dna): {}".format(Dna('GCGGC') == Rna('GCGGC')))

    print("\nIteration over ATCGGAGTT sequence:")
    for letter in Dna(dna_seq):
        print(letter)

    print("\nIteration over AUUCGAU sequence:")
    for letter in Rna(rna_seq):
        print(letter)
