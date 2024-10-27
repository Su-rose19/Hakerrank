#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    cin>>a;
    cin>>b;
    int l1 = a.size();
    int l2 = b.size();
    string res = a+b;
    cout<<l1<<' '<<l2<<endl;
    cout<<res<<endl;
    // cout<<a<<' '<<b<<endl;
    swap(a[0],b[0]);
    cout<<a<<' '<<b<<endl;
    return 0;
}
