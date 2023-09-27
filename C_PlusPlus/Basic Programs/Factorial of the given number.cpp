#include <iostream>
using namespace std;

int main()
{
    int num1, factorial=1;
    cout<<"Input a number to find the factorial: ";
    cin>>num1;
    for(int a=1;a<=num1;a++)
    {
        factorial*=a;
    }
    cout<<"The factorial of the given number is: "<<factorial<<endl;
    return 0;
}