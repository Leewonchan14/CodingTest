#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    double mid = pow(n, (double)1 / 2);
    if ((int)mid * (int)mid == n){
        return 1;
    } else{
        return 2;
    }
    
}