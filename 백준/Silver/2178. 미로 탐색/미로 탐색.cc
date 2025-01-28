#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> maps;

int main()
{
  cin >> n >> m;
  maps.resize(n);
  string s;

  for (size_t r = 0; r < n; r++)
  {
    maps[r].resize(m);
    cin >> s;
    for (size_t i = 0; i < m; i++)
    {
      int item = stoi(s.substr(i, 1));
      maps[r][i] = item;
    }
  }

  queue<vector<int>> que;
  que.push(vector<int>{0, 0, 0});
  vector<vector<int>> visited;
  visited.resize(n);
  for (auto &&i : visited)
  {
    i.resize(m);
  }

  int dy[] = {-1, 0, 1, 0};
  int dx[] = {0, -1, 0, 1};

  int result = 0;

  while (!que.empty())
  {
    vector<int> x = que.front();
    que.pop();
    int r = x[0];
    int c = x[1];
    int cnt = x[2];

    if (r == n - 1 && c == m - 1)
    {
      result = cnt;
      break;
    }

    for (size_t i = 0; i < 4; i++)
    {
      int nr = r + dy[i];
      int nc = c + dx[i];

      if (0 <= nr && nr < n && 0 <= nc < m && !visited[nr][nc] && maps[nr][nc] == 1)
      {
        visited[nr][nc] = 1;
        que.push(vector<int>{nr, nc, cnt + 1});
      }
    }
  }

  cout << result + 1 << endl;
}
