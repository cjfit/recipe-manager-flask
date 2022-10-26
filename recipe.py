class Recipe:

    dishes = []
    def __init__(self, name, ingredients):
        self.__ingredients = ingredients
        self.__name = name
        Recipe.dishes.append(self)

    @classmethod
    def remove_dish(cls, dish_name):
        """
        Given a dish name, removes all objects in dishes with that name
        """
        for dish in cls.dishes:
            if dish.__name == dish_name:
                cls.dishes.remove(dish)

    def get_ingredients(self):
        return self.__ingredients


    def __str__(self):
        """
        Returns the recipe name as a string
        :return: name (string)
        """
        return self.__name