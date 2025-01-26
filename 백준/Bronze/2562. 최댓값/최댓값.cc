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

    for (size_t i = 0; i < 9; i++)
    {
        int j;
        cin >> j;

        list.push_back(j);
    }

    int maxv = *max_element(list.begin(), list.end());
    int maxvIdx = max_element(list.begin(), list.end()) - list.begin();

    cout << maxv << endl;
    cout << maxvIdx + 1;
}
