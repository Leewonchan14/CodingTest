#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{

    int MAX = 10000000;

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long n;
    cin >> n;

    long i = 2;
    while (n > 1)
    {
        if (n % i == 0)
        {
            cout << i << endl;
            n /= i;
            continue;
        }
        i++;
        if (i * i > n)
        {
            cout << n;
            break;
        }
    }
}
