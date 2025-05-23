def main():
    text = input("Please enter your text: ")

    l_count = letter_count(text)
    w_count = word_count(text)
    s_count = sentence_count(text)

    L = (l_count / w_count) * 100
    S = (s_count / w_count) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    final_index = round(index)

    if final_index >= 16:
        print("Grade 16+")
    elif final_index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {final_index}")


def letter_count(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def word_count(text):
    return len(text.split())


def sentence_count(text):
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count

main()
