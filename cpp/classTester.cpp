//
//  classTester.cpp
//  A small program to test and refresh class operations in C++
//
//  Created by Swaminathan Sivaraman on 1/2/17.
//  Copyright © 2017 Swaminathan Sivaraman. All rights reserved.
//

#include <iostream>

class Hello {
private:
    int i;
public:
    int j;
    Hello(int initial);
    void setI(int val);
    int getI();
};

Hello::Hello(int initial) {
    i = initial;
    j = initial;
}

void Hello::setI(int val) {
    i = val;
}

int Hello::getI() {
    return i;
}


int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    Hello *hello = new Hello(7);
    std::cout << hello->j << "\n";
    hello->setI(4);
    std::cout << hello->getI() << "\n";
    delete hello;
    return 0;
}
