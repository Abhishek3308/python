s="hello world from python"
rev=s[::-1]
print("reverse of string is:",rev)
r=""
for char in rev:
    if char not in r:
        r=r+char
print("string after removing duplicates:",r)
letter_count={}
for char in s:
    if char.isalpha():
        letter_count[char]=letter_count.get(char,0)+1
print("count :",letter_count)
