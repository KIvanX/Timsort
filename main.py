
from show_sort import Show_sort
from random import randint
from time import time


def Tim_sort(array):

    def show():
        stack_arr = []
        for arr in stack:
            stack_arr += arr
        now_res = stack_arr + run + array[index:]
        display.show(now_res, [index])

    def bin_insert(array, k):
        n = len(array)
        if k <= array[0]:
            return [k] + array
        a, b = 0, n
        while a != b - 1:
            a, b, = ((a + b) // 2, b) if k > array[(a + b) // 2] else (a, (a + b) // 2)
        return array[:a + 1] + [k] + array[b:]

    def merge(a, b):
        new, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            new.append(a[(i:=i+1)-1] if a[i] <= b[j] else b[(j:=j+1)-1])

        return new + a[i:] + b[j:]

    def balansing(stack):
        if len(stack) == 2 and len(stack[1]) >= len(stack[0]):
            stack = [merge(stack[0], stack[1])]
        elif len(stack) > 2 and (not (len(stack[-3]) > len(stack[-2]) + len(stack[-1])) or
                                 not (len(stack[-2]) > len(stack[-1]))):
            if len(stack[-3]) > len(stack[-1]):
                stack = stack[:-2] + [merge(stack[-2], stack[-1])]
            else:
                stack = stack[:-3] + [merge(stack[-2], stack[-3])] + [stack[-1]]
            stack = balansing(stack)
        return stack

    stack, run, minrun = [], [], 64 if len(array) > 300 else 8
    for index in range(len(array)):
        show()
        run.append(array[index])
        if len(run) > 1 and run[-2] > run[-1]:
            run = bin_insert(run[:-1], run[-1])
            if len(run) >= minrun:
                stack = balansing(stack + [run])
                run = []
    if run:
        stack = balansing(stack + [run])

    while len(stack) > 1:
        stack = stack[:-2] + [merge(stack[-2], stack[-1])]

    return stack[0]


def speed_test():
    for i in range(1, 51):
        n = i * 300
        array = [randint(-10**10, 10**10) for _ in range(n)]
        t0 = time()
        for _ in range(10):
            Tim_sort(array)
        print(n, (time() - t0) / 10)


display = Show_sort(600, 300, show_time=8)
array = [randint(0, 100) for i in range(150)]
new = Tim_sort(array)
display.show(new, wait=True)
