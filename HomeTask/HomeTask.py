my_list = [7, 5, 4, 4, 3]
my_list2 = [7, 5, 4, 4, 3]
def sort_list_imperativ(arr):
    for j in range(len(arr)):

        for i in range(j+1, len(arr)):
            if arr[j] < arr[i]:
                item = arr[j]
                arr[j] = arr[i]
                arr[i] = item
    print(arr)


def sort_list_declarativ(arr):
    arr.sort(reverse=True)
    print(arr)

sort_list_declarativ(my_list)

sort_list_imperativ(my_list2)