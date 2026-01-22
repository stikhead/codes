class Node {
  int data;
  Node? next;
  Node(this.data);
}

void traversal(Node? head) {
  while (head != null) {
    print(head.data);
    head = head.next;
  }
}

void main() {
  Node head = Node(8);

  Node second = Node(8);

  Node third = Node(8);
  head.next = second;
  second.next = third;
  third.next = null;
  traversal(head);
}
