#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

int n, m;
vector<vector<int>> maps;

int d[4][2] = {{-1, -1}, {-1, 0}, {0, -1}};

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> n >> m;
  maps.resize(n);

  for (size_t i = 0; i < n; i++)
  {
    maps[i].resize(m);
    for (size_t j = 0; j < m; j++)
    {
      cin >> maps[i][j];
    }
  }

  for (size_t i = 0; i < n; i++)
  {
    for (size_t j = 0; j < m; j++)
    {
      int maxv = 0;
      for (size_t k = 0; k < 3; k++)
      {
        int ni = i + d[k][0];
        int nj = j + d[k][1];
        if (ni >= 0 && nj >= 0)
        {
          maxv = max(maxv, maps[ni][nj]);
        }
      }

      maps[i][j] += maxv;
    }
  }

  cout << maps.back().back() << endl;
}
