class Solution {
    static int PIZZA = 6;
    
    public int solution(int n) {
        int answer = 1;
        answer = getPizza(answer, n);
        return answer;
    }
    
    private int getPizza(int num, int y) {
        if (PIZZA * num % y == 0) {
            return num;
        }
        return getPizza(num + 1, y);
    }
}