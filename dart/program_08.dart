void main() {
  List<int> arr = [1, 2, 3, 4, 5];
  print(arr);
  arr.insert(5, 6);
  print(arr);
  print(arr.contains(4));
  print(arr.length);
  arr.remove(6);
  print(arr);
  arr.insertAll(0, [1, 2, 3, 4]);
  print(arr);
  print(arr.reversed);
}
