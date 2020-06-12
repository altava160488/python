r = {}
with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        l = line.replace('(пр)', '').replace('(лаб)','').replace('(л)', '').replace('-', '')
        k = l[:l.index(':')]
        v = 0
        for i in l[l.index(':') + 1:].split():
            v += int(i)
        r[k] = v
print(r)