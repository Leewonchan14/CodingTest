#include <iostream>
#include <vector>

using namespace std;

int n, m, s, e;
vector<int> maps;
vector<vector<int>> costs;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n;
    maps.resize(n);
    costs.resize(n);
    for(int i = 0; i < n; i++ ){
        cin >> maps[i];
        costs[i].resize(n + 1);
    }
    
    for(int e = 1; e <= n; e ++ ){
        for(int s = e - 1; s >= 0; s-- ){
            costs[s][e] = maps[s] == maps[e - 1] && (s + 1 >= e - 1 || costs[s + 1][e - 1]);
        }
    }
    
    cin >> m;
    for(int i = 0; i < m; i++){
        cin >> s >> e;
        cout << costs[s - 1][e] << "\n";
    }
}