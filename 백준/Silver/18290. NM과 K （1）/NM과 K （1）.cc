#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string.h>

using namespace std;

int n, m, k;
vector<vector<int>> maps;

vector<long> sums;

vector<int> li;
int combi(long sumv);

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;

    for (size_t i = 0; i < n; i++)
    {
        vector<int> row;
        for (size_t i = 0; i < m; i++)
        {
            int input;
            cin >> input;
            row.push_back(input);
        }
        maps.push_back(row);
    }

    combi(0);

    long maxv = -10000000;
    for (size_t i = 0; i < sums.size(); i++)
    {
        maxv = max(maxv, sums[i]);
    }

    cout << maxv;
}

int dy[4] = {0, -1, 0, 1};
int dx[4] = {-1, 0, 1, 0};

int isInner(int r, int c)
{
    return 0 <= r && r < n && 0 <= c && c < m;
}

int isAdj(int a, int b)
{
    int r1 = a / m;
    int c1 = a % m;

    int r2 = b / m;
    int c2 = b % m;

    for (size_t i = 0; i < 4; i++)
    {
        int nr = r1 + dy[i];
        int nc = c1 + dx[i];
        if (isInner(nr, nc) && nr == r2 && nc == c2)
        {
            return true;
        }
    }
    return false;
}

int isAnyAdj(int v)
{
    for (auto &&i : li)
    {
        if (isAdj(v, i))
            return true;
    }
    return false;
}

int combi(long sumv)
{
    if (li.size() == k)
    {
        sums.push_back(sumv);
        return 0;
    }

    for (size_t i = 0; i < n * m; i++)
    {
        if (li.empty() || (i > li.back() && !isAnyAdj(i)))
        {
            li.push_back(i);
            combi(sumv + maps[i / m][i % m]);
            li.pop_back();
        }
    }

    return 0;
}
