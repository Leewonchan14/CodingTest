#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int n;
    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << a + b << endl;
    }
}
