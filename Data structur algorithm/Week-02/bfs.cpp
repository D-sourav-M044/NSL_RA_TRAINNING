#include<bits/stdc++.h>
using namespace std;
#define mxnode 100
vector<int> graph[mxnode];
int cost[mxnode];
int visit[mxnode];
void bfs(int source)
{
    memset(visit,0,mxnode);
    visit[source]=1;
    cost[source] = 0;
    queue<int> q;
    q.push(source);
    while(!q.empty())
    {
        int node = q.front();
        //cerr<<"front is : "<<next<<endl;
        q.pop();
        for(int i=0;i<graph[node].size();i++)
        {
            int next = graph[node][i];
            if(visit[next]!=1)
            {
                visit[next]=1;
                cost[next]=cost[node]+1;
                q.push(next);
            }
        }
    }
}

int main()
{
    int node,edge;
    cin>>node>>edge;
    for(int i=0;i<edge;i++)
    {
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    cout<<"enter the source : ";
    int source;
    cin>>source;
    cout<<"from the source"<<endl;
    bfs(source);
    for(int i=0;i<node;i++)
    {
        cout<<"from "<<source<<" to "<<i+1<<". The cost is : "<<cost[i+1]<<endl;
    }
}
