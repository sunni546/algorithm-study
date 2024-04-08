class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        answer[0] = numer1 * denom2 + numer2 * denom1;
        answer[1] = denom1 * denom2;
        
        int gcd = getGCD(answer[0], answer[1]);
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] /= gcd;
        }
            
        return answer;
    }
    
    private int getGCD(int num1, int num2) {
        if (num2 > num1) {
            int tmp = num1;
            num1 = num2;
            num2 = tmp;
        }
        
        if (num1 % num2 == 0) {
            return num2;
        }
        
        return getGCD(num2, num1 % num2);
    }
}