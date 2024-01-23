class Solution {
    public String solution(int age) {
        String answer = "";
        
        String ageStr = String.valueOf(age);
        for (int i = 0; i < ageStr.length(); i++) {
            answer += (char) ((int) ageStr.charAt(i) + 'a' - '0');
        }
        
        return answer;
    }
}