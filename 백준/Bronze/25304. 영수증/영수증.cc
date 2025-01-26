#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    long x;
    int n;
    cin >> x >> n;
    long sum = 0;
    for (size_t i = 1; i <= n; i++)
    {
        long a, b;
        cin >> a >> b;
        sum += a * b;
    }
    if (sum == x)
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
}
