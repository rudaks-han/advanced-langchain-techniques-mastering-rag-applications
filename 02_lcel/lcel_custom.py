from abc import ABC, abstractmethod

class CRunnable(ABC):
    def __init__(self):
        self.next = None

    @abstractmethod
    def process(self, data):
        """
        This method must be implemented by subclasses to define
        data processing behavior.
        """
        pass

    def invoke(self, data):
        processed_data = self.process(data)
        if self.next is not None:
            return self.next.invoke(processed_data)
        return processed_data

    def __or__(self, other):
        return CRunnableSequence(self, other)

class CRunnableSequence(CRunnable):
    def __init__(self, first, second):
        super().__init__()
        self.first = first
        self.second = second

    def process(self, data):
        return data

    def invoke(self, data):
        first_result = self.first.invoke(data)
        return self.second.invoke(first_result)

class AddTen(CRunnable):
    def process(self, data):
        print("AddTen: ", data)
        return data + 10

class MultiplyByTwo(CRunnable):
    def process(self, data):
        print("Multiply by 2: ", data)
        return data * 2

class ConvertToString(CRunnable):
    def process(self, data):
        print("Convert to string: ", data)
        return f"Result: {data}"


a = AddTen()
b = MultiplyByTwo()
c = ConvertToString()

chain = a | b | c

result = chain.invoke(10)
print(result)