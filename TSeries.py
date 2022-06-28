class TSeries():
    first = None
    parameter = None

    def __init__(self, first=0, parameter=0):
        self.set_first(first)
        self.set_parameter(parameter)

    def set_first(self, first):
        self.first = first

    def set_parameter(self, parameter):
        self.parameter = parameter