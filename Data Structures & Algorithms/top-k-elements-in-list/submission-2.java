class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                int t=map.get(nums[i]);
                map.put(nums[i],++t);
            }else{
                map.put(nums[i],1);
            }
        }
        List<Integer> lst=new ArrayList<>();

        for(Map.Entry<Integer,Integer> i:map.entrySet()){
            if(i.getValue()>=k) lst.add(i.getKey());
        }
        int j=0;
        while(lst.size()<k){
            if(!lst.contains(nums[j])) lst.add(nums[j]);

            j++;
        }
        int[] arr=new int[k];
        for(int i=0;i<k;i++){
            arr[i]=lst.get(i);
        }

        return arr;
    }
}
