#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int length= nums.size();
        for(int i=0;i< length;i++){
            for(int j=i+1;j<length;j++){
                if((nums[i]+nums[j])== target){
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
        
    }
};