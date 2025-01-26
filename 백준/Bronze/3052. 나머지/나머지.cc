#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int cntList[42] = {};

    for (size_t i = 0; i < 10; i++)
    {
        int j;
        cin >> j;
        cntList[j % 42]++;
    }

    int cnt = 0;
    for (int i : cntList)
    {
        if (i > 0)
            cnt += 1;
    }

    cout << cnt;
}
