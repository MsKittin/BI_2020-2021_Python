import itertools
from Bio.Seq import Seq

'''
Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n (аккуратно, не вызывайте её с n > 8)
Пример вызова
list(generate(2))
['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']
'''


def generate(n):

    for i in range(1, n + 1):
        comb = itertools.product(['A', 'T', 'G', 'C'], repeat=i)
        for j in comb:
            yield "".join(j)


print(list(generate(7)))


'''
Напишите генератор, осуществляющий считывание фасты и возвращающий по 1-ой оттранслированной последовательности 
(используйте биопитон)

Принимаемые аргументы функции:
    путь до фасты
    таблица кодонов - 'Standard' по умолчанию
Аутпут:
    протеиновый Seq
'''


def translate_seq(path_to_file, codon_table="Standard"):

    with open(path_to_file, 'r') as fasta_file:
        temp_fasta = [line.rstrip("\n") for line in fasta_file]

    fasta_list = temp_fasta[1::2]

    num = 0
    while num <= len(fasta_list) - 1:
        yield Seq(fasta_list[num]).translate(table=codon_table)
        num += 1


path_to_fasta = "/home/misskittin/Downloads/sample.fa"

transcript = translate_seq(path_to_fasta, codon_table="Standard")
print(next(transcript))
print(next(transcript))
print(next(transcript))
print(next(transcript))
print(next(transcript))

