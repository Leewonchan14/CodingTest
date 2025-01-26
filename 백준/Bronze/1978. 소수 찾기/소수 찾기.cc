#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    bool che[1000 + 1] = {};

    for (size_t i = 2; i < 1000 + 1; i++)
    {
        che[i] = true;
    }

    for (size_t i = 2; i < 1000 + 1; i++)
    {
        if (che[i])
        {
            for (size_t j = i + i; j < 1000 + 1; j += i)
            {
                che[j] = false;
            }
        }
    }

    int cnt = 0;
    for (size_t i = 0; i < n; i++)
    {
        int j;
        cin >> j;

        if (che[j])
            cnt++;
    }

    cout << cnt;
}
