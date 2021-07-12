#include <iostream>
using namespace std;

void pass_value(int var){
    var = 5;
}

void pass_reference(int* var){
    *var = 4;
}

int main(){
    int a = 6;
    pass_value(a);
    cout << a << endl;
    pass_reference(&a);
    cout << a << endl;
    return 0;
}