import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        
        Set<Integer> numbers = new HashSet<>();
        for(int i = 2; i <= n; i++) {
            while(n % i == 0) {
                n /= i;
                numbers.add(i);
            }
        }
        
        answer = numbers.stream()
                .mapToInt(i -> i)
                .toArray();
        Arrays.sort(answer);
        
        return answer;
    }
}