#include<bits/stdc++.h>
using namespace std;

void insert(stack<int> &st, int &temp){
    if(st.size()==0){
        st.push(temp);
        return;
    }
    int t = st.top();
    st.pop();
    if(t>=temp){
        st.push(t);
        st.push(temp);
        return;
    }
    insert(st, temp);
    st.push(t);
    
}
void sort(stack<int> &st){
    if(st.size()==1){
        return;
    }
    int temp = st.top();
    st.pop();
    sort(st);
    insert(st, temp);
}


int main(){
    stack<int> st({2, 3, 1});
    // {2, 1}
    // {2} 1
    sort(st);
    for(int i= 0; i<3; i++){
        cout<< st.top()<< " ";
        st.pop();
    }
}