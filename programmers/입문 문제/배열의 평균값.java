class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (double n : numbers) {
            answer += n;
        }
        return answer / numbers.length;
    }
}