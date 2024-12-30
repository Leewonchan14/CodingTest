#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    int mid = (int)pow(n, (double)1 / 2);
    for(int i = 1; i <= mid; i++){
        if (n % i == 0){
            answer.push_back(i);
            answer.push_back(n / i);
        }
    }
    
    if (mid * mid == n){
        answer.pop_back();
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}