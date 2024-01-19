#include <string>
using namespace std;
class Solution {
public:
    string answer ="";
    int reminder=0 ;
    int quantifier =0;
    bool isPalindrome(int x) {

        if(x<0){
            return false;
        }
        else if(x==0){
            return true;
        }
        else{
           quantifier =x;
            while (quantifier!=0){
                answer += to_string(quantifier %10);
                quantifier= quantifier/10;
            }
            
            if (answer == to_string(x)){
                return true;
            }
            else{
                return false;
            } 
        }
        

    }

};