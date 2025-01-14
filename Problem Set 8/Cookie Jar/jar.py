class Jar:
    def __init__(self, capacity=12, size=0):        
        self.capacity = capacity  # This calls the capacity setter
        self._size = size   # Private variable (starting size)

    def __str__(self):
        # Represent the jar as a string of 🍪 based on the number of size
        return '🍪' * self._size

    def deposit(self, n):
        # Ensure you can't exceed the capacity
        if self._size + n > self.capacity:
            raise ValueError("Cannot deposit more size than the capacity.")
        self._size += n

    def withdraw(self, n):
        # Ensure you can't withdraw more size than are available
        if n > self.size:
            raise ValueError("Not enough size to withdraw.")
        self.size -= n

    @property
    def size(self):
        return self._size  # Getter for _size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size cannot be negative.")
        if value > self.capacity:
            raise ValueError("size cannot exceed capacity.")
        self._size = value  # Setter for _size

    @property
    def capacity(self):
        return self._capacity  # Getter for _capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self._capacity = value  # Setter for _capacity
