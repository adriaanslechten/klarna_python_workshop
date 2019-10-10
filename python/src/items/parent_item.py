import abc

class ParentItem(abc.ABC):

    @abc.abstractmethod
    def update(self):
        pass