def hamming_metric(father, child):
    distance = 0
    for c in zip(child, father):
        cn, fn = c
        if cn != fn:
            distance += 1

    return distance

if __name__ == "__main__":
    first_dna = input("1st candidate DNA: ")
    second_dna = input("2nd candidate DNA: ")
    child_dna = input('child\'s  DNA: ')

    first_distance = hamming_metric(first_dna, child_dna)
    second_distance = hamming_metric(second_dna, child_dna)
    if first_distance > second_distance:
        print('Second candidate is a father')
    elif first_distance == second_distance:
        print("Error - someone is cheating")
    else:
        print('First candidate is a father')