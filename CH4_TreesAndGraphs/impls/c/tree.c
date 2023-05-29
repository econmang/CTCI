#include <stdio.h>

struct node {
    int value;
    struct node* left;
    struct node* right;
};

struct tree {
    struct node root;
};

int main() {
    struct node leaf_1;
    struct node leaf_2;
    struct node root_node;

    leaf_1.value = 1;
    leaf_2.value = 2;
    root_node.value = 0;
    root_node.left = &leaf_1;
    root_node.right = &leaf_2;
    struct tree t1;
    t1.root = root_node;

    printf("ROOT: %d\n", t1.root.value);
    printf("LEFT: %d\n", t1.root.left->value);
    printf("RIGHT: %d\n", t1.root.right->value);

    return 0;
}
