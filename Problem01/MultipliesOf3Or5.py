#Note: List comprehension
def sum_of_multiplies_3_or_5(to):
    return sum([i for i in range (1, to) if i % 3 == 0 or i% 5 == 0])

if __name__ == "__main__":
    print(sum_of_multiplies_3_or_5(1000))