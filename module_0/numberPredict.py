import numpy as np

def numberPredict(minimum=1, maximum=1000):
    '''Использую алгоритм бинарного поиска для минимализации количества попыток (count) поиска 
    рандомного числа в диапазоне от 'minimum' до 'maximum' '''
    count   = 1
    predict = np.random.randint( minimum, maximum+1 )
    start   = minimum
    end     = maximum
    while True:
        mid = (start + end) // 2
        if predict < mid:
            end = mid
        elif predict > mid:
            start = mid
        elif predict == mid:
            return count
            break
        count += 1