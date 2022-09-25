#include <iostream>
#include <random>
#include <vector>
#include <iomanip>

using namespace std;

class State
{
public:
    virtual bool contains(int s) const = 0;
};


class DiscreteState : public State {

private:
    int const s0;

public:
    DiscreteState(int s0) : s0(s0) { }
    bool contains(int s) const {
        return s == s0;
    }
};


class SegmentState :public State {

private:
    int const begin_s0, end_s0;

public:
    SegmentState(int begin_s0, int end_s0) : begin_s0(begin_s0), end_s0(end_s0) { }

    bool contains(int s) const {
        return s >= end_s0 and s <= end_s0;
    }
};


class Disj: public State {
private:
    State& lha;
    State& rha;
public:
    Disj(State& lha , State& rha) : lha(lha), rha(rha) { }

    bool contains(int s) const
    {
        return (lha.contains(s) or rha.contains(s));
    }
};

class Conj: public State {
private:
    State& lha;
    State& rha;
public:
    Conj(State& lha, State& rha) : lha(lha), rha(rha) { }

    bool contains(int s) const
    {
        return (lha.contains(s) and rha.contains(s));
    }

};

class Invert : public State {
private:
    SegmentState& lha;

public:
    Invert(SegmentState& lha) : lha(lha) { }

    bool contains(int s) const
    {
        return (not lha.contains(s));
    }

};

class ProbabilityTest {
private:

    unsigned seed;
    int test_min, test_max;
    unsigned test_count;

public:
    ProbabilityTest(unsigned seed, int test_min, int test_max, unsigned test_count) : seed(seed), test_min(test_min), test_max(test_max), test_count(test_count) { }

    float test(State const& s) const {
        default_random_engine rng(seed);
        uniform_int_distribution<int> dstr(test_min, test_max);
        unsigned good = 0;
        for (unsigned cnt = 0; cnt != test_count; ++cnt)
            if (s.contains(dstr(rng))) ++good;

        return static_cast<float>(good) / static_cast<float>(test_count);
    }
};

int main() {
    int a = 1000;
    DiscreteState d(0);
    SegmentState s(0, 300);
    SegmentState s1(5, 15);
    cout << "Task 1: Probability from number of tests " << endl;
    for (int i = 0; i < 20; ++i)
    {
        ProbabilityTest pt(100, 0, 1000, a*i);
        cout << round(pt.test(s) * 1000000) / 1000000;
        cout << setw(10) << a * i << endl;
       
    }
    cout << "Task 2: verification of agreement with theory " << endl;
    ProbabilityTest pt1(100, 0, 1000, 100);
    float с = 300. / 1000;
    cout << "Theoretical probability = " << с << endl;
    cout << "Programming probability = " << pt1.test(s) << endl;
}
