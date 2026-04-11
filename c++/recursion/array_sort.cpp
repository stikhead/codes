#include<bits/stdc++.h>

using namespace std;
void insert(vector<int> &arr, int temp){
    if(arr.size()==0 || arr[arr.size()-1]<=temp){
        arr.push_back(temp);
        return;
    }
    int t = arr[arr.size()-1];
    arr.pop_back();
    insert(arr, temp);
    arr.push_back(t);
}
void sort(vector<int>& arr){
    if(arr.size()==1){
        return;
    }
    int temp = arr[arr.size()-1];
    arr.pop_back();
    sort(arr);
    insert(arr, temp);
}
int main(){
    vector<int> arr = {1, 0, 5, 3, 2, 5};
    sort(arr);
    for(auto i: arr){
        cout<<arr[i]<< " ";
    }
}