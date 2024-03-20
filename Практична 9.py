class Book:
    def __init__(self, title):
        self.title = title
class ChroniclesOfNarnia(Book):
    def __init__(self):
        super().__init__("Хроніки Нарні")
class TheHumanAmphibian(Book):
    def __init__(self):
        super().__init__("Людина-амфібія")
class  GulliversTravels(Book):
    def __init__(self):
        super().__init__("Подорож Гуллівера")
class IslandsInTheOcean(Book):
    def __init__(self):
        super().__init__("Острови в океані")
class CrimeAndPunishment(Book):
    def __init__(self):
        super().__init__("Злочин і кара")
class TheManInBrownSuit(Book):
    def __init__(self):
        super().__init__("Людина в коричневому костюмі")
class TheMurderOnTheStreetOfMorg(Book):
    def __init__(self):
        super().__init__("Вбивство на вулиці Морг")
def message_handler(class_name):
    return f"Назва книги: {class_name().title}"
fantasy_books = [ChroniclesOfNarnia, TheHumanAmphibian, GulliversTravels, IslandsInTheOcean]
detective_books = [CrimeAndPunishment, TheManInBrownSuit, TheMurderOnTheStreetOfMorg]
for book_class in fantasy_books:
    print(message_handler(book_class))
for book_class in detective_books:
    print(message_handler(book_class))
