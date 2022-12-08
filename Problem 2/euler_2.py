prev_1, prev_2 = 1, 0
fibonaccis = []

while prev_1 < 4000000:
    _new = prev_1 + prev_2
    fibonaccis.append(_new)
    prev_2 = prev_1
    prev_1 = _new

answer = sum([number for number in fibonaccis if number % 2 == 0 and number < 4000000])
print(answer)
