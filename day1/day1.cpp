#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>


void part1 (std::vector<int> vectora, std::vector<int> vectorb){
    std::sort(vectora.begin(), vectora.end());
    std::sort(vectorb.begin(), vectorb.end());
    int sum = 0;
    for (int i=0; i<vectora.size(); i++){
        sum += std::abs(vectora[i] - vectorb[i]);
    }
    std::cout << "Part 1:\n" << sum <<"\n";

}

void part2 (std::vector<int> vectora, std::vector<int> vectorb){
    std::map<int, int> map_vector2;

    for (int i=0; i<vectorb.size(); i++){
        
        if (map_vector2.find(vectorb[i]) != map_vector2.end()){
            map_vector2[vectorb[i]] += 1;

        }
        else{
            map_vector2[vectorb[i]] = 1;
        }
    }

    int sum = 0;
    for (int i=0; i<vectora.size(); i++){
        if (map_vector2.find(vectora[i]) != map_vector2.end()){
            sum += vectora[i] * map_vector2[vectora[i]];
        }
    }

    std::cout << "Part 2:\n" << sum <<"\n";


}

int main(){
    std::ifstream inputfile {"./day1_input.txt"};
    // std::ifstream inputfile {"./day1_input.txt"};

    std::string line;
    std::vector<int> vectora, vectorb;

    if (inputfile.is_open()){
        while (getline(inputfile, line)){   // rejects the last newline operator itself
            // std::cout << "reading line:" << line << "\n"; 

            std::size_t first_space = line.find_first_of(" ");
            std::size_t last_space = line.find_last_of(" ");
            
            int  a = std::stoi(line.substr(0, first_space));
            int  b = std::stoi(line.substr(last_space+1)); 
        
            vectora.push_back(a);
            vectorb.push_back(b);
        }
        inputfile.close();
    }
    
    part1(vectora, vectorb);
    std::cout << "-------------- \n";
    part2(vectora, vectorb);
    

    return 0;

}