#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int tc, n, x1, yy1, x2, y2;
vector<vector<int>> points;

int dist(int x1, int y1, int x2, int y2);

int main()
{
    cin >> tc;
    for (int i = 0; i < tc; i++)
    {
        cin >> x1 >> yy1 >> x2 >> y2 >> n;
        points.resize(n);
        for (int j = 0; j < n; j++)
        {
            vector<int> li;
            li.resize(3);
            cin >> li[0] >> li[1] >> li[2];
            points[j] = li;
        }

        int cnt = 0;
        for (auto &&li : points)
        {
            int a = dist(li[0], li[1], x1, yy1) <= pow(li[2], 2);
            int b = dist(li[0], li[1], x2, y2) <= pow(li[2], 2);

            if ((a || b) && (a != b))
            {
                cnt += 1;
            }
        }

        cout << cnt << "\n";
    }

    return 0;
}

int dist(int x1, int y1, int x2, int y2)
{
    return pow((x1 - x2), 2) + pow((y1 - y2), 2);
}