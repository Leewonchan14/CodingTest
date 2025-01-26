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

    int list[9] = {};
    int sum = 0;
    for (size_t i = 0; i < 9; i++)
    {
        int j = 0;
        cin >> j;
        list[i] = j;
        sum += j;
    }

    bool flag = false;
    int a, b;
    for (size_t i = 0; i < 9; i++)
    {
        for (size_t j = i + 1; j < 9; j++)
        {
            if (sum - list[i] - list[j] == 100)
            {
                a = i;
                b = j;
            }
        }
        if (flag)
            break;
    }

    vector<int> list2 = {};
    for (size_t i = 0; i < 9; i++)
    {
        if (i != a && i != b)
        {
            list2.push_back(list[i]);
        }
    }

    sort(list2.begin(), list2.end());

    for (auto &&i : list2)
    {
        cout << i << endl;
    }
}
