import pandas as pd
from collections import Counter
train_df = pd.read_csv(r'train_set.csv', sep='\t')
test_df = pd.read_csv(r'test_a.csv', sep='\t')

all_lines = ' '.join(list(train_df['text']))
word_count = Counter(all_lines.split(" "))
word_count = sorted(word_count.items(), key=lambda d:d[1], reverse = True)

print(len(word_count))

print(word_count[0])

print(word_count[-1])