
class Algorithm():
    algorithms = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.algorithms.append(cls())

    @classmethod
    def buy(cls, **kwargs):
        print(f"Algorithm.buy called with {kwargs}")
        for algorithm in cls.algorithms:
            algorithm.buy(**kwargs)

    @classmethod
    def sell(cls, **kwargs):
        print(f"Algorithm.sell called with {kwargs}")
        for algorithm in cls.algorithms:
            algorithm.sell(**kwargs)


class MyAlgorithm(Algorithm):
    def buy(self, **kwargs):
        print(f"MyAlgorithm.buy called with {kwargs}")


class MyOtherAlgorithm(Algorithm):
    def buy(self, **kwargs):
        print(f"MyOtherAlgorithm.buy called with {kwargs}")


if __name__ == "__main__":
    Algorithm.buy(stock="AAPL",amount=10)
