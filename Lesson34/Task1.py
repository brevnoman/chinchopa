from threading import Thread

class Counter(Thread):
    counter = 0
    rounds = 100000

    @classmethod
    def run(cls):
        for _ in range(cls.rounds):
            cls.counter += 1



if __name__ == '__main__':
    count = Counter()
    count.start()
    count.run()
    count.join()

    print(Counter.counter)

# from time to time got different answers like 186912 or 149072 think it's because of using one memory block