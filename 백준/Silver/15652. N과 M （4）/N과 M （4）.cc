#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string.h>

using namespace std;

vector<int> li;
int n, m;
string result;
// int visited[10];
int recur();

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    recur();

    cout << result;
}

int recur()
{
    if (li.size() == m)
    {
        for (auto &&i : li)
        {
            cout << i << " ";
        }

        cout << "\n";

        return 0;
    }
    for (size_t i = 1; i <= n; i++)
    {
        if (li.empty() || i >= li.back())
        {
            li.push_back(i);
            recur();
            li.pop_back();
        }
    }

    return 0;
}
