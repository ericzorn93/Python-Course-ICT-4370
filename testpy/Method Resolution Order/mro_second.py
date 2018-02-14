# Base Class
class Alpha(object):
    def method(self):
        print("method() from Alpha...")

# Child Class
class Bravo:
    def method(self):
        print("method() from Bravo...")

# Second Inherited Child Class (Inherits from Alpha and Bravo)
class Charlie(Bravo, Alpha):
    def method(self):
        print("method() from Charlie...")


def main():
    obj1 = Charlie()
    obj1.method()

if __name__ == "__main__":
    main()