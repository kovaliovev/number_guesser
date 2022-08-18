import random


play = input('Enter "S" to start')
while play.lower() == 's':
    print("Please choose the game language")
    leng = input('en for english or uk for ukrainian \n')
    target = random.randint(1, 100)
    count = 1

    while leng.lower() != 'uk' and leng.lower() != 'en':
        leng = input('Please choose an available language \n')

    if leng.lower() == 'uk':
        print('Число загадане, спробуйте вiдгадати його якомога швидше!')
        trying = int(input('Введiть ваше число вiд 1 до 100 \n'))
        while trying != target:
            if trying > target:
                trying = int(input('Занадто багато, спробуйте ще раз \n'))
                count += 1
            else:
                trying = int(input('Занадто мало, спробуйте ще раз \n'))
                count += 1
        print(f'Вiтаю, ви вiдгадали! Кiлькiсть ваших спроб: {count}')
        play = input('Введ iть "S", щоб знову грати чи щось  iнше, щоб вийти \n')

    elif leng.lower() == 'en':
        print('The number is guessed, try to guess it as soon as possible!')
        trying = int(input('Enter your number from 1 to 100 \n'))
        while trying != target:
            if trying > target:
                trying = int(input('Too many, try again \n'))
                count += 1
            else:
                trying = int(input('Too little, try again \n'))
                count += 1
        print(f'Congratulations, you guessed it! Number of your attempts: {count}')
        play = input('Enter "S" to play again or something else to exit \n')
