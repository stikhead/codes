import 'dart:io';

void main() {
  print("Enter the name: ");
  String name = stdin.readLineSync()!;
  print("The length of name is: ");
  print(name.length);
}
