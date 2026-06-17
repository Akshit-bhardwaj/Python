# *args , **kwargs


def add(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(add(1 , 2 ,3 , 4))    



def keyword_args(**kwargs):
    return kwargs
print(keyword_args(a = 10 , b = 20  , c= 30))