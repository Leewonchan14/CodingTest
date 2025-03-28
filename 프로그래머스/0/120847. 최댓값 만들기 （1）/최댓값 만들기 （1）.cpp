#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int maxv = -1;
    for(int i = 0; i < numbers.size() - 1; i++ ){
        for (int j = i + 1; j < numbers.size(); j++ ){
            if (numbers[i] * numbers[j] > maxv) {
                maxv = numbers[i] * numbers[j];
            }
        }
    }
    
    return maxv;
}