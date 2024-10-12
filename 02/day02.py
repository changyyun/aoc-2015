
def convert(s):
    return tuple(map(int, s.strip().split('x')))

with open('input', 'r') as f:
    lines = list(map(convert, f.readlines()))

# Part 1
total = 0
for (l, w, h) in lines:
    area = 2 * (l * w + w * h + h * l)
    area += min(l*w, w*h, h*l)
    total += area

print(total)

# Part 2
lines = list(map(sorted, lines))

total = 0
for (x, y, z) in lines:
    total += 2 * (x + y)
    total += x * y * z

print(total)
