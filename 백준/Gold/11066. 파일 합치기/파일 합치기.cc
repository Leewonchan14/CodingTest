#include <iostream>
#include <vector>

using namespace std;

int tc, n;
vector<long> arr;
vector<vector<long>> dp;

int main()
{
  cin >> tc;

  for (int i = 0; i < tc; i++)
  {
    cin >> n;
    arr.assign(n, 0);
    dp.resize(n);
    for (int j = 0; j < n; j++)
    {
      cin >> arr[j];
      dp[j].assign(n, 0);
    }

    dp[0][0] = 0;
    dp[0][1] = arr[0] + arr[1];

    for (int r = 2; r < n; r++)
    {
      for (int l = r - 1; l >= 0; l--)
      {
        long minv = (long)10000 * 5000 + 1;
        long sumv = arr[r];
        for (int k = r - 1; k >= l; k--)
        {
          long a = dp[l][k];
          long b = dp[k + 1][r];
          sumv += arr[k];
          minv = min(minv, a + b);
        }
        dp[l][r] = minv + sumv;
      }
    }

    cout << dp[0][n - 1] << "\n";
  }

  return 0;
}
