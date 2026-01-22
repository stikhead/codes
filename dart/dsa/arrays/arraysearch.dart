int binarySearch(List<int> arr, int size, int value) {
  int left = 0;
  int right = size - 1;
  while (left <= right) {
    int mid = ((left + right) / 2).round();
    if (arr[mid] == value) {
      return mid;
    }
    if (arr[mid] < value) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

void main() {
  List<int> arr = [1, 3, 7, 4, 5, 6];
  print(binarySearch(arr, 6, 6));
}
