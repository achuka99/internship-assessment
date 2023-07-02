from typing import List


def collatz(n: int) -> List[int]:
    sequence = [n]  # Initialize the list with the initial value n

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1

        sequence.append(n)  # Append the new value of n to the sequence list

    return sequence


def distinct_numbers(numbers: List[int]) -> int:
    unique_numbers = set(numbers)  # Convert the list to a set to get unique elements
    return len(unique_numbers)  # Return the number of unique elements in the set
