# алгоритм
# #
# # Big o -
#
#
# # O(10n)=O(n)
# print(1+5)
# n=0
# n1=8
# print(n+n1)
#
#
# for i in range(1,10):
#     print(i)
#
#
# # O(n2)
# while 1:
#     while 1:...
#
# while 9:...
# # O(B)


l=[]
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True





# def foo(a):
#     def foo2(a):
#         foo(foo2())
