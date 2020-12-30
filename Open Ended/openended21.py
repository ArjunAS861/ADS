def main():
    L=int(input())
    R=int(input())
    
    for i in range(L,R+1):
        if len(set(str(i))) == len(str(i)):
            print(i,end=" ")
main()