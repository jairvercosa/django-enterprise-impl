import abc


class IUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass
