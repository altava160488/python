time = int(input('Введите время в секундах:\n'))

ss = time % 60 % 60
mm = time // 60 % 60
hh = time // 60 // 60


v = '%02d:%02d:%02d'%(hh, mm, ss)
d = " -- '%02d:%02d:%02d'%(hh, mm, ss)\n"
print(v,d)

v = '%(h)02d:%(m)02d:%(s)02d'%dict(h = hh, m = mm, s = ss)
d = " -- '%(h)02d:%(m)02d:%(s)02d'%dict(h = hh, m = mm, s = ss)\n"
print(v,d)

v = '{0:02}:{1:02}:{2:02}'.format(hh, mm, ss)
d = " -- '{0:02}:{1:02}:{2:02}'.format(hh, mm, ss)\n"
print(v,d)

v = '{:02}:{:02}:{:02}'.format(hh, mm, ss)
d = " -- '{:02}:{:02}:{:02}'.format(hh, mm, ss)\n"
print(v,d)

v = '{:0>2}:{:0>2}:{:0>2}'.format(hh, mm, ss)
d = " -- '{:0>2}:{:0>2}:{:0>2}'.format(hh, mm, ss)\n"
print(v,d)

v = f'{hh:02}:{mm:02}:{ss:02}'
d = " -- f'{hh:02}:{mm:02}:{ss:02}'\n"
print(v,d)

v = f'{hh:02d}:{mm:02d}:{ss:02d}'
d = " -- f'{hh:02d}:{mm:02d}:{ss:02d}'\n"
print(v,d)


l = 2

v = '{0:0{3}}:{1:0{3}}:{2:0{3}}'.format(hh, mm, ss,l)
d = " -- '{0:0{3}}:{1:0{3}}:{2:0{3}}'.format(hh, mm, ss,l)\n"
print(v,d)

v = '{h:0{z}}:{m:0{z}}:{s:0{z}}'.format(h = hh, m = mm, s = ss, z = l)
d = " -- '{h:0{z}}:{m:0{z}}:{s:0{z}}'.format(h = hh, m = mm, s = ss, z = l)\n"
print(v,d)


input('Для выхода нажмите любую клавишу..')


