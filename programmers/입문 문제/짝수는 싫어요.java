import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int[] answer = n % 2 == 0 ? new int[n / 2] : new int[n / 2 + 1];
        
        for (int i = 1; i <= n; i += 2) {
            answer[i / 2] = i;
        }
        
        Arrays.sort(answer);
        return answer;
    }
}