class MenuMeal:
    """
    Class for subsubitems == meals
    """
    def __init__(self, *args):
        """
        init method
        :param args:
        """
        self.position = args[0]

    def info(self):
        """
        print info about subsubitems
        :return:
        """
        print("\t", end="")
        print(self.position)


class MenuCategory:
    """
    Class for subitems == categories
    """
    def __init__(self, *args):
        """
        init method
        :param args:
        """
        self.position = args[0]
        self.children = []

    def add(self, child):
        """
        adding subitem
        :param child: - subitem
        :return:
        """
        self.children.append(child)

    def remove(self, child):
        """
        removing subitem
        :param child: - subitem
        :return:
        """
        self.children.remove(child)

    def info(self):
        """
        print info about item and its subitems
        :return:
        """
        print(self.position)
        for child in self.children:
            print("\t\t", end="")
            child.info()


class Menu:
    """
    Main class for Main Menu
    """
    def __init__(self, *args):
        """
        init method
        :param args:
        """
        self.position = args[0]
        self.children = []

    def add(self, child):
        """
        adding subitem
        :param child: - subitem
        :return:
        """
        self.children.append(child)

    def remove(self, child):
        """
        removing subitem
        :param child: - subitem
        :return:
        """
        self.children.remove(child)

    def info(self):
        """
        print info about item and its subitems
        :return:
        """
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.info()


if __name__ == "__main__":
    MainMenu = Menu("Main Menu")
    Kitchen = MenuCategory("Kitchen")
    Bar = MenuCategory("Bar")
    KitchenCategory1 = MenuCategory("Cold Snacks")
    KitchenCategory2 = MenuCategory("Hot Snacks")
    KitchenCategory3 = MenuCategory("Salads")
    KitchenCategory4 = MenuCategory("Soups")
    KitchenCategory5 = MenuCategory("Main Dishes")
    BarCategory1 = MenuCategory("NonAlco Drinks")
    BarCategory2 = MenuCategory("Alco Drinks")
    BarCategory3 = MenuCategory("Tea")
    BarCategory4 = MenuCategory("Coffee")
    ColdSnack1 = MenuMeal("Chips")
    ColdSnack2 = MenuMeal("Carpaccho")
    HotSnack1 = MenuMeal("Fried chips")
    Salad1 = MenuMeal("Greek salad")
    Salad2 = MenuMeal("Caeser salad")
    Salad3 = MenuMeal("Russian classic salad")
    Soup1 = MenuMeal("Borsch")
    Soup2 = MenuMeal("Rassolnik")
    MainDish1 = MenuMeal("Steak")
    MainDish2 = MenuMeal("Dalmadoes")
    MainDish3 = MenuMeal("Stefado")
    NonAlcoDrink1 = MenuMeal("Water")
    NonAlcoDrink2 = MenuMeal("Apple Juice")
    NonAlcoDrink3 = MenuMeal("Orange Juice")
    AlcoDrink1 = MenuMeal("Vodka")
    AlcoDrink2 = MenuMeal("Beer")
    AlcoDrink3 = MenuMeal("White Russian")
    AlcoDrink4 = MenuMeal("Ersch")
    Tea1 = MenuMeal("Black")
    Tea2 = MenuMeal("Green")
    Tea3 = MenuMeal("Milk Ulun")
    Coffee1 = MenuMeal("Espresso")
    Coffee2 = MenuMeal("Americano")

    KitchenCategory1.add(ColdSnack1)
    KitchenCategory1.add(ColdSnack2)
    KitchenCategory2.add(HotSnack1)
    KitchenCategory3.add(Salad1)
    KitchenCategory3.add(Salad2)
    KitchenCategory3.add(Salad3)
    KitchenCategory4.add(Soup1)
    KitchenCategory4.add(Soup2)
    KitchenCategory5.add(MainDish1)
    KitchenCategory5.add(MainDish2)
    KitchenCategory5.add(MainDish3)
    BarCategory1.add(NonAlcoDrink1)
    BarCategory1.add(NonAlcoDrink2)
    BarCategory1.add(NonAlcoDrink3)
    BarCategory2.add(AlcoDrink1)
    BarCategory2.add(AlcoDrink2)
    BarCategory2.add(AlcoDrink3)
    BarCategory2.add(AlcoDrink4)
    BarCategory3.add(Tea1)
    BarCategory3.add(Tea2)
    BarCategory3.add(Tea3)
    BarCategory4.add(Coffee1)
    BarCategory4.add(Coffee2)

    Kitchen.add(KitchenCategory1)
    Kitchen.add(KitchenCategory2)
    Kitchen.add(KitchenCategory3)
    Kitchen.add(KitchenCategory4)
    Kitchen.add(KitchenCategory5)
    Bar.add(BarCategory1)
    Bar.add(BarCategory2)
    Bar.add(BarCategory3)
    Bar.add(BarCategory4)

    MainMenu.add(Kitchen)
    MainMenu.add(Bar)

    MainMenu.info()
