#include<bits/stdc++.h>
using namespace std;
#define maxdata 10000
vector<int> edges[maxdata];
vector<int> cost[maxdata];
map<int,int> in;

int main()
{
    int node,line;
    scanf("%d %d",&node,&line);
    for (int i=0;i<line;i++)
    {
        int x,y;
        cin>>x>>y;
        edges[x].push_back(y);
        cost[x].push_back(y);
    }
    cout<<"showing nodes:"<<endl;
    for (int i=1;i<=node;i++)
    {
        cout<<"("<<i<<")"<<"<<";
        for(int j=0;j<edges[i].size();j++)
        {
             cout<<edges[i][j]<<" ";
             in[edges[i][j]]++;
        }

        cout<<endl;
    }
    cout<<" showing indegree & outdegree"<<endl;
    for(int i=1;i<=node;i++)
    {
        cout<<"node "<<i<<" >>"<<"indegree : "<<in[i]<<" "<<" outdegree : "<<edges[i].size()<<endl;
    }
}
