class A(object):
    count = 0
    def __init__(self, count):
        self.count = count

class B(A):
    def __init__(self, count):
        A.__init__(self, count)

class C(B):
    def __init__(self, count):
        B.__init__(self, count)

def main():
    bb = B(1)
    print(B.count)
    print(bb.count)

    cc = C(2)
    print(cc.count)

if __name__ == "__main__":
    main()