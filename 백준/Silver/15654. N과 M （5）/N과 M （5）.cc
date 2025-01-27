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
int visited[10];
int arr[10];
int recur();

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (size_t i = 0; i < n; i++)
    {
        int input;
        cin >> input;

        arr[i] = input;
    }

    sort(arr, &arr[n]);

    recur();

    cout << result;
}

int recur()
{
    if (li.size() == m)
    {
        for (auto &&i : li)
        {
            cout << arr[i] << " ";
        }

        cout << "\n";

        return 0;
    }

    for (size_t i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            li.push_back(i);
            recur();
            li.pop_back();
            visited[i] = 0;
        }
    }

    return 0;
}
