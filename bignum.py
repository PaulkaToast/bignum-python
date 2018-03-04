"""
Bignum

We representing a number as a list of digits
where the least significant digit is in the 0 position,
while the most significant digit is in the nth position.

We are only concerning ourselves with unsigned numbers 
with this implentation.

Examples:
0 = [0]
123 = [3, 2, 1]
"""
def numToBigNum( n ):
    result = []
    if n == 0:
        return [0]
    while n != 0:
        result.append(n % 10)
        n = n // 10
    return result

"""
Multiplication is just repeated addition
using that concept, we can re-use our implentation
of bigAdd. 
"""
def bigMul( n1, n2 ):
    #Multiplying with zero results in zero, shortcut to return [0]
    if n1 == [0] or n2 == [0]:
        return [0]
    
    result = [0]
    counter = [0]
    #Add n1 to itself until counter reaches n2
    while counter != n2:
        result = bigAdd(result, n1)
        counter = bigAdd(counter, [1])
    return result

"""
We combine Mod and Div into one function 
since their implentation is identical, the
only difference is what is returned at the end

Integer division is repeated subtration, so
we reused the bigSub function.
"""
def bigDivMod( n1, n2 , isDiv = True ):
    #Division by zero
    if n2 == [0]:
        raise ZeroDivisionError

    counter = [0]
    result = [0]
    #Keep subtrating until the result is a negative number
    while n1 != [-1]:
        result = n1
        n1 = bigSub(n1, n2)
        counter = bigAdd(counter, [1])
    if isDiv :
        #return the number of times you successfully subtrated
        #n2 from n1
        return bigSub(counter, [1])
    else:
        #return the remaining number before subtration became
        #negative
        return result

"""
Addition can be done digit wise such it is done by hand
however one must account for a possible carry when digit
addition overflows.
"""
def bigAdd( n1, n2 ):
    result = []
    carry = 0
    #Iterate until you hit the end of one of the lists
    for i in range(0, min(len(n1), len(n2))):
        r = n1[i] + n2[i] + carry
        #calculate the carry by using integer division
        carry = r // 10
        #calculate the digit by using modulous
        result.append(r % 10)
    #check for left over carry
    if len(n1) == len(n2):
        if carry != 0:
            result.append(carry)
        return result
    #If there are left over digits, they must be appended
    #to the result as well, keeping carry in mind
    if len(n1) > len(n2):
        for i in range(len(result), len(n1)):
            result.append((n1[i] + carry)% 10)
            carry = (n1[i] + carry)// 10
    else:
        for i in range(len(result), len(n2)):
            result.append((n2[i] + carry)% 10)
            carry = (n2[i] + carry)//10
    if carry != 0:
        result.append(carry)
    return result

"""
Subtration was the most difficult, this implentation
follows the algorithm one would follow when performing
subtration by hand.
""" 
def bigSub( n1, n2 ):
    result = []
    #if the list are the same, we return [0] right away
    #this prevent the case of a list of zeros being returned
    if n1 == n2:
        return [0]
    #I'm only concerning myself with unsigned values for this
    #exercise therefore if n2 is larger than n1 we return a
    #negative number identifier
    if len(n2) > len(n1):
        return [-1]
    #iterate over the subtrator
    for i in range(0, len(n2)):
        r = n1[i] - n2[i]
        #check if digit subtration results in a negative
        if r < 0:
            #if there is no subsequent digit to pull from
            #n2 is larger than n1 return negative identifier
            if i + 1 >= len(n1):
                return [-1]
            #if the subsequent digit to pull from is zero
            #delegate to helper function to repeated pull
            if n1[i + 1] == 0:
                bigSubHelper(n1, i)
            else:
            #otherwise just pull once from the subsequent digit
                n1[i+1] -= 1
            #calculate the result digit after adding 10 from pulling
            r = 10 + n1[i] - n2[i]
        result.append(r)
    #Add remaining digits into result from n1
    if len(n1) > len(n2):
        for i in range(len(n2), len(n1)):
            result.append(n1[i])
    #Remove any leading zeros
    while result[-1] == 0:
        del result[-1]
    return result

def bigSubHelper( n1, i ):
    j = i + 1
    while n1[j] == 0:
        n1[j] = 9
        if n1[j + 1] != 0:
            n1[j + 1] -= 1
            break
        j += 1
    
