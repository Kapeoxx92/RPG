classes= ['warlock', 'warrior', 'ranger', 'healer']
items = ['wand', 'sword', 'longbow', 'potion']

players = []

class player:
    def __init__(self, name):
        self.nickname= name
        self.backpack = []

    def chooseYourClass(self, number_of_character):
        self.type= classes[number_of_character]

    def giveItem(self, number_of_item):
        self.backpack.append(items[number_of_item])

    def showItems(self):
        for item in self.backpack:
            print(item)

def main(args=None):
    while 1:
        print('1 stworz bohatera, 2  wybierz klase, 3  wybierz przedmiot, 4 pokaż moje towary')
        option = int(input())
        if option == 1:
            nick = input('wprowadz nick ')
            temp_player = player(nick)
            players.append(temp_player)
        if option == 2:
            rola = int(input('nadaj klase '))
            players[-1].chooseYourClass(rola)
        if option == 3:
            przedmiot = int(input('daj przedmiot '))
            players[-1].giveItem(przedmiot)
        if option == 4:
            players[-1].showItems()
        if option == 5:
            for temp_player in players:
                print(temp_player.nickname)
                temp_player.showItems()



if __name__ == '__main__':
    main()