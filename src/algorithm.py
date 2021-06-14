
class Algorithm():
    algorithms = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        instance = cls()
        Algorithm.algorithms.append(instance)
        cls.algorithms = [instance]

    @classmethod
    def run(cls, chart):
        lst = []
        for i in range(len(chart.candlesticks)):
            for algorithm in cls.algorithms:
                algorithm.buying_rule(chart, i)
                algorithm.selling_rule(chart, i)
                lst.append(algorithm.cash + algorithm.stocks*chart.candlesticks[i])
        return lst

class MyAlgorithm(Algorithm):
    def buying_rule(self, **kwargs):
        print(f"MyAlgorithm.buying_rule called with {kwargs}")


class MyOtherAlgorithm(Algorithm):
    def buying_rule(self, **kwargs):
        print(f"MyOtherAlgorithm.buying_rule called with {kwargs}")


if __name__ == "__main__":
    Algorithm.run(stock="AAPL",amount=10)
    MyAlgorithm.run(stock="AAPL",amount=10)
    MyOtherAlgorithm.run(stock="AAPL",amount=10)
