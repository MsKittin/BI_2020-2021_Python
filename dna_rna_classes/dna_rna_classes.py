class Rna:
    def __init__(self, seq) -> None:
        if isinstance(seq, str):
            if not seq:
                raise ValueError("Empty sequence received")

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
            if not seq:
                raise ValueError("Empty sequence received")

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
