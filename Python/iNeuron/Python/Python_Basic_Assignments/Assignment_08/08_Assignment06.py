import pyinputplus as pypi
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		6. If a blank input is entered three times, what does inputStr(limit=3) do?""")


def main():

	print("""Answer-
		The statement inputStr(limit=3) will throw two exceptions ValidationException and RetryLimitException.
		The first exception is thrown because blank values are not allowed by inputStr() function by default.
		it we want to consider blank values as valid input, we have to set blank=True.\n

		The second exception is occurred because we have reached the max limit we have specified by using limit parameter.
		inorder to avoid this exception we can use default parameter to return a default value when max limit is reached..""")

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
