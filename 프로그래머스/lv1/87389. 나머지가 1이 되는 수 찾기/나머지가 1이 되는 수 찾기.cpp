#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int m = n - 1;
    for(int i = 2; i <= m; i++)
    {
        if (m % i == 0)
        {
            answer = i;
            return answer;
        }
    }
}