#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double sumv = 0;
    for(int i = 0; i < numbers.size(); i ++){
        sumv += numbers[i];
    }
    return sumv / numbers.size();
}