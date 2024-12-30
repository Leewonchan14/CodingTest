#include <string>
#include <vector>

using namespace std;

bool isIn(string a, string b){
    if (a.size() < b.size()) return false;
    
    for(int i = 0; i < a.size() - b.size() + 1; i++){
        string a1 = string(a.begin() + i, a.begin() + i + b.size());
            
        if (a1 == b) return true;
    }
    return false;
}

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(auto s: strArr){
        if (!isIn(s, "ad")) {
            answer.push_back(s);
        }
    }
    return answer;
}