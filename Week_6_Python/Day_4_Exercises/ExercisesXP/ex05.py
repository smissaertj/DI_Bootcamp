for i in range(1,21):
    print(i)


for i in list(range(1,21)):
    if list(range(1,21)).index(i) % 2 == 0:
        print(i)
