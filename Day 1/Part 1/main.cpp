#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

char const* digits = "0123456789";

int main()
{
    std::string line;
    std::ifstream myfile;
    myfile.open("input.txt");
    if (myfile.is_open())
    {
        while (getline (myfile, line))
        {
            int first = line.find_first_of(digits);
            int last = line.find_last_of(digits);

            std::cout << first + last;
        }
    }
}