#include <iostream>
#include <vector>

using namespace std;

int n,m;
vector<int> arr;

int main(){
    cin >> n >> m;
    
    arr.resize(n);
    
    for(int i = 0; i < n; i ++ ){
        cin >> arr[i];
    }
    
    long sum = arr[0];
    int l = 0;
    int r = 1;
    int cnt = 0;
    
    
    while(true){
        if(sum == m) {
            cnt += 1;
            sum -= arr[l];
            l += 1;
            continue;
        }
        
        if (sum < m) {
            if (r >= n) break;
            
            sum += arr[r];
            r += 1;
            continue;
        }
        if(sum > m) {
            sum -= arr[l];
            l += 1;
            continue;
        }
    }
    
    cout << cnt << "\n";
    
    return 0;
}