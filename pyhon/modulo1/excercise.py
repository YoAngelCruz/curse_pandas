#  0
color="blue"

print(color)
#  1

pi = 3.14159 # approximate
diameter = 3

radius=diameter/2

area=pi*(radius*radius)

print(area)
# 2

a = [1, 2, 3]
b = [3, 2, 1]

c=a
a=b
b=c

print(a, b, c)
#  3a
print((5 - 3) // 2)
#  3b
print(8 - 3 * 2 - (1 + 1))

#  3b

alice_candies = 121
bob_candies = 77
carol_candies = 109

all_candies =(alice_candies + bob_candies + carol_candies)
to_smash = (all_candies % 3)
print (to_smash)