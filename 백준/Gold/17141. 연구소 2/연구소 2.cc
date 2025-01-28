#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

int n, m;
vector<vector<int>> maps;
vector<vector<int>> visited;
vector<vector<int>> canVirus;
vector<vector<vector<int>>> canVirusComb;

void combi();
int bfs(vector<vector<int>> &can);

int main()
{

  cin >> n >> m;
  maps.resize(n);
  visited.resize(n);
  for (int i = 0; i < n; i++)
  {
    maps[i].resize(n);
    visited[i].assign(n, -1);
    for (int j = 0; j < n; j++)
    {
      cin >> maps[i][j];
      if (maps[i][j] == 2)
        canVirus.push_back(vector<int>{i, j});
    }
  }

  combi();

  int minv = 2500 + 1;

  for (auto &&can : canVirusComb)
  {
    int result = bfs(can);
    if (result == -1)
    {
      continue;
    }
    minv = min(minv, result);
  }

  if (minv == 2500 + 1)
  {
    cout << -1 << endl;
    return 0;
  }

  cout << minv << endl;
  return 0;
}

vector<int> li;
void combi()
{
  if (li.size() == m)
  {
    vector<vector<int>> nli;
    for (auto &&i : li)
    {
      nli.push_back(canVirus[i]);
    }

    canVirusComb.push_back(nli);
    return;
  }
  for (int i = 0; i < canVirus.size(); i++)
  {
    if (li.empty() || i > li.back())
    {
      li.push_back(i);
      combi();
      li.pop_back();
    }
  }
}

int dy[] = {0, -1, 0, 1};
int dx[] = {-1, 0, 1, 0};

bool inner(int y, int x)
{
  return 0 <= y & y < n && 0 <= x && x < n;
}

int bfs(vector<vector<int>> &can)
{
  for (size_t i = 0; i < n; i++)
  {
    visited[i].assign(n, -1);
  }

  queue<vector<int>> que;
  for (auto &&i : can)
  {
    que.push(vector<int>{i[0], i[1], 0});
    visited[i[0]][i[1]] = 0;
  }

  int maxv = 0;

  while (!que.empty())
  {
    int y = que.front()[0];
    int x = que.front()[1];
    int cnt = que.front()[2];
    que.pop();

    maxv = max(cnt, maxv);

    for (size_t i = 0; i < 4; i++)
    {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (inner(ny, nx) && maps[ny][nx] != 1 && visited[ny][nx] == -1)
      {
        visited[ny][nx] = cnt + 1;
        que.push(vector<int>{ny, nx, cnt + 1});
      }
    }
  }

  for (size_t i = 0; i < n; i++)
  {
    for (size_t j = 0; j < n; j++)
    {
      if (maps[i][j] != 1 && visited[i][j] == -1)
        return -1;
    }
  }

  return maxv;
}
