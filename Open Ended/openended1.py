"""Given an array of N distinct elements, the task is to find all elements in array except two greatest elements.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two lines. The first line of input contains an integer N denoting the size of the array. Then in the next line are N space separated array elements.

Output:
For each test case in a new line print the space separated sorted values denoting the elements in array which have at-least two greater elements than themselves.

Constraints:
1<=T<=100
3<=N<=100
1<=A[]<=100

Example:
Input:
2
5
2 8 7 1 5
6
7 -2 3 4 9 -1

Output:
1 2 5
-2 -1 3 4

Explanation:
Test case 1: Largest two elements are 7 and 8. So array left is 1 2 5."""
def greatest(arr):
    return sorted(arr)[:-2]

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        m=list(map(int,input().split()))
        for i in greatest(m):
            print(i,end=" ")
        print()
        

main()