"""Копилка"""
class Goal:                                                               # Класс для представления цели
    def __init__(self, name, target_amount, current_balance=0, category=None, status="В процессе"):
        self.name = name
        self.target_amount = target_amount
        self.current_balance = current_balance
        self.category = category
        self.status = status

    def add_money(self, amount):                                           # Пополнить текущий баланс цели
        self.current_balance += amount
        self._update_status()

    def _update_status(self):                                              # Обновить статус цели от текущего баланса
        if self.current_balance >= self.target_amount:
            self.status = "Цель достигнута"
        else:
            self.status = "В процессе"

    def get_progress(self):                                                 # Получить процент выполнения цели
        return (self.current_balance / self.target_amount) * 100 if self.target_amount > 0 else 0

    def to_dict(self):                                                      # Преобразовать объект цели в словарь
        return {
            "Название цели": self.name,
            "Категория цели": self.category,
            "Сумма цели": self.target_amount,
            "Текущий баланс": self.current_balance,
            "Статус цели": self.status
        }

    @classmethod                                                            # Создать объект цели из словаря
    def from_dict(cls, data):
        return cls(
            name=data.get("Название цели"),
            category=data.get("Категория цели"),
            target_amount=data.get("Сумма цели"),
            current_balance=data.get("Текущий баланс", 0),
            status=data.get("Процент выполнения цели", "В процессе")
        )

    def __str__(self):                                                       # Строковое представление объекта цели
        return (f"Название цели: {self.name}\n"
                f"Категория цели: {self.category}\n"
                f"Сумма цели: {self.target_amount} руб.\n"
                f"Текущий баланс: {self.current_balance} руб.\n"
                f"Процент выполнения цели: {self.get_progress():.0f}%\n"
                f"Статус цели: {self.status}")


goal1 = Goal("Покупка автомобиля", 1000000, category="Транспорт")   # Создание цели
goal1.add_money(250000)                                                                # Пополнение баланса
goal1.add_money(250000)                                                                # Пополнение баланса
print(goal1)                                                                           # Вывод информации о цели
print()

goal2 = Goal("Ремонт квартиры", 500000, category="Ремонт")    # Создание цели
goal2.add_money(200000)                                                          # Пополнение баланса
goal2.add_money(200000)                                                          # Пополнение баланса
print(goal2)                                                                     # Вывод информации о цели
print()

goal3 = Goal("Отпуск", 200000, category="Транспорт")          # Создание цели
goal3.add_money(100000)                                                          # Пополнение баланса
goal3.add_money(100000)                                                          # Пополнение баланса
print(goal3)                                                                     # Вывод информации о цели