def linear_search(list,key):
    for i in range(len(list1)):
        if list1[i]==key:
            print("key elemen found at position:",i+1)
            break
        else:
            print("key element not found in list")
            list1=[10,20,30,574,65]
            key=int(input("enter the key element to search ;"))
            linear_search(list1,key)
