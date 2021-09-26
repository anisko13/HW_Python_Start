import time

my_list = [0, 5, 2, 4, 7, 1, 3, 19]

nechet_list = (list(filter(
    lambda x: x % 2 == 1,
    my_list
)))
print(len(nechet_list))

counter = 0

while True:
    print(1)
    time.sleep(5)

for item in my_list:
    if item % 2 == 1:
        counter += 1
print(counter)