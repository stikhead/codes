#include<bits/stdc++.h>
using namespace std;



void dfsWithMatrix(vector<vector<int>> &matrix, vector<int> &visited, int node){
    visited[node]=1;
    for(int k = 0; k<matrix.size(); k++){
        if(matrix[node][k]==1 && !visited[k]){
            dfsWithMatrix(matrix, visited, k);

        }
    }
}
vector<vector<int>> l = {
    {1, 2},       // Node 0 is connected to 1 and 2
    {0, 3, 4},    // Node 1 is connected to 0, 3, and 4
    {0, 4},       // Node 2 is connected to 0 and 4
    {1, 4},       // Node 3 is connected to 1 and 4
    {1, 2, 3}     // Node 4 is connected to 1, 2, and 3
};
void dfsWithList(vector<vector<int>> &list, vector<int> &visited, int node, int count){
    visited[node] = 1;
    for(int i=0; i<list[node].size(); i++){
        if(!visited[list[node][i]]){
            dfsWithList(list, visited, list[node][i], max(count, count+1));
        }
    }
}

// retry this in future someday
// void dfsWithEdges(vector<vector<int>> &edges, vector<int> &vis, int node){
//     vis[node] = 1;
//     for(int i=0; i<edges.size(); i++){
//         if(edges[i][0]==node)
//         if(!vis[edges[node][1]]){
//             vis[edges[node][1]] = 1;
//             dfsWithEdges(edges, vis, edges[node][1]);
//         }
//     }
// }

void dfsWithGrid(vector<vector<char>> &grid, int r, int c){
    int m = grid.size();
    int n = grid[0].size();
    if(r<0 || c< 0 || r>=m || c>=0 || grid[r][c]=='0'){
        return;
    }

    grid[r][c] = '0';

    dfsWithGrid(grid, r + 1, c);
    dfsWithGrid(grid, r-1, c);
    dfsWithGrid(grid, r, c+1);
    dfsWithGrid(grid, r, c-1);
    
}
int main(){
    vector<int> vis = {0, 0, 0, 0, 0};
    vis[0] = 1;
    vector<vector<int>> matrix = {
    {0, 1, 1, 0, 0}, // Node 0 connects to 1, 2
    {1, 0, 0, 1, 1}, // Node 1 connects to 0, 3, 4
    {1, 0, 0, 0, 1}, // Node 2 connects to 0, 4
    {0, 1, 0, 0, 0}, // Node 3 connects to 1
    {0, 1, 1, 0, 0}  // Node 4 connects to 1, 2
};
vector<vector<int>> l = {
    {1, 2},       // Node 0 is connected to 1 and 2
    {0, 3, 4},    // Node 1 is connected to 0, 3, and 4
    {0, 4},       // Node 2 is connected to 0 and 4
    {1, 4},       // Node 3 is connected to 1 and 4
    {1, 2, 3}     // Node 4 is connected to 1, 2, and 3
};
vector<vector<int>> edges = {
    {0, 1}, // Edge between 0 and 1
    {0, 2}, // Edge between 0 and 2
    {1, 3}, // Edge between 1 and 3
    {2, 3}, // Edge between 2 and 3
    {3, 4}  // Edge between 3 and 4 (The "Tail")
};
vector<vector<char>> grid = {
    {'1', '1', '0'},
    {'1', '0', '0'},
    {'0', '0', '1'}
};
    dfsWithMatrix(matrix, vis, 0);
    dfsWithList(l, vis, 0, 0);
}