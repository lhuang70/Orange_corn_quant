//
//  main.cpp
//  123
//
//  Created by lijun on 9/20/17.
//  Copyright © 2017 Lijun. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class solution{
public:
    int maxnumber(vector<int> & nums)
    {
        int cur_max = 0, res = INT_MIN;
        for (auto x: nums)
        {
            cur_max = cur_max > 0? (cur_max + x) : x;
            
            if (cur_max > res)
                res = cur_max;
            
        }
        return res;
    }
};


int main(int argc, const char * argv[])
{
    /*
    solution x;
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    cout<< x.maxnumber(nums)<<endl;
    */

    
    string s1 = "A string example";
    string s2 = "A different string";
    
    bool b2 = s2> s1? true:false;
    cout<<b2;
    

    
    
    
    
    
    
}
