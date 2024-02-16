
#include <iostream>
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
    char carac = '[';
    char end = ']';
    int value, input;

    cin << input;
    while (input != end) {
        cin << input;
        nums.push_back(input);
    }

    cin << value;
    cout << removeElement(nums, value);
}
};