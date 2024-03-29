import random
import math
# Taking Inputs
lower = int(input("Nhập giới hạn dưới: "))

# Taking Inputs
upper = int(input("Nhập giới hạn trên "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tBạn chỉ có ", 
	round(math.log(upper - lower + 1, 2)),
	" cơ hội để đoán số. Chúc bạn may mắn!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Mời đoán số:- "))

	# Condition testing
	if x == guess:
		print("Chúc mừng bạn đã đoán đúng ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("Bạn đoán quá thấp!")
	elif x < guess:
		print("Bạn đoán quá cao!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nSố cần đoán là %d" % x)
	print("\tChúc bạn may mắn lần sau!")

