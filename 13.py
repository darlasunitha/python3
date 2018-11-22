s=int(input())
for j in range(2,s):
	if (s%j==0):
		print(s," is not a prime number")
		break
	else:
		print(s," is prime number")
		break
