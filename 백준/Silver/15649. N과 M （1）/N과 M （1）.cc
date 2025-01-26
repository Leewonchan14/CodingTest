#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string.h>

using namespace std;

void recur(int n, int m, vector<int> &li, int size, int visited[]);

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> li;
    int *visited = new int[n + 1];

    memset(visited, 0, sizeof(int) * (n + 1));

    recur(n, m, li, 0, visited);
}

void recur(int n, int m, vector<int> &li, int size, int visited[])
{

    if (size == m)
    {
        for (auto &&i : li)
        {
            cout << i << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            li.push_back(i);
            recur(n, m, li, size + 1, visited);
            li.pop_back();
            visited[i] = 0;
        }
    }

    return;
}
