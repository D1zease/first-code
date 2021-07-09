total1 = 0 # these totals are 0
total2 = 0 # since it will add one number to the int.


# adds all the numer inside the list.
for element in range(1,6):
    total1 += el 
    
for element1 in range(1,6):
    total2 += el1
    

def test(totaltest1, totaltest2):
    # vary to an argument that will add both the equal of the list.
    
    # so total1 + total2
    a = totaltest1 + totaltest2
    
    # if the variable a is less than 50. it prints by saying the integer is small.
    if a < 50:
        return "The integer is small"
    # an else statement if the int is bigger than 50 or equal to 50.
    else:
        return "The integer is so big.."
        


result = test(total1, total2) # result to tell if the int is over at 50 or not.
add = total1 + total2 # adds the tot

print(f"Result: {result}")
print(f"Int: {add}")

