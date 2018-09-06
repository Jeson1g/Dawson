class Singleclass(object):
    """单例模式"""

    def __init__(self,num):
        self.num = num

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls,'_isinstance'):
            cls._isinstance = super().__new__(cls)

        return cls._isinstance

    def __str__(self):

        return "my_num{}".format(self.num)

if __name__ == '__main__':
    s1 = Singleclass(3)
    s2 = Singleclass(2)

    print(s1)
    print(s2)