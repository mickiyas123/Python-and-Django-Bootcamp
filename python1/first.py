import random
def get_guess():
    return list(input("What is your guess: "))
def generate_code():
    digits=[str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED!"
    clues=[]
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close") 
    if clues == []:
        return ['Nope']
    else:
        return clues

print("Welcome code Breaker!")
secret_code =generate_code()
print(secret_code) 
clueReport=[]
while clueReport !="CODE CRACKED!":
    guess=get_guess()
    clueReport=generate_clues(secret_code,guess)
    print("here is the result of your guess.")
    for clue in clueReport:
        print(clue)                                    