# 이니셜(숫자) 하나만 받고 리스트 이름 출력하는 애

a_list = [1, 2, 3]
b_list = [4, 5, 6]
c_list = [7, 8, 9]

list_0 = [a_list, b_list, c_list]

def get_list_by_initial(initial):
    for lst in list_0:
        if str(lst[0]).lower() == initial.lower():
            return lst
    return None

initial = input("Enter the initial: ")

result_list = get_list_by_initial(initial)

if result_list:
    print("{}_list: {}".format(initial, result_list))
else:
    print("No list found with the initial '{}'".format(initial))
