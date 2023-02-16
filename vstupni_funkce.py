def vstup_cisel(zprava):
    while True:
        vstup = input(zprava)
        if vstup.isdigit():
            return int(vstup)
        else:
            print("\nProsím zadejte pouze čísla.")


def vstup_string(zprava):
    while True:
        vstup = input(zprava)
        if vstup.isalpha():
            return vstup
        else:
            print("\nProsím zadejte pouze text.")
