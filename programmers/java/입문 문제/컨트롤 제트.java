class Solution {
    public int solution(String s) {
        int answer = 0;
        
        String[] arrays = s.split(" ");
        for(int i = 0; i < arrays.length; i++) {
            if(arrays[i].equals("Z")) {
                answer -= Integer.parseInt(arrays[i-1]);
            } else {
                answer += Integer.parseInt(arrays[i]);
            }
        }
        
        return answer;
    }
}