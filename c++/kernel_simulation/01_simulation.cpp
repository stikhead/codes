#include<bits/stdc++.h>
using namespace std;

// states of our cpu 
enum CPUMode {
    USER_MODE,
    KERNEL_MODE
};

// by default computer is in user mmode
CPUMode current_cpu_mode = USER_MODE;

class Kernel {
    int next_memory_address;
    unordered_map<string, string> fake_hard_drive;
    unordered_map<int, string> physical_ram;
    public:
        Kernel(){
            next_memory_address = 0;
        }
        string make_system_call(int req_id, string details, string data = ""){
            // switch from user mode to kernel mode
            current_cpu_mode = KERNEL_MODE;
            cout<<"[CPU SWITCH] -> Entered kernel mode..."<<endl;
            // now interacting with hardware for the task..

            string response = "";
            cout<<"[kernel] -> reviewing request id: "<<req_id<< " (" <<details<<" )"<<endl;
            if(req_id==1){
                cout<<"[kernel] allocating RAM from physical memory chips.."<<endl;
                response = to_string(next_memory_address);
                next_memory_address+=8;
                cout<<"[kernel] memory allocated at: "<<response<<endl;
            }
            
            else if(req_id==2){
                int address = stoi(details);
                cout<<"[kernel] writing data to physical address "<<address<<endl;
                physical_ram[address] = data;
                response = "SUCCESS";
            }

            else if(req_id==3){
                int address = stoi(details);
                cout<<"[kernel] reading from physical RAM at "<< address<<endl;
                response = physical_ram[address];
            } 

            else if(req_id==4){
                cout<<"[kernel] spinning up hard disk"<<endl;
                if(fake_hard_drive.find(details) != fake_hard_drive.end()){
                    int address = next_memory_address;
                    physical_ram[address] = fake_hard_drive[details];
                    next_memory_address+=100;
                    response = to_string(address);
                    cout<<"[kernel] file loaded into RAM"<<endl;

                } else {
                    response = "-1";
                    cout<<"[kernel] file doesnt exist";
                }



            }

            // switch back to usermode
            cout<<"[CPU switch] -> switched to user mode"<<endl;
            current_cpu_mode = USER_MODE;

            return response;
        }
};

class Program {
    private:
        Kernel* os_kernel;
    public:
        Program(Kernel * curr_os){
            os_kernel = curr_os;
        }

        void execute(){
            cout<<"[user program]: 2+2=4"<<endl;
            cout<<"[user program]: memory required to store 4"<<endl;
            string ptr_str = os_kernel->make_system_call(1, "8 bytes of memory");
            cout<<"[user program]: os gave memory at: "<<ptr_str<<endl;

            cout<<"[user program]: writing 4 to allocated memory.."<<endl;
            os_kernel->make_system_call(2, ptr_str, "4");


        }

};


int main(){
    cout<<"BOOTING UP"<<endl;
    Kernel * temp_kernel;

    Program p(temp_kernel);

    p.execute();

}