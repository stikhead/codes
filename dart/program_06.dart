import 'dart:io';

void main() {
  print("Enter a number: ");
  int num1 = int.parse(stdin.readLineSync()!);
  if (num1.isEven) {
    print("The number is even");
  } else {
    print("The number is odd");
  }
}
