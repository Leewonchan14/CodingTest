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

    bool *che = new bool[MAX + 1];

    for (size_t i = 2; i < MAX + 1; i++)
    {
        che[i] = true;
    }

    for (size_t i = 2; i < MAX + 1; i++)
    {
        if (che[i])
        {
            for (size_t j = i + i; j < MAX + 1; j += i)
            {
                che[j] = false;
            }
        }
    }

    long n;
    cin >> n;

    long i = 2;
    while (n > 1)
    {
        if (n % i == 0)
        {
            cout << i << endl;
            n /= i;
        }

        while (n > 1 && n % i != 0)
        {
            i += 1;
        }
    }
}
