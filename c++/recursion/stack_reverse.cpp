#include<bits/stdc++.h>
using namespace std;

void construct_stack(stack<int> &st, int t){
    if(st.size()==0){
        st.push(t);
        return;
    }
    int temp = st.top();
    st.pop();
    construct_stack(st, t);
    st.push(temp);
}
void reverse(stack<int> &st){
    if(st.size()==0){
        return;
    }
    int t = st.top();
    st.pop();
    reverse(st);
    construct_stack(st, t);
    return;
    

}
int main(){
    stack<int> st({6,4, 5, 3,7,8});
    reverse(st);
    for(int i=0; i<6; i++){
        cout<<st.top()<< " ";
        st.pop();
    }
}

unordered_map<pair<vector<pair<set<int>, int>>, pair<int, vector<vector<int>>>>, int> j;