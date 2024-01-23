class Solution {
    public int solution(int price) {
        int answer = price;
        
        if (price >= 500000) {
            answer = answer * 80 / 100;
        } else if (price >= 300000) {
            answer = answer * 90 / 100;
        } else if (price >= 100000) {
            answer = answer * 95 / 100;
        }
            
        return answer;
    }
}