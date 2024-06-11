def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


def main_count_vow():
    print("Hello, this program count vowels...")
    word = input("Please, write here the word that you want analyze: \n")
    result = count_vowels(word)
    print("The word : ", word, ", contains :", result)


if __name__ == "__main__":
    main_count_vow()
