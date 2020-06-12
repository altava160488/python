l = list(range(10))
with open('text_5.txt', 'w', encoding='utf-8') as f_obj:
    for i in l:
        f_obj.write(str(i) + ' ')

with open('text_5.txt', 'r', encoding='utf-8') as f_obj:
    r = []
    for line in f_obj:
        for i in line.split():
            r.append(int(i))
        print(line)
    print(sum(r))