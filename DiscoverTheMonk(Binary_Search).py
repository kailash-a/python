#!/usr/bin/env python

# HackerEarth codeMonk(SearchingQ1)
##You are given an array A of size N, and Q queries to deal with.
##For each query, you are given an integer X, and you're supposed to find
##out if X is present in the array A or not.
##Input:
##The first line contains two integers, N and Q, denoting the size of array A
##and number of queries. The second line contains N space separated integers,
##denoting the array of elements Ai. The next Q lines contain a single integer X
##per line.
##Output:
##For each query, print YES if the X is in the array, otherwise print NO.

def binarySearch(arr,length,n):
    kmin=0;
    kmax=length-1
    while(kmin<=kmax):
        mid=(kmin+kmax)/2
        if(arr[mid]==n):
            return True
        elif(arr[mid]<n):
            kmin+=1
        else:
            kmax-=1
    return False;

   
N,Q=raw_input().split();
length=int(N)
queries=int(Q)
arr=list(map(int, raw_input().strip().split(" ")))
arr.sort()
for i in range(queries):
    n=input()
    if(binarySearch(arr,length,n)):
        print("YES")
    else:
        Print("NO")


