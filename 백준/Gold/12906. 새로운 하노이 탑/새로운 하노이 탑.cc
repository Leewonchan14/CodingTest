#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

struct QueItem
{
  vector<vector<string>> li;
  int cnt;
};

unordered_map<string, int> visited;
vector<vector<string>> li;

string getKey(vector<vector<string>> &li);
string join(vector<string> &li);
bool isClear(vector<vector<string>> &li);

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
    for (size_t j = 0; j < a; j++)
    {
      li[i].push_back(s.substr(j, 1));
    }
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
      if (li[i].size() == 0)
        continue;

      for (size_t j = 0; j < 3; j++)
      {
        if (i == j)
          continue;

        int k = 3 - i - j;
        vector<vector<string>> other(li.begin(), li.end());
        other[j].push_back(other[i].back());
        other[i].pop_back();

        vector<vector<string>> nli;
        nli.resize(3);
        nli[i] = other[i];
        nli[j] = other[j];
        nli[k] = other[k];

        string key = getKey(nli);

        if (visited[key])
          continue;

        visited[key] = 1;
        que.push(QueItem{nli, cnt + 1});
      }
    }
  }
}

bool isClear(vector<vector<string>> &li)
{
  string c = "ABC";
  for (size_t i = 0; i < 3; i++)
  {
    for (auto &&item : li[i])
    {
      if (item != c.substr(i, 1))
      {
        return false;
      }
    }
  }

  return true;
}

string getKey(vector<vector<string>> &li)
{
  string s = "";
  s.append(join(li[0]));
  s.append(" ");
  s.append(join(li[1]));
  s.append(" ");
  s.append(join(li[2]));

  return s;
}

string join(vector<string> &li)
{
  string s = "";

  for (size_t i = 0; i < li.size(); i++)
  {
    s.append(li[i]);
  }

  return s;
}
