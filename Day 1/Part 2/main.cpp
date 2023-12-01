#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>


std::string digits = "0123456789";

std::vector<std::string> numbers = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

int main()
{
    int total = 0;
    std::string result = "00";
    std::string line;
    std::ifstream myfile;
    myfile.open("input.txt");
    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            for (int i = 0; i < numbers.size(); i++)
            {
                while (true)
                {
                    std::size_t found = line.find(numbers[i]);
                    if (found != std::string::npos)
                    {
                        line[found + 1] = digits[i];
                    }
                    else
                    {
                        break;
                    }
                }
            }

            std::size_t first = line.find_first_of(digits);
            std::size_t last = line.find_last_of(digits);
            result[0] = line[first];
            result[1] = line[last];

            total = total + stoi(result);
            std::cout << result;
            std::cout << "\n";
        }
    }
    std::cout << total;
}