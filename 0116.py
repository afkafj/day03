

Guess_me = 5
for number in range(10):
    if number < Guess_me:
        print("'too low'")
    elif number == Guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    number = number + 1
