#include <iostream>
#include <vector>
using namespace std;

int removeElement(vector<int>nums, int value) {

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == value) {
            nums.erase(nums.begin() + i);
            i--; // Decrement i to account for the erased element
        }
    }
    return nums.size();
}

int main() {
    vector<int> nums;
    int value, input;

    string in;
    while (cin >> in and in != "]")
    {
        if (in != "[" or in != ",")
        {
            int intN = stoi(in);
            nums.push_back(intN);  // 3 2 2 1
        }
    }
    cin >> value;
    cout << removeElement(nums, value);
    

    // cin << input;
    // while (input != end) {
    //     cin << input;
    //     nums.push_back(input);
    // }

    // cin << value;
    // cout << removeElement(nums, value);
    return 0;
    
}
