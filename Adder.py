def calculate(first_number: float, second_number: float) -> float:
	"""Return the sum of two numbers."""
	return first_number + second_number


def main() -> None:
	print("Adder Calculator (type 'q' to quit)")
	while True:
		entry = input("Enter two numbers separated by a space: ").strip()
		if entry.lower() in {"q", "quit", "exit"}:
			break

		try:
			first_number, second_number = map(float, entry.split())
		except ValueError:
			print("Please enter exactly two valid numbers.")
			continue

		print(f"Sum: {calculate(first_number, second_number)}")


if __name__ == "__main__":
	main()
