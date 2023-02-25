import os
import random
import string

passnumber1 = (random.randint(0, 9))
passnumber2 = (random.randint(0, 9))
passnumber3 = (random.randint(0, 9))
passnumber4 = (random.randint(0, 9))
passnumber5 = (random.randint(0, 9))
passnumber6 = (random.randint(0, 9))
passnumber7 = (random.randint(0, 9))
passnumber8 = (random.randint(0, 9))
passnumber9 = (random.randint(0, 9))

pass1 = string.ascii_lowercase

pass_string1 = random.choice(pass1)
pass_string2 = random.choice(pass1)
pass_string3 = random.choice(pass1)
pass_string4 = random.choice(pass1)
pass_string5 = random.choice(pass1)
pass_string6 = random.choice(pass1)
pass_string7 = random.choice(pass1)
pass_string8 = random.choice(pass1)
pass_string9 = random.choice(pass1)


ip1 = (random.randint(0, 255))
ip2 = (random.randint(0, 255))
ip3 = (random.randint(0, 255))
ip4 = (random.randint(0, 255))

credit_cart = (random.randint(1111111111111111, 9999999999999999))


print (" ")
print (" ")
print ("Password: ",pass_string1,pass_string2,passnumber1,passnumber2,pass_string3,pass_string4)

print ("İp Adress: ",ip1,".",ip2,".",ip3,".",ip4)

print ("Credit Cart Number: ",credit_cart)
