class Solution {
    public int solution(int slice, int n) {
        int answer = 1;
        while(n - slice > 0) {
            n -= slice;
            answer++;
        }
        return answer;
    }
}