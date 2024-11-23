
"""
If you don't have NumPy installed, you need to install it first using the following command:

pip install numpy
Or if you're using Python 3 explicitly:

pip3 install numpy
Once installed, you can import it using import numpy as np and start using its powerful features to work with arrays, matrices, and more.

"""

import numpy as np

# Create a NumPy array with the specified numbers
arr = np.array([5, 10, 15, 20, 25])

# Print the original array
print("Original Array:")
print(arr)

# Add 10 to each element in the array
arr_added = arr + 10

# Multiply each element by 2
arr_multiplied = arr_added * 2

# Print the modified array
print("\nModified Array after adding 10 and multiplying by 2:")
print(arr_multiplied)
