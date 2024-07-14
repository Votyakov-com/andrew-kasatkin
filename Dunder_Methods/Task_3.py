class Item:
    def __init__(self, ID, price, rarity, color, name):
        self.ID = ID
        self.price = price
        if rarity == 0:
            self.rarity = 'common'
        elif rarity == 1:
            self.rarity = 'rare'
        elif rarity == 2:
            self.rarity = 'epic'
        elif rarity == 3:
            self.rarity = 'legendary'
        self.color = color
        self.name = name

    @staticmethod
    def sort(*args):
        sorted_ID = list(args[n].ID for n in range(len(args)))
        sorted_ID.sort()
        sorted_ID.reverse()
        sorted_prices = list(obj.price for obj in args)
        sorted_prices.sort()
        sorted_prices.reverse()
        sorted_color = list(obj.color for obj in args)
        sorted_rarity = list(obj.rarity for obj in args)

        clear_inventory = list()

        # Непонятно как отлавливать значения, которые уже успели уйти в корректно отсортированный список.
        # Создать цикл с проверкой на [index] и [index+1] не получилось. Постоянно всплывала IndexError.

        for index in range(len(args)):
            if index != 0:
                if args[index].ID == args[index - 1].ID:
                    pass
                else:
                    clear_inventory.append(args[index])
            else:
                clear_inventory.append(args[index])

        check_list = list()
        for index in range(len(clear_inventory)):
            check_list.append(clear_inventory[index].name)
        print(check_list)


gold_crown = Item(645, 1000, 3, 'ffa500', 'gold_crown')
pot = Item(23, 10, 0, 'ecd8718', 'pot')
flask = Item(109, 99, 1, 'a56705', 'flask')
jewelry = Item(309, 311, 3, '744fdb', 'jewelry')
treasure_map = Item(709, 500, 2, 'efe8d4', 'treasure_map')
stone = Item(3, 1, 0, 'a9a19b', 'stone')
medicinal_herbs = Item(74, 69, 2, '35c02e', 'medicinal_herbs')

Item.sort(gold_crown, pot, flask, jewelry, treasure_map, stone, medicinal_herbs)