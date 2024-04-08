import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        Arrays.sort(array);
        
        int[] count = new int[array[array.length - 1] + 1];
        for(int i = 0; i < array.length; i++) {
            count[array[i]]++;
        }
        
        int maxCount = 0;
    
        for(int i = 0; i < count.length; i++) {
            if (maxCount < count[i]) {
                maxCount = count[i];
                answer = i;
            } else if (maxCount == count[i]) {
                answer = -1;
            }
        }
            
        return answer;
    }
}