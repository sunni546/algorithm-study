import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        
        int[] emergencyTmp = new int[emergency.length];
        for (int i = 0; i < emergencyTmp.length; i++) {
            emergencyTmp[i] = emergency[i];
        }
        
        Arrays.sort(emergencyTmp);
        
        for (int i = 0; i < emergencyTmp.length; i++) {
            for (int j = 0; j < emergency.length; j++) {
                if (emergencyTmp[i] == emergency[j]) {
                    answer[j] = emergency.length - i;
                }
            }
        }
        
        return answer;
    }
}