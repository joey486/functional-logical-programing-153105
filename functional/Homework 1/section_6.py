import random

def nihushTest(random_tuple, *guesses):
    result = []
    correct_guesses = 0

    for i in range(len(random_tuple)):
        if i < len(guesses) and random_tuple[i] == guesses[i]:
            result.append(guesses[i])
            correct_guesses += 1
        else:
            result.append("X")

    return tuple(result), (correct_guesses / len(random_tuple)) * 100

def function6():
    N = random.randint(3, 9)
    random_tuple = tuple(random.randint(1, 9) for _ in range(N))
    # For testing purposes, we can print the randomly generated tuple
    # print("Random tuple:", random_tuple)
    
    maxpct = 0
    
    while True:
        print(f"Enter {N} integers between 1 and 9 (inclusive) as your guess (duplicates allowed), or -1 to exit:")
        user_input = input()
        
        if user_input.strip() == '-1':
            break

        guesses = tuple(map(int, user_input.split()))
        
        if len(guesses) != N:
            print(f"Please enter exactly {N} numbers.")
            continue
        
        result, success_pct = nihushTest(random_tuple, *guesses)
        print("Result tuple:", result)
        print(f"Success rate: {success_pct:.2f}%")
        
        if success_pct > maxpct:
            maxpct = success_pct
        
        if success_pct == 100.0:
            print("Congratulations! You guessed all numbers correctly.")
            break
    
    print("Game over.")
    print("The randomly generated tuple was:", random_tuple)
    print(f"Highest success rate achieved: {maxpct:.2f}%")

def main():
    function6()

if __name__ == "__main__":
    main()
