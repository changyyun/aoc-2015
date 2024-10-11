from collections import Counter

with open('input', 'r') as f:
    line = f.read().strip()

counts = Counter(line)

print(counts['('] - counts[')'])

floor = 0
for i, c in enumerate(line):
    floor += 1 if c == '(' else -1
    if floor < 0:
        print(i + 1)
        break

