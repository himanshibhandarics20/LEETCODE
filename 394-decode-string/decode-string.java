class Solution {
    public String decodeString(String s) {
        Stack<Integer> nums = new Stack<>();
        Stack<String> strs = new Stack<>();

        String str = "";
        int num = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } 
            else if (c == '[') {
                nums.push(num);
                strs.push(str);
                num = 0;
                str = "";
            } 
            else if (c == ']') {
                int n = nums.pop();
                String old = strs.pop();

                str = old + str.repeat(n);
            } 
            else {
                str += c;
            }}
            return str;
            }}