def prime_numbers(low:int, high:int) -> list:
    """Finds prime numbers in certain range.
    Returns the list with numbers that are sorted by ascending order."""
    if low < 0 or high < 0:
        raise ValueError("Range limits must be positive: "+ str(low) + " "+ str(high))
    if low > high:
        raise ValueError("Lower limit must be less than higher: "+ str(low) + " "+ str(high))
    answer = []
    prime = [True] * (high + 1)
    prime[0], prime[1] = False, False
    for i in range(2, high + 1):
        if prime[i]:
            for j in range(2 * i, high + 1, i):
                prime[j] = False

    for i in range(low, high + 1):
        if prime[i]:
            answer.append(i)
    return answer

if __name__ == "__main__":
    low, high = int(input()), int(input())
    print(*prime_numbers(low, high))
