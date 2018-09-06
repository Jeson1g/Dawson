
def add_params(params):

    def my_decorator(func):

        def wrapper(*args,**kwargs):
            print("装饰器{}".format(params))
            return func(*args,**kwargs)

        return wrapper

    return my_decorator

if __name__ == '__main__':

    @add_params(1)
    def test1(num,num2):

        return num + num2

    nums = test1(1,2)
    print(nums)