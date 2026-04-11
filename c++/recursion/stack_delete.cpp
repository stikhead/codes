#include<bits/stdc++.h>
using namespace std;

bool deletion(stack<int> &st, int target){
    if(st.size()==0){
        return false;
    }
    if(st.top()==target){
        st.pop();
        return true;
    }
    int t = st.top();
    st.pop();
    bool f = deletion(st, target);
    st.push(t);
    return f;

}
int main(){
    stack<int> st({1, 2, 3, 5});
int size = 4;
    if(deletion(st, 2)){
size = 3;
    };
    
    for(int i=0; i<size; i++){
        cout<<st.top()<<" ";
        st.pop();
    }

}