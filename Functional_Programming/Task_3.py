def filter_odd(List):
    return list(filter(lambda number:number%2==0,List))


List=map(int,input('Enter some numbers, to check if they are odd: ').split())
print(filter_odd(List))