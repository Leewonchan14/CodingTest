#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int n;
    cin >> n;
    for (size_t i = 1; i <= 9; i++)
    {
        cout << n << " * " << i << " = " << n * i << endl;
    }
}
