n = int(input())
count = 0
type_1 = 0
type_2 = 0
type_3 = 0
type_4 = 0

def read_type(i):
	global count
	if i + count > n:
		print("invalid")
		exit()
	for _ in range(i -1):
		utfIn = input()
		count += 1
		if utfIn[0:2] != "10":
			print("invalid")
			exit()


while count < n:
	utfIn = input()
	if utfIn[0] == "0":
		type_1 += 1
	elif utfIn[0:3] == "110":
		read_type(2)
		type_2 += 1
	elif utfIn[0:4] == "1110":
		read_type(3)
		type_3 += 1
	elif utfIn[0:5] == "11110":
		read_type(4)
		type_4 += 1
	else:
		print("invalid")
		exit()
	count += 1

print(type_1)
print(type_2)
print(type_3)
print(type_4)