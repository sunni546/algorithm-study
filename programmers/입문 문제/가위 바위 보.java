class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        for (int i = 0; i < rsp.length(); i++) {
            String s = String.valueOf(rsp.charAt(i));
            if (s.equals("0")) {
                answer += "5";
            } else if (s.equals("2")) {
                answer += "0";
            } else if (s.equals("5")) {
                answer += "2";
            }
        }
        
        return answer;
    }
}