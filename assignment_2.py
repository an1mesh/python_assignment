def getSlicedArray(arr, startIndex, endIndex):
    if arr == []:
        return 'array was empty please give a non empty array'
    if len(arr) >= endIndex:
        ans = arr[startIndex:endIndex]
        return ans
    return 'Please give a list if length greater than or equal to end index'


def checkPalindrome(word):
    if word == '':
        return 'word was empty please provide a non empty word'
    reversedWord = word[::-1]
    if reversedWord == word:
        return 'Palindrome'
    return 'Not Palindrome'


def checkRepeatedCharacter(word):
    if word == '':
        return 'word was empty please provide a non empty word'
    wordSet = set()
    for i in word:
        if i in wordSet:
            return f'Contains repeated character - {i} in {word}'
        wordSet.add(i)
    return f'No repeated characters in {word}'


# Slice
print('---SLICING---')
print(getSlicedArray(arr=[1, 2, 3, 4, 5, 6], startIndex=1, endIndex=5))
print()

# Palindrome check
print('---PALINDROME CHECK---')
print(checkPalindrome(word='ab'))
print(checkPalindrome(word='abc'))
print(checkPalindrome(word='aba'))
print()

# Repeated characters check
print('---REPEATED CHARACTERS CHECK---')
print(checkRepeatedCharacter(word='aab'))
print(checkRepeatedCharacter(word='abc'))
print(checkRepeatedCharacter(word='def'))
print()
