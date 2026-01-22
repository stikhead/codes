class MyArray {
  late int tsize;
  late int usize;
  late List<int> ptr;

  MyArray(int x, int y) {
    tsize = x;
    usize = y;
    ptr = List<int>.filled(tsize, 0);
  }

  void setVal() {
    for (int i = 0; i < usize; i++) {
      ptr[i] = i * i;
    }
  }

  void display() {
    for (int i = 0; i < usize; i++) {
      print(ptr[i]);
      print(" ");
    }
  }
}

void main() {
  MyArray arr = MyArray(10, 5);
  arr.setVal();
  arr.display();
}
