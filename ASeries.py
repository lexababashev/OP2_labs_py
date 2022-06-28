
from TSeries import TSeries


class ASeries(TSeries):
    def calculate_n(self, index):
        result = self.first + self.parameter*(index-1)
        return result

    def calculate_sum(self, index):
        last = self.calculate_n(index)
        return int(((self.first + last)/2)*index)