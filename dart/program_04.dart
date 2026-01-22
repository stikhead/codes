import 'dart:io';

void main() {
  print("Enter number: ");
  int num1 = int.parse(stdin.readLineSync()!);
  print("Enter Name: ");
  String name = stdin.readLineSync()!;
  print("Enter decimal");
  double decimal = double.parse(stdin.readLineSync()!);
  var sum = 10 + num1;
  print(sum);
  print(name);
  print(decimal);
}
