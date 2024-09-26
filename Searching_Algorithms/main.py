class Searching:
    list1=[]
    size = int(input("Enter size of list: "))
    for i in range(size):
        ele = int(input("Enter element: "))
        list1.append(ele)
    key = int(input("Enter key"))
    Fibol =[0,1]
    for i in range(size):
       Fibol.append(Fibol[i]+Fibol[i+1])
    def Fibo(self, m):
        return self.Fibol[m]
    def Linear(self):
        for i in range(self.size):
            if self.key==self.list1[i]:
                print("Found at ",i)
                return
        print("Not found")
    def Sentinel(self):
        last=self.list1[self.size-1]
        self.list1[self.size-1]=self.key
        i=0
        while self.list1[i]!=self.key:
            i+=1
        self.list1[self.size-1]=last
        if i < self.size or last==self.key:
            print("Found at ",i)
        else:
            print("Not found")
    def Binary(self):
        high=self.size-1
        low=0
        while low<=high:
            mid=int((low+high)/2)
            if self.key==self.list1[mid]:
                print("Found at ",mid)
                return
            elif self.key>self.list1[mid]:
                low = mid+1
            else:
                high = mid - 1
        print("Not found")

    def FiboSearch(self):
        m = 0
        while self.Fibo(m) < self.size:
            m += 1
        offset = -1
        while self.Fibo(m) > 1:
            midd=min(offset+self.Fibo(m-2), self.size-1)
            if self.key == midd:
                print("Found at ", midd)
            elif self.key > midd:
                offset = midd
                m -= 1
            else:
                m -= 2
        if self.list1[offset+1] == self.key and self.Fibo(m-1)==0:
            print("Found at ", offset+1)
        else:
            print("Not found")


if __name__ == '__main__':

    while True:
        s1 = Searching()
        opt = int(input("Enter which search: "))
        if opt == 1:
            s1.Linear()
        elif opt == 2:
            s1.Sentinel()
        elif opt == 3:
            s1.Binary()
        elif opt==4:
            s1.FiboSearch()
        else:
            break