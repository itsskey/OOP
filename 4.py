class Tree:
    """Базовый класс Деревья"""
    def __init__(self, name: str, height: int):
        self._name = name
        """Делаем атрибут name непубличным, поскольку название дерева меняться не может"""
        self.height = height

    def add_height(self, addition: int) -> None:
        """Метод, с помощью которого можно следить за динамикой роста дерева"""
        self.height += addition

    def __str__(self):
        return f"Дерево {self._name}. Высота {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, height={self.height!r})"


class OrangeTree(Tree):
    """Дочерний класс Апельсиновое дерево"""
    def __init__(self, name, height, fruits: int):
        super().__init__(name, height)
        self.fruits = fruits

    def add_fruits(self, addition: int) -> None:
        """Метод для добавления количества фруктов на апельсиновом дереве.
        Перегружаем этот метод, поскольку атрибут fruits в базовом классе отсутствует"""
        self.fruits += addition

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, height={self.height!r}, fruits={self.fruits!r})"


if __name__ == "__main__":
    first_tree = Tree('Сосна', 100)
    second_tree = OrangeTree('Каламондин', 60, 5)
    second_tree.add_height(10)
    second_tree.add_fruits(7)
    print(first_tree.__str__())
    print(first_tree.__repr__())
    print(second_tree.__str__())
    print(second_tree.__repr__())
    pass
