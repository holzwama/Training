from collections import Counter
 
words = []

counts = Counter(words)
top_four = counts.most_common(4)
print(top_four)