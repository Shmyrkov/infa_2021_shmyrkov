#include <iostream>
using namespace std;

struct Node 
{
    int val;
    Node *next;
    Node *prev;
    Node(int value, Node *next_node, Node *prev_node) 
    {
        val = value;
        next = next_node;
        prev = prev_node;
    }
    ~Node() 
    {
        val = 0;
        next = nullptr;
        prev = nullptr;
    }
};

struct List 
{
    unsigned size = 0;
    Node *first;
    Node *last;
    void push_back (int new_val) 
    {
        Node *p = new Node(new_val, nullptr, nullptr);
        if (size == 0) 
        {
            last = p;
            first = p;
        }
        else 
        {
            last->next = p;
            p->prev = last;
            last = p;
        }
        size++;
    }

    void push_front (int new_val) 
    {
        Node *p = new Node(new_val, nullptr, nullptr);
        if (size == 0) 
        {
            last = p;
            first = p;
        }
        else 
        {
            p->next = first;
            p->prev = nullptr;
            first = p;
        }
        size++;
    }

    void print()
    {
        if (size == 0) return;
        Node* p = first;
        while (p) 
        {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl;
        delete p;
    }

    
    int length()
    {
        return size;
    }
    
    void remove_first() 
    {
        if (size == 0) return;
        Node* p = first;
        first = p->next;
        first->prev = nullptr;
        delete p;
        size--;
    }

    void remove_last() 
    {
        if (size == 0) return;
        if (first == last) {
            remove_first();
            return;
        }
        Node* p = last;
        last = p->prev;
        last->next = nullptr;
        delete p;
        size--;
    }
    
    int get(int idx)
    {
        int index = 0;
        Node* p = first;
        while (index != idx)
        {
            index++;
            p = p->next;
        }
        return p->val;
        delete p;
    }
};

int main() 
{
    List l;
    l.push_front(3);
    l.push_front(5);
    l.push_front(9);
    l.remove_last();
    l.print();
}
