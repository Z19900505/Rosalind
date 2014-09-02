from nose.tools import *
import rosalind.iotools
import urllib

def parse_fasta_test():
    sequence = 'MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK'
    from_internet = urllib.urlopen('http://www.uniprot.org/uniprot/B5ZC00.fasta').read()
    assert_equals(rosalind.iotools.parse_fasta(from_internet)[1], sequence)

def read_fasta_test():
    fp = open('data/rosalind_cons.txt', 'r')
    fasta = rosalind.iotools.read_complete_fasta(fp)
    sequence = 'TAAACGCTCGATCTACCCTACCCCGCATGTCAAGTGCGTTCGTAAGAGTCCAACGTGGCTCACGCGGCGGGTTATCACTAGGACTTAGAAATAACAAAGCCGGAGCGCACGTCTGCGTAATTTGATCGCGGCGGGACCGAAACTATGAGAGAGCTTGGCAGCGGGCTATATGGATTTGACTAACATGATCCCACCGGCGATAGCGTTGACTTACAAAGCTCTCATGTCTTAAGCTCATGCTTGAGTATGTGCAACTGGAAAACTCTCCTGAGATGAAGCATAACTGCTTCCTCGTGTAACCCACATACGTACACTTACTACGCAAATATTCACTACAGAGTACAACACCGACTCGTGGTGGACTAGTAAGTTTGGTGACCTCCCGGGACAGACACAAGGCGTGCTCCCTCGTGAGACCTATCAGCCTGATCTTGCGTACATGGGCTACGGGAGCAGGAAAATACGCCTGATAGGCCAGCACCGGGGCTGCGTACGCAATTATAGTGAGGGGTAAGGTTTTGATGCTTTGCTCTCGTAGACACAATGGTGAATAATAATCTATGAACATAAAATTCGGAGATATTTACCTCTGTGGGGTGCGGGGGGGGCCGATTCTCCAATGTAGTCGCTAGATGATGTTGTAGTCGGGGCCAGGATTGGCTGATGTTCATCTATTGACCCTAGAGGTCGTCTCCAACTAGTGAAAACGGACAAGATGCGCAAGCAAGAGGCATAATGCGGTGTTTCTTTCTAGTGTCGAGATCTATCCACATACGGACGTAGCACAGATTGTAGTGTGGAGGGCGCAATCCTGAAATATCACCGCCCTAGACATCAATGACTCCGACATCCGGGAATAAAACAACGATTATGATCCCGATAGTCCGGGGCCAGATGATGGGGGCTGGAACATAAGCAACTCCATTTGGCACCTTGACGGTCGCTATATCTGCCCCTGGTATATAAGTCTATCGTTAATCCAAACCGATGCT'
    assert_equals(sequence, fasta[1][1])
