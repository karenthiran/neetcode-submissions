class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map1=new HashMap<>();
        HashMap<Character,Integer> map2=new HashMap<>();

        if(s.length()!=t.length()) return false;
        
        for(int i=0;i<s.length();i++){
            if(map1.containsKey(s.charAt(i))){
                int val=map1.get(s.charAt(i));
                map1.put(s.charAt(i),++val);
            }
            else{
                map1.put(s.charAt(i),1);
            }
            if(map2.containsKey(t.charAt(i))){
                int val=map2.get(t.charAt(i));
                map2.put(t.charAt(i),++val);
            }
            else{
                map2.put(t.charAt(i),1);
            }
        }

        if(map1.size()!=map2.size()) return false;

        for(int i=0;i<s.length();i++){
            if(map2.containsKey(s.charAt(i)) && map1.containsKey(s.charAt(i))){
                if(map2.get(s.charAt(i))!=map1.get(s.charAt(i))){
                    return false;
                }
            }
            else{
                return false;
            } 
        }

        return true;

    }
}
