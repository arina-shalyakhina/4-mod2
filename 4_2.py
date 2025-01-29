import doctest
class Language:
  def __init__(self, name:str, vowels:int, consonants:int):
    """
    Создание и подготовка к работе объекта "Язык"
    :param name:название языка
    :param vowels:число гласных фонем в языке
    :param consonants: число согласных фонем в языке
    Пример:
    >>> russian=Language("Русский", 5, 34)
    """
    if not isinstance(name, str):
       raise TypeError("Название языка должно быть строкой")
    if name.isalpha()==False:
      raise ValueError("Название языка должно содержать только буквы")
    self.name=name
    if not isinstance(vowels, int):
      raise TypeError("Число гласных должно быть целым числом")
    if vowels<=0:
      raise ValueError("Число гласных в языке обязательно положительно")
    self.vowels=vowels
    if not isinstance(consonants, int):
      raise TypeError("Число согласных должно быть целым числом")
    if consonants<=0:
      raise ValueError("Число согласных в языке обязательно положительно")
    self.consonants=consonants
  def whats_more(self, vowels:int, consonants:int)->str:
    """
    Функция, которая определяет к какой группе принадлежит язык по его соотношению гласных и согласных
    :return: Тип языка на основании этой типологии
    Примеры:
    >>> ubihskiy=Language("Убыхский", 2, 84)
    >>> ubihskiy.whats_more(2, 84)
    'Язык относится к консонантным языкам'
    """
    if consonants/vowels>1:
      return "Язык относится к консонантным языкам"
    if vowels/consonants>1:
      return "Язык относится к вокалическим языкам"
    if vowels==consonants:
      return "Язык относится к консонантно-вокалическим языкам"
  def phonemes_sum(self, vowels:int, consonants:int)->int:
    """
    Функция, которая определяет суммарное количество фонем
    :return: сумма гласных и согласных
    Примеры:
    >>> english=Language("Английский", 20, 24)
    >>> english.phonemes_sum(20,24,)
    44
    """
    return vowels+consonants
  def __str__(self):
    """
    Функция, которая выводит экземпляр класса на экран в удобно читаемом виде
    """
    return f"{self.name} содержит {self.vowels} гласных фонем и {self.consonants} согласных фонем"
  def __repr__(self):
    """
    Функция, которая выводит экземпляр класса так, как он есть
    """
    return f"{self.__class__.__name__}(name={self.name!r}, vowels={self.vowels!r}, consonants={self.consonants!r})"
class Tonal(Language):
  def __init__(self, name:str, vowels:int, consonants:int, tones:int):
    """
    Создаем дочерний класс "Тональные языки"
    Добавляем новый атрибут "тоны":
    :param tones: число тонов в языке
    :vowels: число гласных фонем с ровным тоном
    Пример:
    >>> vietnamskiy=Tonal("Вьетнамский", 14, 21, 6)
    """
    super().__init__(name, vowels, consonants)
    if not isinstance(tones, int):
      raise TypeError("Число тонов должно быть целым числом")
    if tones<=1:
      raise ValueError("Число тонов в тональном языке обязательно больше 1")
    self.tones=tones
  def phonemes_sum(self, vowels:int, consonants:int, tones:int)->int:
    """
    Перегружаем метод родительского класса в дочернем.
    При вычислении суммарного количества фонем необходимо помнить:
    гласный звук, произнесенный разными тонами, различает смыслы слов, а значит, обозначает разные фонемы
    Пример:
    >>> vietnamskiy=Tonal("Вьетнамский", 14, 21, 6)
    >>> vietnamskiy.phonemes_sum(14,21,6)
    105
    """
    return tones*vowels+consonants
  def whats_more(self, vowels: int, consonants: int) -> str:
    """
    Функцию whats_more(self, vowels:int, consonants:int) можно унаследовать от родительского класса,
    так как при выявлении соотношения между гласными и согласными тоны роли не играют
    Пример:
    >>> vietnamskiy=Tonal("Вьетнамский", 14, 21, 6)
    >>> vietnamskiy.whats_more(14, 21)
    'Язык относится к консонантным языкам'
    """
    return super().whats_more(vowels, consonants)
  def __str__(self):
    return f"{self.name} содержит {self.vowels} гласных фонем, {self.consonants} согласных фонем и {self.tones} тонов"
  def __repr__(self):
    return f"{self.__class__.__name__}(name={self.name!r}, vowels={self.vowels!r}, consonants={self.consonants!r}, tones={self.tones!r}"
if __name__ == '__main__':
    doctest.testmod()