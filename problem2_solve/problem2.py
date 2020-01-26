

if __name__=="__main__":
    n,d = map(int, input().split())
    data = list(map(int, input().split()))
    i=0;
    j=0;
    for i in range(d):
        temp = data[0];
        for j in range(n-1):
            data[j]=data[j+1];
        data[n-1]=temp;
    for sdata in data:
        print(sdata, end=" ");

