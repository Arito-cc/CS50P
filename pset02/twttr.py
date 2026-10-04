twitter = input("Input: ")
twttr = ""
vowel = ['a','e','i','o','u','A','E','I','O','U']

for c in twitter:
    if c not in vowel:
        twttr += c

print(f"Output: {twttr}")


