string =input("Enter a word: ")

vowel_count=sum(1 for char in string if char.lower() in "aeiou")

print("{} vowels prsesnt".format(vowel_count))