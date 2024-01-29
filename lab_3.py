class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"


paper = PaperBook('Emma', 'Jane Osten', 500)
audio = AudioBook('The castle', 'Franz Kafka', 22.5)
print(paper.__str__())
print(paper.__repr__())
print(audio.__str__())
print(audio.__repr__())