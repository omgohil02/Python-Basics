# Vowel and Consonant Analyzer in python 

words = []
vowels_set = {'a', 'e', 'i', 'o', 'u'}

print("Enter 5 words:\n")

for i in range(1, 6):
    while True:
        word = input(f"Word {i}: ").strip()
        if word.isalpha():
            words.append(word.lower())
            break
        else:
            print("Invalid input. Please enter alphabetic characters only.\n")

# Sort words alphabetically
words.sort()

print("\nWords in alphabetical order:")
print(words)

print("Word-wise analysis:")
total_vowels = 0
total_consonants = 0

for word in words:
    v_count = sum(1 for char in word if char in vowels_set)
    c_count = len(word) - v_count
    
    total_vowels += v_count
    total_consonants += c_count
    
    print(f"{word}\tVowels: {v_count}, Consonants: {c_count}")

print(f"Total vowels: {total_vowels}")
print(f"Total consonants: {total_consonants}")