#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

struct QueItem
{
  vector<string> li;
  int cnt;
};

unordered_map<string, int> visited;
vector<string> li;

string getKey(vector<string> &li);
string join(vector<string> &li, string del);
bool isClear(vector<string> &li);

int main()
{
  li.resize(3);

  for (size_t i = 0; i < 3; i++)
  {
    int a;
    string s;
    cin >> a;
    if (a == 0)
      continue;

    cin >> s;
    li[i] = s;
  }

  queue<QueItem> que;
  que.push(QueItem{li, 0});
  visited[getKey(li)] = 1;

  while (!que.empty())
  {
    li = que.front().li;
    int cnt = que.front().cnt;
    que.pop();

    if (isClear(li))
    {
      cout << cnt << endl;
      return 0;
    }

    for (size_t i = 0; i < 3; i++)
    {
      if (li[i].length() == 0)
        continue;

      for (size_t j = 0; j < 3; j++)
      {
        if (i == j)
          continue;

        int k = 3 - i - j;
        vector<string> other(li.begin(), li.end());
        other[j].push_back(other[i].back());
        other[i].pop_back();

        string key = getKey(other);

        if (visited[key])
          continue;

        visited[key] = 1;
        que.push(QueItem{other, cnt + 1});
      }
    }
  }
}

bool isClear(vector<string> &li)
{
  string c = "ABC";
  for (size_t i = 0; i < 3; i++)
  {
    for (auto &&item : li[i])
    {
      if (item != c.at(i))
      {
        return false;
      }
    }
  }

  return true;
}

string getKey(vector<string> &li)
{
  return join(li, " ");
}

string join(vector<string> &li, string del)
{
  string s = "";

  for (size_t i = 0; i < li.size(); i++)
  {
    s.append(li[i]);
    if (i != li.size() - 1)
    {
      s.append(del);
    }
  }

  return s;
}
