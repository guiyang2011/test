from collections import Iterable

class Function(object):
    def is_instance(self):
        l = list(range(1, 9))
        print("list is {0}".format(l))
        result = isinstance(l, Iterable)
        print("result is {0}".format(result))

    def try_list(self):
        l = list(range(1,9,2))
        l2 = [x*x for x in l]
        print("list 2 is {0}".format(l2))

        l3 = list(range(15))
        l4 = [x*x for x in l3 if x % 2 == 0]
        print("list 4 is {0}".format(l4))

    def try_generator(self):
        l = list(range(9))
        gen = (x for x in l)
        print(next(gen))
        print(next(gen))


def main():
    fun = Function()
    #fun.is_instance()
    #fun.try_list()
    fun.try_generator()

if __name__ == "__main__":
    main()
