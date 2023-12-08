// given an integer array sorted
// remove duplicates in place such that each element appear only once
// the relative order of the elements should be kept the same
// return the new length (number of unique elements)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> removeDuplicates(vector<int> arr) {
        vector <int> resp = {0};
        if (arr.size() == 0) return resp;
        
        int cnt = 0;
        vector <int> aux;
        for(int i = 1; i < arr.size(); i++) {
            if (arr[i] == arr[i-1]) cnt++;
            else aux.push_back(arr[i-1]);
        } 
        // retorna o array final sem repetições
        return aux;
        //return aux.size();
    }

    int main() {
        vector <string> arr;
        vector <int> arr2;
        string enter;
        // recebo o vector
        while (cin >> enter and (enter != "[") or (enter != "]") or (enter != ",")) {
            arr.push_back(enter);
        }    

        // transformar de string para inteiro
        for (int i = 0; i < arr.size(); i++) {
            int x = stoi(arr[i]);
            arr2[i] = x;
        }
        
        vector <int> final = removeDuplicates(arr2)
        
        // printar o vector final
        for (int i = 0; i < final.size(); i++) {
            cout << final[i] << " ";
        }
        return 0;
    }
};