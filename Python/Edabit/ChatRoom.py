def main():
	num = int(input("Enter number: "))
	if num == 0:
		print("No one online")
	if num == 1:
		print("User1 online")
	if num == 2:
		print("User1 and user2 online")
	if num > 2:
		print("User1, user2 and", num-2, "more online")


if __name__ == "__main__":
	main()
