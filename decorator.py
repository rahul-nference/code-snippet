# bad
class TextProcessor:
    def __init__(self, text):
        self.text = text
    @abstractmethod
    def process(self):
        pass

class LowerCaseTextProcessor(TextProcessor):
    def process(self):
        return self.text.lower()
    
class StripTextProcessor(TextProcessor):
    def process(self):
        return self.text.strip()
    
##################################################
# Using decorators
from abc import ABC, abstractmethod

class TextProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

class ConcreteTextProcessor(TextProcessor):
    def __init__(self, text):
        self.text = text

    def process(self):
        return self.text

class LowerCaseDecorator(TextProcessor):
    def __init__(self, processor):
        self.processor = processor

    def process(self):
        return self.processor.process().lower()

class StripDecorator(TextProcessor):
    def __init__(self, processor):
        self.processor = processor

    def process(self):
        return self.processor.process().strip()

# Client code
processor = ConcreteTextProcessor(" Hello World! ")
print(processor.process())  # " Hello World! "

processor = LowerCaseDecorator(processor)
print(processor.process())  # " hello world! "

processor = StripDecorator(processor)
print(processor.process())  # "hello world!"