# Base Class
class A(object):
    def __init__(self, name):
        self.name = name
# Child Class
class B:
    pass
# Second Inherited Child Class (Inherits from A and B)
class C(A, B):
    pass


def main():
    obj1 = C("Eric")
    obj2 = C("Robert")
    print(obj1.name, obj2.name)

if __name__ == "__main__":
    main()