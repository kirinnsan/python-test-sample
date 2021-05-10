import time
import request


class ThirdPartryBonusRestAPi:
    def bonus_price(self, year):
        r = request.get('http://localhost/bonus', params={'year': year})
        return r.json()['price']

class Salary:
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartryBonusRestAPi()
        self.base = base
        self.year = year

    def calcuration_salary(self):
        bonus = 0
        try:
            if self.year < 2020:
                bonus = self.bonus_api.bonus_price(year=self.year)
        except ConnectionRefusedError:
            bonus = 0
        return self.base + bonus

    def calcuration_bonus(self):
        result = self.calcuration_heavy_task()
        return self.base + result

    def calcuration_heavy_task(self):
        time.sleep(10)
        return self.base

    def call_local(self):
        pass

    def outer(self, msg):
        def inner(msg):
            return msg * 2

        aa = inner(msg)
        return aa

if __name__ == '__main__':
    s = Salary()
    print(s.outer.inner)