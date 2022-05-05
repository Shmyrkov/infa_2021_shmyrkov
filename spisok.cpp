#include <iostream>
using namespace std;

struct Node 
{
    int val;
    Node *next;
    Node(int value, Node *next_node) 
    {
        val = value;
        next = next_node;
    }
    ~Node() 
    {
        val = 0;
        next = nullptr;
    }
};

struct List 
{
    unsigned size = 0;
    Node *first;
    Node *last;
    void push_back (int new_val) 
    {
        Node *p = new Node(new_val, nullptr);
        if (size == 0) 
        {
            last = p;
            first = p;
        }
        else 
        {
            last->next = p;
            last = p;
        }
        size++;
    }
    void push_front (int new_val) 
    {
        Node *p = new Node(new_val, nullptr);
        if (size == 0) 
        {
            last = p;
            first = p;
        }
        else 
        {
            p->next = first;
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
        Node* p = first;
        while (p->next != last) p = p->next;
        p->next = nullptr;
        delete last;
        last = p;
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
    
    void remove(int idx)
    {
        if (size == 0) return;
        if (idx == 0)
        {
            Node* p = first->next;
            delete first;
            first = p;
            size--;
            return;
        }
        Node* p = first;
        for (int i = 0; i < idx - 1; i++)
        {
            p = p->next;
        }
        Node* del = p->next;
        p->next = del->next;
        delete del;
        delete p;
        size--;
    }
    
    void clear()
    {
        while(first)
        {
            Node* p = first->next;
            delete first;
            first = p;
        }
    }
    
    Node& operator[](int i) 
    {
        Node* p = first;
        for (int j = 0; j < i; j++) {
            p = p->next;
        }
        delete p;
        return (*p);
    }
    
    void insert(int new_val, int idx)
    {
        if (size == 0 or idx == 0) 
        {
            this->push_front(new_val);
            return;
        }
        if (idx == size) {
            this->push_back(new_val);
            return;
        }
        Node *p = new Node(new_val, &(*this)[idx]);
        (*this)[idx-1].next = p;
        size++;
        delete p;
    }

};

int main() 
{
    List l;
    l.push_front(3);
    l.push_front(5);
    l.push_front(9);
    l.print();
    l.clear();
    l.print();
    l.push_front(3);
    l.push_front(5);
    l.push_front(9);
    l.insert(15, 0);
    l.print();
    
}
