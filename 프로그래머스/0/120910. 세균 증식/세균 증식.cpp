#include <string>
#include <vector>

using namespace std;

int solution(int n, int t) {
    int mul = n;
    while (t-- > 0){
        mul *= 2;
    }
    return mul;
}