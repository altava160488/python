import json

i, s, r = 0, 0, {}
with open('text_7.txt', 'r', encoding='utf-8') as f_in, open('text_77.txt', 'w', encoding='utf-8') as f_out:
    for line in f_in:
        l = line.split()
        p = float(l[2]) - float(l[3])
        s += (p if p > 0 else 0)
        i += (1 if p > 0 else 0)
        r[l[0]] = p
    json.dump([r, {"average_profit": s / i}], f_out, ensure_ascii=False)