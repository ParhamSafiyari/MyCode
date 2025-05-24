import csv
import sys


def main():
    # Check for proper command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the database into a list of dictionaries
    with open(database_file, newline='') as db:
        reader = csv.DictReader(db)
        database = list(reader)
        str_keys = reader.fieldnames[1:]

    # Read the DNA sequence into a string
    with open(sequence_file, 'r') as seq_file:
        sequence = seq_file.read()

    # Find longest match of each STR in the DNA sequence
    str_counts = {}
    for STR in str_keys:
        str_counts[STR] = longest_match(sequence, STR)

    # Compare against each profile in the database
    for person in database:
        match = True
        for STR in str_keys:
            if int(person[STR]) != str_counts[STR]:
                match = False
                break
        if match:
            print(person['name'])
            return

    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
