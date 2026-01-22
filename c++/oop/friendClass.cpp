#include<iostream>
using namespace std;
class Complex; 
class Calculator {
    public:
        int add(int a, int b){
            return a+b;
        }
        int sumRealComplex(Complex, Complex );
        int sumCompComplex(Complex, Complex );
};
class Complex {
    int a, b;
    friend class Calculator;
    // friend int Calculator::sumRealComplex(Complex o1, Complex o2);
    // friend int Calculator::sumCompComplex(Complex o1, Complex o2);
    public: 
        void setNumber(int v1, int v2){
            a = v1;
            b = v2;
        }
        void printNumber(){
            cout<<a<<" + "<<b<<"i"<<endl;
        }
};

int Calculator :: sumRealComplex(Complex o1, Complex o2){
    return o1.a + o2.a;
}
int Calculator :: sumCompComplex(Complex o1, Complex o2){
    return o1.b + o2.b;
}

int main(){
    Complex o1, o2;
    o1.setNumber(2, 5);
    o2.setNumber(4, 6);
    Calculator calc;
    int res = calc.sumRealComplex(o1, o2);
    cout<<res<<endl;
    int resc = calc.sumCompComplex(o1, o2);
    cout<<resc<<endl;
}