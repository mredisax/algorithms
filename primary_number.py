def primary_number(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))

print(primary_number(3) == True)
print(primary_number(4) == False)
