class BubbleSort:
    def __init__(self, lst, ascending=True):
        self.lst = lst
        self.ascending = ascending

    def sort(self):
        for i in range(len(self.lst) - 1):
            for j in range(len(self.lst) - 1 - i):
                num1 = self.lst[j]
                num2 = self.lst[j + 1]

                if (num1 > num2 and self.ascending) or (num1 < num2 and not self.ascending):
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    yield True
        return self.lst
