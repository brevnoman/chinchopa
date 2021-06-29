class NeBoss(Exception):
    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def ne_tot_boss(cls):
        return cls("This is not a boss")


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

    @property
    def boss_company(self):
        return self._company

    @boss_company.setter
    def boss_company(self, value):
        self._company = value

    def __repr__(self):
        return f"{self._name}"



class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self._name = name
        self._company = company
        self._boss = self.__validate(boss)
        boss.workers.append(self)

    def __validate(self, boss):
        if isinstance(boss, Boss):
            return boss
        else:
            raise NeBoss.ne_tot_boss()

    @property
    def worker_name(self):
        return self._name

    @worker_name.setter
    def worker_name(self, value):
        self._name = value

    @property
    def worker_company(self):
        return self._company

    @worker_company.setter
    def worker_company(self, value):
        self._company = value

    @property
    def worker_boss(self):
        return self._company

    @worker_boss.setter
    def worker_boss(self, value: Boss):
        if isinstance(value, Boss):
            self._boss.workers.remove(self)
            self._boss = value
            value.workers.append(self)
        else:
            raise NeBoss.ne_tot_boss()

    def __repr__(self):
        return f"{self._name}"


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
