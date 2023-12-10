import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов
class Telegram:
    def __init__(self, message: Union[str], friend: Union[str], number_of_friends: Union[int]):
        """
        Создание и подготовка к работе объекта Телеграм
        Примеры:
        >>> example = Telegram("hello", "Jack", 100)    # инициализация экземпляра класса
        """
        if not isinstance(message, (str)):
            raise TypeError
        self.message = message  # отправляемое сообщение
        if not isinstance(friend, (str)):
            raise TypeError
        self.friend = friend    # друг, которому пишем
        if not isinstance(number_of_friends, (int)):
            raise TypeError
        if not number_of_friends > 0:
            raise ValueError
        self.number_of_friends = number_of_friends  # общее количество друзей
    def send_message(self) -> str:
        """
        Функция которая отправляет сообщение

        :return: message

        Примеры:
        >>> example = Telegram("hello", "Jack", 100)
        >>> example.send_message()
        'hello'
        """
        return self.message
    def to_whom(self) -> str:
        """
        Функция которая определяет кому мы отправляем сообщение

        :return: name

        Примеры:
        >>> example = Telegram("hello", "Jack", 100)
        >>> example.to_whom()
        'Jack'
        """
        return self.friend


class Instagram:
    def __init__(self, number_of_pictures: Union[int], action: Union[str]):
        """
        Создание и подготовка к работе объекта Инстаграм
        Примеры:
        >>> example = Instagram(5, "story")    # инициализация экземпляра класса
        """
        if not isinstance(action, (str)):
            raise TypeError
        self.action = action    # действие с картинкой
        if not isinstance(number_of_pictures, (int)):
            raise TypeError
        if not number_of_pictures > 0:
            raise ValueError
        self.number_of_friends = number_of_pictures  # количество картинок
    def count_pictures(self) -> int:
        """
        Функция которая считает количество изображений
        :return: number of pics

        Примеры:
        >>> example = Instagram(100, "reels")
        >>> example.count_pictures()
        """
        ...
    def action_with_picture(self) -> str:
        """
        Функция которая узнает куда выкладываем изображение
        :return: action

        Примеры:
        >>> example = Instagram(100, "reels")
        >>> example.action_with_picture()
        'reels'
        """
        return self.action


class VK:
    def __init__(self, friend: Union[str], action: Union[str]):
        """
        Создание и подготовка к работе объекта Инстаграм
        Примеры:
        >>> example = VK("Karina", "add")    # инициализация экземпляра класса
        """
        if not isinstance(action, (str)):
            raise TypeError
        self.action = action  # действие с другом
        if not isinstance(friend, (str)):
            raise TypeError
        self.number_of_friends = friend  # друг
    def add_or_delete_friend(self) -> str:
        """
        Функция которая удаляет или добавляет друга
        :return: add or delete

        Примеры:
        >>> example = VK("Jane Austen", "add")
        >>> example.add_or_delete_friend()
        """
        ...
    def share_music(self) -> str:
        """
        Функция которая выбирает рандомную песню чтобы поделиться с другом
        :return: song

        Примеры:
        >>> example = VK("Jane Austen", "add")
        >>> example.share_music()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
