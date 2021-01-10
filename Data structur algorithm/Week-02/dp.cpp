#include<bits/stdc++.h>
using namespace std;

int mem[110];
int f(int n)
{
    if(n==1) mem[n]=0;
    if(n==2) mem[n]=1;
    if(mem[n] == -1)
        mem[n]= f(n-1)+f(n-2);
}

int main()
{
    int n=5;
    memset(mem,-1,110);
    for(int i=1;i<=n;i++)
    {
        f(i);
    }
    for(int i=1;i<=n;i++)
        cout<<mem[i]<<" ";

}
