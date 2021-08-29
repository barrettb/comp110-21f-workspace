left_hand: int = int(input(" Left-hand side: "))
right_hand: int = int(input("Right-Hand Side: "))

less_than = left_hand < right_hand
greater_than_or_equal_to = left_hand >= right_hand
equal_to = left_hand == right_hand
not_equal = left_hand != right_hand

print(str(left_hand) + " < is " + str(right_hand) + " " + str(less_than))
print(str(left_hand) + " >=  is " + str(right_hand) + " " + str(greater_than_or_equal_to))
print(str(left_hand) + " == is " + str(right_hand) + " " + str(equal_to))
print(str(left_hand) + " != is " + str(right_hand) + " " + str(not_equal))

__author__ = "730390257"