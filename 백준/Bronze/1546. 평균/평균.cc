#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int cnt = 0;
    long sum = 0;
    long maxv = 0;

    for (size_t i = 0; i < n; i++)
    {
        int j;
        cin >> j;
        sum += j;
        cnt += 1;
        maxv = max(maxv, (long)j);
    }

    cout << ((double)sum / maxv * 100) / cnt;
}
