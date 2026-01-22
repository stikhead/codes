#include<iostream>
using namespace std;
// roll number is ambuigity here
class student{
    protected:
        int roll_number;
    public: 
        void set_roll_number(int n){
            roll_number = n;
        }
        void get_roll_number(){
            cout<<"Roll Number is: "<<roll_number<<endl;
        }
};
class test: virtual protected student{
    protected:
        float math;
        float physics;
    public:
        void set_marks(int n, int m){
            math = n;
            physics = m;
        }
        void get_marks(){
            cout<<"Marks: \n"
                <<"Physics: "<<physics<<"\n"
                <<"Maths: "<<math<<endl;
        }
};
class sport: virtual protected student{
    protected:
        float score;
    public: 
        void set_score(float k){
            score = k;
        }
        void get_score(){
            cout<<"Score is: "<<score<<endl;
        }
};
class result:protected test, protected sport{
    private:
        float total;
    public:
        void set_marks(int n, int m){
            test::set_marks(n, m);
        }
        void set_score(float n){
            sport::set_score(n);
        }
        void get_score(){
            sport::get_score();
        }
        void get_marks(){
            test::get_marks();
        }
        void display(int roll){
            total = math+physics+score;
            cout<<"Total: "<<total<<endl;
            set_roll_number(roll);
            cout<<"Roll Number: "<<roll<<endl;
        }
};
int main(){
    result r;
    r.set_marks(98, 96);
    r.set_score(77.9);
    r.get_marks();
    r.get_score();
    r.display(241466);

}