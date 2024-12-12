def isAnagram(s1,s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

def obtain_the_strings():
    while True:
        s1 = input('Please input the first string: ')
        if s1.isalpha():
            s2 = input('Please enter the second string: ')
            if s2.isalpha():
                return s1,s2
            else:
                print('invalid input')
        else:
            print('invalid input')
        
s1,s2 = obtain_the_strings()
if (isAnagram(s1,s2)):
    print('is an anagram')
else:
    print('is not an anagram')