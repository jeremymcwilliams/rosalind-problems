class Hamming:

    def __init__(self, seq1, seq2):
        self.seq1=seq1
        self.seq2=seq2
        seqLen1=len(seq1)
        seqLen2=len(seq2)
        if (seqLen1==seqLen2):
            self.seqLen=seqLen1
        else:
            self.seqLen=false

    def compare(self):
        hdist=0;
        #print(self.seqLen)
        for x in range(self.seqLen-1):
            if (self.seq1[x] != self.seq2[x]):
                hdist+=1

        return hdist





if __name__ == '__main__':

    seq1="TGGGCCTATAGCTTGTTCGCAGAACATTTGGTAAGAATATAACGGCGCTTCAGCATAATGCTCAACCGGCCGTCAATACTGCGAGGGCACCCTTTGGCGATAGGCCCTCGTTCACGTAATAGAACATTTGCGGGAAGCTCCTCCTGTAATCCGTCATGTTAGTAGCACTTCTCCCTGTATGGGGGGATCGTTCTTTCCCAACGCTTATGCTACCCTTATAAATGTCCGCCCCCACAGCATGAAGTGTTATACGCGACCGGAGCTGATAACAAAAGCTTTGGCACGCACAACCTGGTTAGGGAAGTCGGCGTTATGGCGTTTAACACCATGGGCGGCTAAGCCGTCTCACTGGCAAGATACATAAACCGCAATGCATTCTCTAAGGGAGAGTCATTGGGGATTGAGCACTTCCAGATTAACGGTCTCTGTGCTTCCGTTATCATAGCCGGTATCTTGTTATCGCCAACAGTCGTCTGTCCGACAATAATTTACTTGTGTCGTAAGTGTCATTTGAAGCTAAAGTTAATAGGCCGACGATGAGAAACTTACCCAGGCTATTAAAAAGCGCTATAATCGTACAACTTAAGCAACTTCGTGAGCCCATAGGCCTTCGGACAGAGCCACCAGCCATATGTACGCAAGCTTTTCTAAGTTACGGCCTTGAATTAACCCTACGAGGATCATGAAAGTCGACGACTAGAACGTGTACTCCCTGGGATCCTGATGCTTTGCTTAAATAAGCAAGACCGGCAGTGTGCGGTCCACGGTTCATAGGATATACAACGCGGGCAGGCGACCGGGGGATTGGGTACGTGGCCAAGGTTCTTGGCTGTCATCCTGCTAAAAAGTCCATGCCTATAGGGAAGCCTCGCATCGTTGGGTGAGGTCAACCGCGTGCAGAGTGACGGCACTTGCGGGCTCACTATAATCAGTTAGGCGCAAATAGACTCTTTAAGTCCATACCGTGATGATCAAAGGGTATTACGAGTA";
    seq2="TGGGCCTGTAACTTCTCCGGAGTCCCATTTGTAATCATGTAACTGGACATGGACGTAACTCCCAACAGGATGCCCAGACGATGGAAATACCGTATAGGGACAGGCCCTACTGAAAGTAACAAAACATTTGCGAAACGTGTTCCATGAATTTGGTCACTGAAGTGCCGGCGCGCCCGGCTAGCGCCCAAGTTATTAAACACTCGATTTGGCCCTGGTTATCGATGGAAAGGACCCTTTGGGGAGGTGAAATCCGGGACTATAACTACCATATAAGATCCTGTCACGACCACACTAGCTATCAAAGTCGGCATTGCTGCCACGAGCCCCTGGAGCCGCGAGGACCTCACACTTCCAAAAAAAACAAACAGCAATGCCCTCTCTGAGGCAGAATCATAGAACAAACAGTAAGGCCAGACTATCTTATGTACCTCTTCCGTTTCCGTTACCTTTGTCTTGCTATTGGGCCACGTCGTCTGTCCCACGAGCGGAGTCTGTAGTTGCAACTGGCTATATGAGACAAAGGTAGACGTCCGGTTATCACCAATGTTCCATGGAAAGCACAGTCCCCACTGAACGAACATTTTCTGCGACTTGCAGCTAGCGTAGACGTTCCTTCAGCCCCAACCGCGCCTAGTAGAAGAGTTCTCCTCTGATTCGGGGTTTATCTCCTAAAATGTGGTTAATGACTTCCGAAAGCTAACTTATCTACTGGAAGGAGGCCTGTTTCTTTGCATAGGTGTGCTCGACGAGCCATATTGTCCTGACTAATGATAGGCGATTTACTATGGGTGGTAGTCTGCCCGCAGATGGACTTGGCGAAAGGTGGTCCCAATCGTCCCTCTAATAACTCAATAGCCAGTGATAAGCGTCGCATAGCAGGGAGTCTTGAACGCCAGACCGAGTGAAAAGAGATGCCCCCCCACACTATTCAGACACTGGCAAGTTGACTGCCTAATTCTGGACCAATATTCATATATGGCGATTCGTGTA";

    hamm=Hamming(seq1, seq2)
    hdist=hamm.compare()
    print(hdist)