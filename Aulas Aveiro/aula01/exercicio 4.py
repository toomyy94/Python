s = int(input("Segundos: "))
h = int(s/3600)
m = int((s/60)%60)
s = s%60
print("{:02d}:{:02d}:{:02d}".format(h, m, s))
