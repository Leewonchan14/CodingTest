#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    return string(my_string.begin(), my_string.begin() + n);
}