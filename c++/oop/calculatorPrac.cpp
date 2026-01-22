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

class HybridCalc: public SimpleCalculator, public ScientificCalculator {

};
int main(){

}
