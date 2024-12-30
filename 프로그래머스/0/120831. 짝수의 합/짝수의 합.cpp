#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int sumv = 0;
    for (int i = 1; i <= n; i++){
        if (i % 2 == 0) {
            sumv += i;
        }
    }
    return sumv;
}