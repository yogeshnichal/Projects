#include <iostream>
using namespace std;

int main()
{
    int n, sum=0;
    cout<<"Enter valid n number: ";
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        cout<<i<<" ";
        sum+=i;
    }
    cout<<"\nSum of the n natural number is: "<<sum;
    
    return 0;
}