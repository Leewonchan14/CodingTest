#include <iostream>
#include <vector>

using namespace std;

int n, s, v, cnt = 0;
vector<int> arr;
vector<int> li;

int recur(long sum);

int main()
{
  cin >> n >> s;

  for (int i = 0; i < n; i++)
  {
    cin >> v;
    arr.push_back(v);
  }

  recur(0);
  cout << cnt << endl;

  return 0;
}

int recur(long sum)
{
  if (!li.empty() && sum == s)
  {
    cnt += 1;
  }

  if (li.size() == arr.size())
  {
    return 0;
  }

  for (int i = 0; i < arr.size(); i++)
  {
    if (li.empty() || i > li.back())
    {
      li.push_back(i);
      recur(sum + arr[i]);
      li.pop_back();
    }
  }

  return 0;
}