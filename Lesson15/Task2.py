class Boss:

    def __init__(self, id_, name: str, company: str):
        self._id = id_
        self._name = name
        self._company = company
        self.workers = []

    @property
    def boss_name(self):
        return self._name

    @boss_name.setter
    def boss_name(self, value):
        self._name = value

    @boss_name.getter
    def boss_name(self):
        return self._name

    @property
    def boss_company(self):
        return self._company

    @boss_company.setter
    def boss_company(self, value):
        self._company = value

    @boss_company.getter
    def boss_company(self):
        return self._company


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self._name = name
        self._company = company
        self._boss = boss
        boss.workers.append(self)

    @property
    def worker_name(self):
        return self._name

    @worker_name.setter
    def worker_name(self, value):
        self._name = value

    @worker_name.getter
    def worker_name(self):
        return self._name

    @property
    def worker_company(self):
        return self._company

    @worker_company.setter
    def worker_company(self, value):
        self._company = value

    @worker_company.getter
    def worker_company(self):
        return self._company

    @property
    def worker_boss(self):
        return self._company

    @worker_boss.setter
    def worker_boss(self, value: Boss):
        self._boss.workers.remove(self)
        self._boss = value
        value.workers.append(self)

    @worker_boss.getter
    def worker_boss(self):
        return self._company


print("do")
boss1 = Boss(1, "name", "comp")
boss2 = Boss(2, "na", "corp")
worker = Worker(3, "Jora", "corp", boss2)
print(boss1.boss_name)
print(boss2.__dict__)
print(boss1.__dict__)
print(worker.__dict__)

worker.worker_boss = boss1
print("posle")
print(boss2.__dict__)
print(boss1.__dict__)
print(worker.__dict__)
