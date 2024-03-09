/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(); // dummy node to hold the result
    ListNode* current = dummy; // pointer to traverse the result list
    int carry = 0; // carry value for addition
    
    while (l1 != nullptr || l2 != nullptr) {
        int x = (l1 != nullptr) ? l1->val : 0;
        int y = (l2 != nullptr) ? l2->val : 0;
        
        int sum = x + y + carry;
        carry = sum / 10; // Update carry
        current->next = new ListNode(sum % 10); // Add new node to the result
        current = current->next; // Move to the next node
        
        if (l1 != nullptr) l1 = l1->next;
        if (l2 != nullptr) l2 = l2->next;
    }
    
    // Handle remaining carry
    if (carry > 0) {
        current->next = new ListNode(carry);
    }
    
    return dummy->next; // return the next of dummy, which holds the result
}

};