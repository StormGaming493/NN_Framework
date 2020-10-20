#import

def iter_2D(iterable):
    for row in iterable:
        for item in row:
            yield item
