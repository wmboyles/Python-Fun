from random import choice


def main(inclSymbols=True, passwordLen=7, numSuggestions=10):
    for i in range(numSuggestions):
        passwordSugg = ""
        for j in range(passwordLen):
            if inclSymbols: rand = choice(list(range(33, 127)))
            else: rand = choice(list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)))
            
            passwordSugg += chr(rand)

        print(passwordSugg)


main(False, 16, 100)
input()
