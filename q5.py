words=['apple','banana','apple','orange','banana','apple']
count={word:words.count(word) for word in set(words)}
print(count)