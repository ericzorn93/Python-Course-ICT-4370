class MyClass(object):
    # Class Attribute
    age = 22

    def __init__(self, name):
        # Instance Attribute
        self.name = name

def main():
    me = MyClass("Eric")
    robert = MyClass("Robert")
    print(me.name)
    print(me.age)

    print(robert.name)
    print(robert.age)
    

if __name__ == "__main__":
    main()