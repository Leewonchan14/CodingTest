#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string myString, string pat) {
    string convert = "";
    for(int i = 0; i < myString.size(); i ++ ){
        convert += myString[i] == 'A' ? "B" : "A";
    }
    
    for(int i = 0; i < myString.size() - pat.size() + 1; i ++){
        if (string(convert.begin() + i,convert.begin() + i + pat.size()) == pat) {
            return 1;
        }
    }
    
    return 0;
    
}