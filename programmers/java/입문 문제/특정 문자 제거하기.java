class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
            String str = String.valueOf(my_string.charAt(i));
            if (!str.equals(letter)) {
                answer += str;
            }
        }
        
        // answer = my_string.replace(letter, "");
        
        return answer;
    }
}