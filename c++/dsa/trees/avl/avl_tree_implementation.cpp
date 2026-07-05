#include<bits/stdc++.h>
using namespace std;

class Node {
    public: 
        int val, height;
        Node * left, * right;
        Node(int v){
            val = v;
            height = 1;
            left = nullptr;
            right = nullptr;
        }
};

int getHeight(Node*root){
    if(!root) return 0;
    return root->height;
}

int getbalance(Node*root){
    return getHeight(root->left) - getHeight(root->right);

}

Node * rightRotation(Node * root){
    Node * child = root->left;
    Node * childRight  = child->right;
    child->right = root;
    root->left = childRight;
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    child->height = 1 + max(getHeight(child->left), getHeight(child->right));
    return child;
}

Node * leftRotation(Node * root){
    Node * child = root->right;
    Node * childLeft  = child->left;
    child->left = root;
    root->right = childLeft;
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    child->height = 1 + max(getHeight(child->left), getHeight(child->right));
    return child;
}

Node * insert(Node*root, int key){
    if(!root) {
        return new Node(key);
    } else if(key > root->val){
        root->right = insert(root->right, key);
    } else if(key < root->val){
        root->left = insert(root->left, key);
    } else {
        return root;
    }

    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    int balance = getbalance(root);
    if(balance > 1 && root->left->val > key){
        return rightRotation(root);
    } else if(balance < -1 && root->right->val < key){
        return leftRotation(root);
    } else if(balance > 1 && root->left->val < key){
        root->left = leftRotation(root->left);
        return rightRotation(root);
    } else if(balance < -1 && root->right->val > key){
        root->right = rightRotation(root->right);
        return leftRotation(root); 
    } 

    return root;


}

void inorder(Node * root){
    if(root){
        inorder(root->left);
        cout<<root->val<<" ";
        inorder(root->right);
    }
}
int main(){
    Node * root = nullptr;
    for(int i=0; i<10; i++){
        root = insert(root, i);
    }

    inorder(root);


}