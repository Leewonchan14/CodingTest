#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    long minv = 1000000, maxv = -1000000, i;

    for (long j = 0; j < n; j++)
    {
        cin >> i;
        maxv = max(maxv, i);
        minv = min(minv, i);
    }

    cout << minv << " " << maxv;
}
