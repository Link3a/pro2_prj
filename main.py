import datetime as dt


def str_to_date(self_date, other_date):
    dt1 = self_date.split('.')               # (data)
    dt2 = other_date.split('.')
    self_date = dt.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_date = dt.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_date, other_date


class Employee:
    def __init__(self, number, fio, bdate, oklad, on_leave = False):
        self.number = number
        self.fio = fio
        self.bdate = bdate
        self.oklad = oklad
        self.on_leave = on_leave

    def increase_salary(self, summa):
        self.oklad += summa

    def __str__(self):
        return f"Сотрудник {self.number} {self.fio} {self.bdate} оклад {self.oklad}, в отпуске: "\
               f"{'да' if self.on_leave else 'нет'}"

    def __lt__(self, other):     # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):     # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):     # <=
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        else:
            return False


petrov = Employee(1, "Петров А.А.", "12.11.1998", 50000)
smirnov = Employee(1, "Смирнов П.Р.", "22.04.2000", 46000)
print(petrov < smirnov)
print(petrov <= smirnov)
print(petrov == smirnov)