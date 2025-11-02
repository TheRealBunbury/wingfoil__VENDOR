
from wingfoil_internal import Node, ticker 

'''
class BaseStream():

    def __new__(cls, *args, **kwargs):
        """Overriden constructor to wrap this instance 
        in proxy Stream - this is where the magic happens"""
        obj = super().__new__(cls)
        obj.__init__(*args, **kwargs)
        proxy = Stream(obj)
        return proxy

    def __init__(self):
        self._value = None
        self._upstreams = []

    def upstreams(self):
        return self._upstreams

    def cycle(self):
        return True

    def peek(self):
        return self.value


class SimpleStream(BaseStream):

    """simple stream that propogates its source every cycle"""""

    def __init__(self, upstream):
        super().__init__()
        self._upstreams = [upstream]
        self._upstream = upstream

    def cycle(self):
        # snap upstream value
        self.value = self._upstream.peek()
        # Return true to trigger downstreams to cycle
        return True
'''