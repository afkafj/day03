

Guess_me = 7
number = 1
while True:
    if number < Guess_me:
        print("'too low'")
    elif number == Guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    number = number + 1
