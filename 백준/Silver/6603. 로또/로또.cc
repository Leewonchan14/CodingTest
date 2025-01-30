#include <iostream>
#include <vector>

using namespace std;

int n, v;
vector<int> arr;
vector<int> li;

int combi();

int main()
{
  while (true)
  {
    arr.clear();
    li.clear();
    cin >> n;
    if (n == 0)
    {
      return 0;
    }
    for (int i = 0; i < n; i++)
    {
      cin >> v;
      arr.push_back(v);
    }
    combi();
    cout << "\n";
  }
}

int combi()
{
  if (li.size() == 6)
  {
    for (auto &&i : li)
    {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return 0;
  }

  for (int i = 0; i < arr.size(); i++)
  {
    if (li.empty() || i > li.back())
    {
      li.push_back(i);
      combi();
      li.pop_back();
    }
  }

  return 0;
}