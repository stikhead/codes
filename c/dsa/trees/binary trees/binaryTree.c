#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node * left;
    struct Node * right;
};

void preOrder(struct Node * p){
    if(p!=NULL){
        printf("%d ", p->data);
        preOrder(p->left);
        preOrder(p->right);
    }
}

void postOrder(struct Node * p){
    if(p!=NULL){
        preOrder(p->left);
        preOrder(p->right);
        printf("%d ", p->data);
    }
}
void inOrder(struct Node * p){
    if(p!=NULL){
        preOrder(p->left);
        printf("%d ", p->data);
        preOrder(p->right);
    }
}
int main(){
    struct Node * p = (struct Node *)malloc(sizeof(struct Node));
    struct Node * p1 = (struct Node *)malloc(sizeof(struct Node));
    struct Node * p2 = (struct Node *)malloc(sizeof(struct Node));
    p->left = p1;
    p->right = p2;
    p->data = 4;
    p1->left = NULL;
    p1->right = NULL;
    p1->data = 8;
    p2->left = NULL;
    p2->right = NULL;
    p2->data = 16;
    postOrder(p);
    printf("\n");
    
    preOrder(p);
    printf("\n");
    
    inOrder(p);
    printf("\n");
}