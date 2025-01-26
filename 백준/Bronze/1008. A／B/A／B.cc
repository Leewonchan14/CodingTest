#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int a,b;
    cin >> a >> b;
    cout << fixed << setprecision(10);
    cout << (double)a / (double)b;
}
