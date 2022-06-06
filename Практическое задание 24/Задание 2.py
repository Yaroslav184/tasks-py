def palindrome(word):
    print('Это слово является полиндромом - YES') if word[0] == word[-1] else print('Это слово НЕ является полиндромом - NO')

palindrome(word=input('Введите слово состоящее из 3-х букв: '))