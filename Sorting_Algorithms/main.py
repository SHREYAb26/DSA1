def Insert(list1):
    for i in range(len(list1)):
        temp=list1[i]
        j=i-1
        while j>=0 and list1[j]>temp:
            list1[j+1]=list1[j]
            j -=1
        list1[j+1]=temp
    return list1
def Select(l):
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1,len(l)):
            if l[j]<l[min_idx]:
                min_idx=j
        if min_idx!=i:
            l[i] , l[min_idx] = l[min_idx], l[i]
        print(l)
def parti(lis,low,high):
    pivot=lis[high]
    i=low-1
    for j in range(low,high):
        if lis[j]<pivot:
            i+=1
            lis[i],lis[j]=lis[j],lis[i]
    lis[i+1], lis[high] = lis[high], lis[i+1]
    return i+1


def Quick(li, low, high):
    if low<high:
        pi=parti(li,low,high)
        Quick(li,low,pi-1)
        Quick(li,pi+1,high)

    print(li)
def Bubb(li):
    for i in range(len(li)-1):
        swap=False
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
                swap =True
        if swap == False:
            break
    return li
def Shell(list1):
    inter = int(len(list1)/2)
    while inter >0:
        for i in range(len(list1)):
            temp =list1[i]
            j = i
            while j>=inter and list1[j-inter]>temp:
                list1[j]=list1[j-inter]
                j -= inter
            list1[j]=temp
        inter = int(inter/2)
    return list1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1=[27,76,17,9,45,58,90,79,100]
    Select(list1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
