#include <iostream>
using namespace std;

int main()
{
    int sum=0;
    cout<<"First 10 natural numbers are: ";
    for(int i=1; i<=10; i++)
    {
        cout<<i<< " ";
        sum+=i;
    }
    cout<<"\nSum of first 10 natural numbers: "<<sum;
    return 0;
}