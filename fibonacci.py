def fibonacci(i):   #число, до которого будет список
    def list(i): #делает список чисел Фибоначчи
        seq = [0, 1]
        while seq[-1] < i:
            seq.append(seq[-2] + seq[-1])
        return seq[:-1]
    z = list(i)
    def p_even(i): # возвращает четные элементы из списка
        return [x for x in z if not x % 2]
    return p_even(i)

print(fibonacci(1000))
