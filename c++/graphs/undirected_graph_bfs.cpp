#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> matrix = {
        {0, 1, 1, 0},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {0, 1, 1, 0},
    };

 
void bfsWithMatrix(vector<vector<int>> &matrix, int startNode){

    vector<int> visited(4, 0); 
    int m = matrix.size();
    int n = matrix[0].size();
    queue<int> q;
    q.push(startNode);
    visited[startNode] = 1;
    while(!q.empty()){
        int size = q.size();
        for(int i=0; i<size; i++){
            int node = q.front();
            q.pop();
            for(int j=0; j<visited.size(); j++){
                if(matrix[node][j]==1 && !visited[j]){
                    visited[j] = 1;
                    q.push(j);
                }
            }
        }
    }
}
void bfsWithList(vector<vector<int>> &list, int startNode){
    int size = list.size();
    vector<int> visited(size, 0);
    queue<int> q;
    q.push(startNode);
    visited[startNode] = 1;
    while(!q.empty()){
        int size = q.size();
        for(int i=0; i<size; i++){
            int node = q.front();
            q.pop();
            for(int j=0; j<list[node].size(); j++){
                if(!visited[list[node][j]]){
                    visited[list[node][j]] = 1;
                    q.push(list[node][j]);
                }
            }
        }         
    }
}
int V = 5; // Total nodes: 0, 1, 2, 3, 4
vector<vector<int>> edges = {
    {0, 1}, // Edge between 0 and 1
    {0, 2}, // Edge between 0 and 2
    {1, 3}, // Edge between 1 and 3
    {2, 3}, // Edge between 2 and 3
    {3, 4}  // Edge between 3 and 4 (The "Tail")
};

void bfsWithEdges(vector<vector<int>> &edges, int startNode){
    vector<int> visited(V, 0);
    queue<int> q;
    q.push(startNode);
    visited[startNode] = 1;
    while(!q.empty()){
        int size = q.size();
        for(int i=0; i<size; i++){
            int node = q.front();
            q.pop();
            for(int j=0; j<edges.size(); j++){
                if(edges[j][0]==node && !visited[edges[j][1]]){
                    visited[edges[j][1]] = 1;
                    q.push(edges[j][1]);
                } else if(edges[j][1]==node && !visited[edges[j][0]]){
                    visited[edges[j][0]] = 1;
                    q.push(edges[j][0]);
                }
            }
        }
    }
}
int main(){
    
}