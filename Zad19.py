def check_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

string1 = "listen"
string2 = "silent"
if check_anagrams(string1, string2):
    print("Podane stringi są anagramami.")
else:
    print("Podane stringi nie są anagramami.")
