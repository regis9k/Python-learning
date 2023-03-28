#if __name__ == '__main__':
#    n = int(input())

n=5
k=list(range(0,n+1))
k=str(k)
k=k.replace(' ','')
k=k.replace(',','')
len=len(k)
k=k[1:len-1]
print(k)