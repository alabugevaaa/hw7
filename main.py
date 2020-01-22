import datetime, time

# играем в прятки
class HideAndSeek:

    def __init__(self, count):
        self.count = count
        self.start = datetime.datetime.now()
        print(f'>Старт - {self.start}')

    def __enter__(self):
        for i in range(1, self.count):
            print(i)
            time.sleep(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.count} - Я иду искать!')
        self.end = datetime.datetime.now()
        print(f'>Окончание - {self.end}')
        print(f'>Затрачено времени - {self.end - self.start}')

if __name__ == '__main__':
    with HideAndSeek(5):
        pass