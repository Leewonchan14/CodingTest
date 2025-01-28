#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, v;
vector<int> *maps;

vector<int> li;
int *visited;

int dfs(int v);
int bfs();

int main()
{
  cin >> n >> m >> v;
  maps = new vector<int>[n + 1];
  visited = new int[n + 1];

  for (size_t i = 0; i < m; i++)
  {
    int a, b;
    cin >> a >> b;
    maps[a].push_back(b);
    maps[b].push_back(a);
  }

  for (size_t i = 0; i <= n; i++)
  {
    sort(maps[i].begin(), maps[i].end());
  }

  li.push_back(v);
  dfs(v);

  for (auto &&i : li)
  {
    cout << i << " ";
  }
  cout << "\n";

  li.clear();
  for (size_t i = 0; i <= n; i++)
  {
    visited[i] = 0;
  }

  bfs();

  for (auto &&i : li)
  {
    cout << i << " ";
  }
  cout << "\n";

  delete[] maps;
  delete[] visited;
}

int dfs(int v)
{
  visited[v] = 1;

  for (auto &&nv : maps[v])
  {
    if (!visited[nv])
    {
      visited[nv] = 1;
      li.push_back(nv);
      dfs(nv);
    }
  }

  return 0;
}

int bfs()
{
  queue<int> que;
  visited[v] = 1;
  que.push(v);

  while (!que.empty())
  {
    v = que.front();
    li.push_back(v);
    que.pop();

    for (auto &&nv : maps[v])
    {
      if (!visited[nv])
      {
        visited[nv] = 1;
        que.push(nv);
      }
    }
  }

  return 0;
}
