void traverse(List<int> arr, int size) {
  for (int i = 0; i < size; i++) {
    print('${arr[i]} ');
  }
  print("\n");
}

void indexInsertion(List<int> arr, int size, int cap, int element, int index) {
  if (index >= cap) {
    print("Error!");
  } else {
    arr.add(0);
    for (int i = size - 1; i >= index; i--) {
      arr[i + 1] = arr[i];
    }
    arr[index] = element;
  }
}

void indexDeletion(List<int> arr, int size, int cap, int index) {
  if (index >= cap) {
    print("Error!");
  } else {
    for (int i = index; i < size - 1; i++) {
      arr[i] = arr[i + 1];
    }
  }
}

void main() {
  List<int> arr = [1, 3, 4, 5, 7];
  int size = 5;
  traverse(arr, size);
  indexInsertion(arr, size, 100, 22, 0);
  size++;
  traverse(arr, size);
  indexDeletion(arr, size, 100, 4);
  size--;
  traverse(arr, size);
}
