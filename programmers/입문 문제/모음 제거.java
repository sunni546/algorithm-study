class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
            String s = String.valueOf(my_string.charAt(i));
            if (s.equals("a")) {
                continue;
            } if (s.equals("e")) {
                continue;
            } if (s.equals("i")) {
                continue;
            } if (s.equals("o")) {
                continue;
            } if (s.equals("u")) {
                continue;
            }
            answer += s;
        }
        
        //answer = my_string.replaceAll("[aeiou]", "");
        
        return answer;
    }
}