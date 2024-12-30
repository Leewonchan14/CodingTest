#include <string>
#include <vector>

using namespace std;

string solution(vector<string> arr) {
    string answer = "";
    for(int i = 0; i < arr.size(); i ++ ){
        for (int j = 0; j < arr[i].length(); j ++ ){
            answer.push_back(arr[i][j]);    
        }
    }
    return answer;
}