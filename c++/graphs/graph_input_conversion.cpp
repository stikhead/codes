#include<bits/stdc++.h>
using namespace std;
int V = 5;
vector<vector<int>> edges = {
    {0, 1},
    {0, 2},
    {1, 3},
    {1, 4},
    {2, 4}, 
    {3, 4}
};

vector<vector<int>> l = {
    {1, 2},       // Node 0 is connected to 1 and 2
    {0, 3, 4},    // Node 1 is connected to 0, 3, and 4
    {0, 4},       // Node 2 is connected to 0 and 4
    {1, 4},       // Node 3 is connected to 1 and 4
    {1, 2, 3}     // Node 4 is connected to 1, 2, and 3
};

vector<vector<int>> mat = {
        {0, 1, 1, 0},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {0, 1, 1, 0},
    };

void EdgeToMatrix(){
    // matrix = [
    //     0, 1, 2, 3, 4
    //  0 [0, 1, 0, 0, 0]
    //  1 [1, 0, 0, 0, 0]
    //  2 [0, 0, 0, 0, 0]
    //  3 [0, 0, 0, 0, 0]
    //  4 [0, 0, 0, 0, 0]
    //]
    vector<vector<int>> matrix(V, vector<int>(V, 0));
    int m = edges.size(); //  6
    for(int i=0; i<m; i++){
        matrix[edges[i][0]][edges[i][1]] = 1;
        matrix[edges[i][1]][edges[i][0]] = 1;
    }
}

void EdgeToList(){
    vector<vector<int>> list(V);
    vector<int> temp;
    int m = edges.size();
    for(int i=0; i<m; i++){
       int u = edges[i][0];
       int v = edges[i][1];
       list[u].push_back(v);
       list[v].push_back(u);
    }
}

void MatrixToList(){
    int m = mat.size();
    int n = mat.size();
    vector<vector<int>> list(m);
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(mat[i][j]==1){
                list[i].push_back(j);
                // list[j].push_back(i); not needed matrix symmetry will work
            }
        }
    }
}

void ListToMatrix(){
    int size = l.size();
    vector<vector<int>> matrix(size, vector<int>(size, 0));
    for(int i=0; i<size; i++){
        for(int j=0; j<l[i].size(); j++){
            matrix[i][l[i][j]] = 1;
        }
    }
}
int main(){
    

}