
p = float(input("principal: "))
r = float(input("rate = "))
t = float(input("time = "))
ci = p * ((1 + r/100)**t) - p
print("compound interest = ",ci)
