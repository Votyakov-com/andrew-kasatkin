from functools import reduce

def reduce_sum(List):
    return reduce(lambda number,total:total+number,List)


List_for_sum=[1,2,3,4,5,609]
print(reduce_sum(List_for_sum))