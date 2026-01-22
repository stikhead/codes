import 'dart:io';

void main() {
  stdout.write("Enter three numbers: ");
  int num1 = int.parse(stdin.readLineSync()!);
  int num2 = int.parse(stdin.readLineSync()!);
  int num3 = int.parse(stdin.readLineSync()!);
  if (num1 > num2 && num1 > num3) {
    print("First number is greater");
  } else {
    if (num2 > num3) {
      print("Second number is greater");
    } else {
      print("Third number is greater");
    }
  }
}
