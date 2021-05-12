import time
import request
from datetime import datetime


class ThirdPartryBonusRestAPi:
    def bonus_price(self, year):
        r = request.get('http://localhost/bonus', params={'year': year})
        return r.json()['price']

    def last_three_salary_list(self):
        return self

    def max_salary(self, salary_list):
        return max(salary_list)


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

    def get_max_salary(self):
        max_salary = self.bonus_api.last_three_salary_list().max_salary([90, 80, 30])
        return max_salary

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

    def now_time(self):
        name = time.time()
        return f"name_{name}"

    def now_date_time(self):
        name = datetime.now()
        return f"name_{name}"

    def now_date_time_utc(self):
        name = datetime.utcnow()
        return f"name_{name}"

    def datetime_method_cahin(self):
        name = datetime.now().date().strftime('%Y-%m-%d')
        return f"name_{name}"

if __name__ == '__main__':
    s = Salary()
    print(s.outer.inner)