def hamming_metric(father, child):
    distance = 0
    for c in zip(child, father):
        cn, fn = c
        if cn != fn:
            distance += 1

    return distance

def dna_check_results(first, second, child):
    first_distance = hamming_metric(first_dna, child_dna)
    second_distance = hamming_metric(second_dna, child_dna)
    if first_distance > second_distance:
        return 'Second candidate is a father'
    elif first_distance == second_distance:
        return "Error - someone is cheating"
    else:
        return 'First candidate is a father'

if __name__ == "__main__":
    first_dna = input("1st candidate DNA: ")
    second_dna = input("2nd candidate DNA: ")
    child_dna = input('child\'s  DNA: ')
    print(dna_check_results(first_dna, second_dna, child_dna))