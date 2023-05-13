# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)


# M1 O(n^2)
def get_diagonal(input_tuple):
	output = []
	for i in range(len(input_tuple)):
		output.append(input_tuple[i][i])

	return tuple(output)



output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)