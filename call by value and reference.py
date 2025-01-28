def call_by_value(x):
    print("Inside call_by_value before modification:", x)
    x = 10
    print("Inside call_by_value after modification:", x)

def call_by_reference(lst):
    print("Inside call_by_reference before modification:", lst)
    lst.append(4)
    print("Inside call_by_reference after modification:", lst)

a = 5
print("Before call_by_value function call:", a)
call_by_value(a)
print("After call_by_value function call:", a)
print("-" * 40)

my_list = [1, 2, 3]
print("Before call_by_reference function call:", my_list)
call_by_reference(my_list)
print("After call_by_reference function call:", my_list)
