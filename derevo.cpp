#include <iostream>

struct ListNode
{
    int key;
    int data[3];
    ListNode *left;
    ListNode *right;
    ListNode *p;
};

ListNode * search(ListNode *root, int key)
{
    ListNode *NIL = nullptr;
    if (root == NIL or key == root->key)
    {
        return root;
    }
    if (key < root->key)
    {
        return search(root->left, key);
    }
    else
    {
        return search(root->right, key);
    }
}

ListNode * find_minimum(ListNode *root)
{
    ListNode *NIL = nullptr;
    while (root->left != NIL)
    {
        root = root->left;
    }
    return root;
}

ListNode * find_maximum(ListNode *root)
{
    ListNode *NIL = nullptr;
    while (root->right != NIL)
    {
        root = root->right;
    }
    return root;
}

struct SimpleTree
{
    ListNode *root;
};

void insert(ListNode *root, ListNode *z)
{
    ListNode *NIL = nullptr;
    ListNode *y = nullptr;
    while (root != NIL)
    {
        y = root;
        if (z->key < root->key)
        {
            root = root->left;
        }
        else
        {
            root = root->right;
        }
    }
    z->p = y;
    if (y == NIL)
    {
        root = z;
    }
    else if (z->key < y->key)
    {
        y->left = z;
    }
    else
    {
        y->right = z;
    }
}

void transplant(ListNode *root, ListNode *u, ListNode *v)
{
    ListNode *NIL = nullptr;
    if (u->p == NIL)
    {
        root = v;
    }
    else if (u == u->p->left)
    {
        u->p->left = v;
    }
}

void deletee(ListNode *root, ListNode *z)
{
    ListNode *y = nullptr;
    ListNode *NIL = nullptr;
    if (z->left == NIL)
    {
        transplant(root, z, z->right);
    }
    else if (z->right == NIL)
    {
        transplant(root, z, z->left);
    }
    else
    {
        y = find_minimum(z->right);
        if (y->p != z)
        {
            transplant(root, y, y->right);
            y->right = z->right;
            y->right->p = y;
        }
        transplant (root, z, y);
        y->left = z->left;
        y->left->p = y;
    }
}

int main()
{
    return 0;
}
