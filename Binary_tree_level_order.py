
def test(list, x):
    list.append(x)

def test2(a, x):
    a = x
    print 'in test2', a

a = []
test(a, 5)
test(a, 10)
test(a, 15)
print a

b = 1
test2(b,10)
print b

a[4] = 1
