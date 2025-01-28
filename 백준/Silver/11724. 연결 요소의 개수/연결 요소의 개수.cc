#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> dic;
vector<int> visited;

void dfs(int start);

int main()
{
  cin >> n >> m;
  dic.resize(n + 1);
  for (size_t i = 0; i < m; i++)
  {
    int a, b;
    cin >> a >> b;
    dic[a].push_back(b);
    dic[b].push_back(a);
  }
  visited.assign(n + 1, 0);

  int cnt = 0;
  for (size_t i = 1; i <= n; i++)
  {
    if (!visited[i])
    {
      cnt += 1;
      visited[i] = 1;
      dfs(i);
    }
  }

  cout << cnt << endl;
}

void dfs(int start)
{
  for (auto &&nv : dic[start])
  {
    if (!visited[nv])
    {
      visited[nv] = 1;
      dfs(nv);
    }
  }
}
