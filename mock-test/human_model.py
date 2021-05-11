class HumanModel:

    def insert(self):
        print('called insert')
        self.connect_db()

    def update(self):
        print('called update')
        self.connect_db()

    def read(self):
        print('called read')
        self.connect_db()

    def delete(self):
        print('called delete')
        self.connect_db()

    def connect_db(self):
        raise ConnectionError()


class Human:
    def _regist(self):
        model = HumanModel()
        model.name = 'taro'
        model.age = 20
        model.sex = '男'
        model.insert()

    def _update(self):
        self._regist()

        model = HumanModel()
        model.name = 'kaoru'
        model.age = 23
        model.sex = '女'
        model.update()
