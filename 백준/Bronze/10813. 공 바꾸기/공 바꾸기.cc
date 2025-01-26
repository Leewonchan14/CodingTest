#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> list;
    int n, m;
    cin >> n >> m;

    for (size_t i = 1; i <= n; i++)
    {
        list.push_back(i);
    }

    for (size_t i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;

        a -= 1;
        b -= 1;

        int temp = list[a];
        list[a] = list[b];
        list[b] = temp;
    }

    for (auto &&i : list)
    {
        cout << i << " ";
    }
}
