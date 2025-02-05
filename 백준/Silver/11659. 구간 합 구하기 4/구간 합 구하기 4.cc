#include <iostream>
#include <vector>

using namespace std;

int n,m,a,b;
vector<int> dp;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;
    dp.resize(n);
    cin >> dp[0];
    for(int i = 1; i < n; i++) {
        cin >> dp[i];
        dp[i] += dp[i - 1];
    }
    
    for(int i = 0; i < m; i++ ){
        cin >> a >> b;;
        int result = dp[b - 1] - (a - 2 >= 0 ? dp[a - 2] : 0);
        cout << result << "\n";
    }
}
