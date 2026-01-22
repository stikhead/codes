 #include<iostream>
#include<cmath>
using namespace std;
class SimpleCalculator{
    protected:
        int num1;
        int num2;
    public: 
        void setData(int n1, int n2){
            num1 = n1;
            num2 = n2;
        }
        void display(){
            cout<<"Addition: "<<num1+num2<<endl;
            cout<<"Subtraction: "<<num1-num2<<endl;
            cout<<"Multiply: "<<num1*num2<<endl;
            cout<<"Division: "<<num1/num2<<endl;
        }
};
class ScientificCalculator{
    protected:
        int num1;
        int num2;
    public: 
        void setData(int n1, int n2){
            num1 = n1;
            num2 = n2;
        }
        void display(){
            cout<<"Log: "<<log(num1)<<endl;
            cout<<"sqrt: "<<sqrt(num2)<<endl;
        }
};

class HybridCalc: protected SimpleCalculator, protected ScientificCalculator {
    public:
        void SimpleCalc(int n1, int n2){
            SimpleCalculator::setData(n1, n2);
            SimpleCalculator::display();
        }
         void ScienceCalc(int n1, int n2){
            ScientificCalculator::setData(n1, n2);
            ScientificCalculator::display();
        }
};

int main(){
    cout<<"------------ SIMPLE -------------\n";
    SimpleCalculator simple;
    simple.setData(7, 7);
    simple.display();
    cout<<"------------ SIMPLE -------------\n";

    cout<<"------------ COMPLEX -------------\n";
    ScientificCalculator complex;
    complex.setData(8, 8);
    complex.display();
    cout<<"------------ COMPLEX -------------\n";

    cout<<"------------ HYBRID SIMPLE -------------\n";
    HybridCalc hybridSimple;
    hybridSimple.SimpleCalc(9, 9);
    cout<<"------------ HYBRID SIMPLE -------------\n";

     cout<<"------------ HYBRID COMPLEX -------------\n";
    HybridCalc hybridComplex;
    hybridComplex.ScienceCalc(9, 9);
    cout<<"------------ HYBRID COMPLEX -------------\n";

}
