def find_missing(sequence):
    razon = 0
    for i in range(len(sequence)):
        analisis1 = sequence[i + 1] - sequence[i]
        analisis2 = sequence[i + 2] - sequence[i + 1]
        if analisis1 == analisis2:
            razon = analisis1
            break
    #print(razon)
    for i in range(len(sequence)):
        if sequence[i] + razon == sequence[i + 1]:
            continue
        else:
            sequence.append(sequence[i] + razon)
            break
            
    return sequence[-1]

def find_missing2(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

print(find_missing2([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing2([1, 3, 4, 5, 6, 7, 8, 9]))