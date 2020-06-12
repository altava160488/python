s = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
with open("text_4.txt", encoding="utf-8") as f_in, open('text_4_out.txt', 'w', encoding="utf-8") as f_out:
    for line in f_in:
        f_out.write(s[line.split()[0].lower()].title() + ' ' + ' '.join(line.split()[1:]) + '\n')
