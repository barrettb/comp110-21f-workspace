left_hand: int = int(input(" Left-hand side: "))
right_hand: int = int(input("Right-Hand Side: "))

exp = left_hand ** right_hand
division = left_hand / right_hand
int_div = left_hand // right_hand
remainder = left_hand % right_hand

print(str(left_hand) + " ** " + str(right_hand) + " is " + str(exp))
print(str(left_hand) + " / " + str(right_hand) + " is " + str(division))
print(str(left_hand) + " // " + str(right_hand) + " is " + str(int_div))
print(str(left_hand) + " % " + str(right_hand) + " is " + str(remainder))

__author__ = "730390257"