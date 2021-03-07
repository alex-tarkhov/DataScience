import numpy as np

def numberPredict(minimum=1, maximum=100):
    '''Использую алгоритм бинарного поиска для минимализации количества попыток поиска 
    рандомного числа в диапазоне 'minimum' > 'maximum''''
    count   = 1
    predict = np.random.randint( minimum,maximum+1 )
    start   = minimum
    end     = maximum
    result  = None
    while True:
        mid = (start + end) // 2
        if predict < mid:
            end = mid
        elif predict > mid:
            start = mid
        elif predict == mid:
            result = count
            return result
            break
        count += 1

numberPredict()