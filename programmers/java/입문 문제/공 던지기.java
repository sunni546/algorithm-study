class Solution {
    public int solution(int[] numbers, int k) {
        int answer = -1;
        
        int people = numbers.length;
        for (int i = 0; i < k; i++) {
            answer += 2;
            if (answer > people) {
                answer -= people;
            }
        }
        
        return answer;
    }
}