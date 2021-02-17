exp=[2200,2350,2600,2130,2190]
new_exp= exp[1]-exp[0]
print("in feb the money spent extra was: ", new_exp)
print("expense for first quarter is: ", exp[1]+exp[0]+exp[2])
for i in exp:
    if i==2000:
        print("yes i did spent exactly 2000", end="")
    else:
        print("No, i did not spent exactly 2000")
exp.append(1980)
print(exp)
print("after refund april expense is :", exp[3]-20)