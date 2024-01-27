class Solution
{
    public int solution(long n, long a, long b)
    {
        int count = 0;
        while(true){            
            
            if(a == b){
                return count;
            }
            
            count++;
                        
            a = (a % 2 == 1) ? (a+1)/2 : a/2;
            b = (b % 2 == 1) ? (b+1)/2 : b/2;            
        }
    }
}