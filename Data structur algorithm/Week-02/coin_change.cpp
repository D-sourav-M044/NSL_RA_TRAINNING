#include<bits/stdc++.h>
using namespace std;
#define inf 100000
int c[inf];
int mem[25][25];
int n;

int f(int i,int w)
{
    if(w<0)
        return inf;
    if(i==n)
    {
        if(w==0) return 0;
        return inf;
    }
    if(mem[i][w]!=-1)
        return mem[i][w];
    int rslt1 = 1+f(i+1,w-c[i]);
    int rslt2 = f(i+1,w);
    mem[i][w] = min(rslt1,rslt2);

    return mem[i][w];

}

int main()
{

}
