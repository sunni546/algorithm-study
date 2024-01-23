class Solution {
    private static int COFFEE = 5500;
        
    public int[] solution(int money) {
        int[] answer = new int[2];
        
        answer[0] = money / COFFEE;
        answer[1] = money % COFFEE;
        
        return answer;
    }
}