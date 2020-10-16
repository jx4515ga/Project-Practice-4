import api_controller
import edemam
import api_controller
def main():
    drink = edemam.get_drink()
    return drink



def display_drink():
    drink = ''
    while len(drink) == 0:
        drink = input('Enter the name of the drink: ').strip()
    drink = f'{drink}'
    return drink



