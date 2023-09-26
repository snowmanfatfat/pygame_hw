def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq)

seq50 = 'GGAACCTT'
print(gc_content(seq50))

seq75 = 'GCGCGCATTA'
print(gc_content(seq75))

seq60 = 'AGCAGCCGCT'
print(gc_content(seq60))
