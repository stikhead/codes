#include<stdio.h>

void traversal(int arr[]){
    int size = 5;
    for(int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}
void bubbleSort(int arr[]){
    int size = 5;
    int count = 0;
    for(int i=0; i<size; i++){
        count = 1;
        for(int j=0; j<=size-i-1; j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                count = 0;
            }
        }
        if(count){
            return;
        }
    }
    traversal(arr);
}

int main(){
    int arr[5] = {0, 4, 5, 2, 1};
    traversal(arr);
    bubbleSort(arr);
}