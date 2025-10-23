numbers = [1, 4, 6, 7, 9, 11, 12, 13, 15, 18, 20]

def missing_numbers():
    numbers.sort()
    return [i for i in range(numbers[0], numbers[-1]) if i not in numbers]

def main():
    print(missing_numbers())
    
    
if __name__ == "__main__":
    main()