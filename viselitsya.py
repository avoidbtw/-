import random
from time import sleep

wordList = ('яблоко','человек','кошка','пульт','кнопка','Шестнадцатеричный','Конституционный','абсолютизм')
life = 6
nowWord = random.choice(wordList)
distWord = len(nowWord)
sliceDistWord = nowWord.split()
textnow = []
starWord = []
players = int(input("Для скольки игроков предназначена данная игра?"))
if players >= 2:
    print("Запущена игра на",players,'игроков')
    life * players
for i in nowWord:
    textnow.append(i)
    starWord.append('*')
game = True
print('твое слово:')
print(starWord)
print('введи букву')
useLetter = [1]


def checkWord(life, game, textnow, starWord, useLetter):
    if life > 0:
        if game == True:
            find = 0
            text = input()
            if all(i != text for i in useLetter):
                useLetter.append(text)
                for i in textnow:
                    if text == i:
                        find += 1
                if find > 0:
                    print('+буква')
                    sleep(0.5)
                    print('Очередь следующего игрока выбрать букву')
                    x = 0
                    for i in textnow:
                        z = 0
                        if i == text:
                            starWord[x] = text
                            for i in starWord:
                                if i == '*':
                                    z += 1
                            if z == 0:
                                game = False
                                break
                        x += 1
                else:
                    life -= 1
                    print('+ошибка = - 1 жизнь')
                    print('всего хп осталось = ' + str(life))
                    sleep(0.5)
                    print('Очередь следующего игрока выбрать букву')
                print(starWord)
                print('использовано букв')
                for i in useLetter:
                    print(str(i) + ' ', end='')
                print()
                checkWord(life, game, textnow, starWord, useLetter)
            else:
                print('эта буковка уже была использована')
                checkWord(life, game, textnow, starWord, useLetter)
        else:
            print('не ну ты крутой, победа за тобой')
    else:
        game = False
        print('Вы проиграли(')
        print('правильное слово было:')
        for i in textnow:
            print(str(i), end='')


checkWord(life, game, textnow, starWord, useLetter)
