#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> list = {};

    for (size_t i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        list.push_back(a);
    }
    int cnt = 0, v = 0;
    cin >> v;
    for (auto i : list)
    {
        if (i == v)
            cnt += 1;
    }

    cout << cnt;
}
