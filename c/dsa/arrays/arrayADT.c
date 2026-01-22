#include<stdio.h>
#include<stdlib.h>
struct myArray {
    int size;
    int used;
    int *ptr;
};

void createArray(struct myArray* arr, int tsize, int usize){
    (*arr).size = tsize;
    (*arr).used = usize;
    (*arr).ptr = ( int*) malloc (tsize*sizeof(int));
}

void setVal(struct myArray* arr){
    int n;
    for(int i=0; i<arr->used; i++){
        scanf("%d\n", &n);
        (arr->ptr)[i]=n;
    }
}

void show(struct myArray* arr){
    for(int i=0; i<arr->used; i++){
        printf("%d\n", (arr->ptr)[i]);
    }
}
int main(){
    struct myArray marks;
    createArray(&marks, 10, 3);
    setVal(&marks);
    show(&marks);
}

