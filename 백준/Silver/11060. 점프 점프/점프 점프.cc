#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int n;
vector<int> maps;
vector<int> costs;

int main()
{
  cin >> n;
  maps.resize(n);
  costs.assign(n, 10001);
  for (int i = 0; i < n; i++)
  {
    cin >> maps[i];
  }

  queue<int> que;
  que.push(0);
  costs[0] = 0;

  while (!que.empty())
  {
    int x = que.front();
    que.pop();

    for (int i = 1; i <= maps[x]; i++)
    {
      int nx = x + i;
      if (nx < n && costs[x] + 1 < costs[nx])
      {
        costs[nx] = costs[x] + 1;
        que.push(nx);
      }
    }
  }

  cout << (costs.back() == 10001 ? -1 : costs.back()) << endl;
}