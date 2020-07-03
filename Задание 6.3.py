class Worker:
    def __init__(self, name, surmane, position, profit, bonus):
        self.name = name
        self.surmane = surmane
        self.position = position
        self._income = {"Прибыль": profit, "Бонус": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surmane}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


manager = Position("Vasya", "Ivanov", "Engineer ", 50000, 10000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())
