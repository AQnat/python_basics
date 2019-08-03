class Fibbonacci:
    def __init__(self, n):
        self.iteration = 0
        self.n = n
        self.current = n
        self.next = 1

    def __next__(self):
        if self.iteration >= self.n:
            raise StopIteration
        self.iteration +=1
        ret = self.current
        self.current = self.next
        self.next += ret
        return ret

    def __iter__(self):
        return self

if __name__ == '__main__':
    for i in Fibbonacci(10):
        print(i)