
class colorized:
    def __init__(self, color: str):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print('\033[91m')
        elif self.color == 'green':
            print('\033[92m')
        elif self.color == 'yellow':
            print('\033[93m')
        elif self.color == 'blue':
            print('\033[94m')
        elif self.color == 'pink':
            print('\033[95m')
        elif self.color == 'turquoise':
            print('\033[96m')
        else:
            print('\033[0m')

    def __exit__(self, *args, **kwargs):
        print('\033[0m')


with colorized('yellow'):
    print("yellow text")

print("Normal text")

with colorized('red'):
    print("red text")

with colorized('green'):
    print("green text")

with colorized('pink'):
    print("pink text")

with colorized('blue'):
    print("blue text")

with colorized('turquoise'):
    print("turquoise text")


def frange(first, last=None, step=1):
    if last is None:
        last = first
        first = 0

    if step < 0:
        num = first
        while num > last:
            yield num
            num += step

    if step > 0:
        num = first
        while num < last:
            yield num
            num += step


assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')



for i in frange(1, 100, 3.5):
    print(i)