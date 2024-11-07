import random

start_range = int(input("Диапазондун төмөнкү чегин киргизиңиз: "))
end_range = int(input("Жогорку диапазону киргизиңиз: "))

computer_number = random.randint(start_range, end_range)

attempts = 0
guessed = False

while not guessed:
    user_guess = int(input(f"{start_range}дон {end_range}га чейинки санды тап: "))
    if user_guess < computer_number:
        print("Табышмактуу Сан азыраак!")
    elif user_guess > computer_number:
        print("Табышмактуу Сан чоңураак!")
    else:
        print("Табышмактуу Сан болдуу!")
        guessed = True
    attempts += 1
print(f"Куттуктайбыз! Сиз {computer_number} санын {attempts} аракетте таптыңыз.")
