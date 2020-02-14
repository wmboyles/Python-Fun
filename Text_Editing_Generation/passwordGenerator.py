from random import choice


def main(inclSymbols=True, passwordLen=7, numSuggestions=10):
    for i in range(numSuggestions):
        print(''.join(
            [
                chr(choice(list(range(33,127)) if inclSymbols
                else (list(range(48,58)) + list(range(65,91)) + list(range(97,123)))))
            for j in range(passwordLen)
            ]
            )
        )


while True:
    inclSymbols = input("Include Symbols? (Y/N): ").lower() == "y"
    length = int(input("Password Length: "))
    suggs = int(input("Num Suggestions: "))
    main(inclSymbols, length, suggs)
    print("\nPress ENTER to continue\n")
    input()
