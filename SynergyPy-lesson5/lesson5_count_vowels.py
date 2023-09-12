word = input("Введите слово: ")

vowels = "aeiou" 

count_vowels = 0
count_consonants = 0

for char in word:
    if char in vowels:
        count_vowels += 1
    else:
        count_consonants += 1
        
print("Количество гласных букв:", count_vowels)
print("Количество согласных букв:", count_consonants)
