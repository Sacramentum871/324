import os
dict = {}
for i in range(1, 4):
    name = f'{i}.txt'
    current = os.getcwd()
    full_path = os.path.join(current, name)
    with open(full_path, 'r', encoding='utf-8') as f:
        dict[name] = [x for x in f.read().splitlines() if x]

with open('completed.txt', 'w', encoding='utf-8') as f:
    for k, v in sorted(dict.items(), key=lambda x: x[1]):
        f.write(k + '\n')
        f.write(str(len(v)) + '\n')
        f.write('\n'.join(v))
        f.write('\n')

