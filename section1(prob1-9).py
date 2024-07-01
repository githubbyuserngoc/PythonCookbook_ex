# 1. swapping values without using  a temporary variable
def prob1():
    a = 10
    b = 20
    c = 30
    c = (b, c, a)

    print(a)
    print(b)
    print(c)

# 2. constructing a dictionary without exessive quoting
def prob2():
    data = {'red' : 1, 'green' : 2, 'blue' : 3}

    def makedict(**kwargs):
        return kwargs
    data = makedict(red = 1, green = 2, blue = 3)

# 3. getting a value from a dictionary
def prob3():
    d = {'key': 'value'}

    if d.has_key('key'):
     'key' in d:
     print(d['key'])
    else:
     print('not found')

#finding the largest or the smallest N item

def prob4():
    import heapq

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
       
       
    ]

