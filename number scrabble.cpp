//  purpose : Played with the list of numbers between 1 and 9. Each player takes
//           turns picking a number from the list. Once a number has been picked, it cannot be picked
//           again. If a player has picked three numbers that add up to 15, that player wins the game.
//           However, if all the numbers are used and no player gets exactly 15, the game is a draw.
// Author: Amr Khaled Ahmed Abd Al Hamid Mohammed.
// version 2.0
// date of creating : 25/2
// ----------------------------------------------------------------------------------------------------------------------
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <thread>

using namespace std;

//calling the function
int check_for_string();
bool winner_checker(vector<int> &selected_numbers);

//here I defined the array as a global variable to use it in the entire program.
vector<int> num_list = {1, 2, 3, 4, 5, 6, 7, 8, 9};
int players = 2, current_player = 0;   //defined the variables.

vector<vector<int>> players_numbers(players, vector<int>()); // this part to make a 2D array , array for every player,
//to store the selected numbers for players


int main() {
    string choice;
    int selected_number;
    //this code make a list for every player to store the selected numbers to each of them such as 2D array.
    //print the rules
    cout << "Hello, in this game the winner who collects any three numbers, the summation of them = 15" << endl;
    cout << "*** Good luck ***" << endl << endl;

    while (!num_list.empty()) {
        //The Game will work until the numbers that can be selected run out
        cout<<endl<<endl;
        cout << "Player " << current_player + 1 << " you have ";
        for (int i:players_numbers[current_player])
            cout<<i<<", ";
        cout<<endl<<endl;
        cout<<"please select a number from the following list: " << endl;
        for (int number: num_list) { cout << number << ", "; }   //print the list.
        cout << endl;
        selected_number=check_for_string(); //this part call the function that take the input and check for any potential errors
        //the following part will check if the selected_number is a part of the list or no and store true if yes.
        bool find_condition = (find(num_list.begin(), num_list.end(), selected_number) == num_list.end());
        while (find_condition) {
            // this loop test by the find_condition and check again.
            cout << "Invalid number. Please player " << current_player + 1 <<" enter a number from the following list: \n";
            for (int number: num_list) { cout << number << ", "; }
            cout << endl;

            selected_number=check_for_string(); //this part call the function that take the input and check for any potential errors

            //check if the selected_number is a part of the list or noo and store true if yes again .
            find_condition = (find(num_list.begin(), num_list.end(), selected_number) == num_list.end());
        }
        //Add the selected number to the current_player as 2D array.
        players_numbers[current_player].push_back(selected_number);

        //Remove the selected number from the num_list.
        num_list.erase(remove(num_list.begin(), num_list.end(), selected_number), num_list.end());

        //this part send the array of the current player and check if he wins.
        bool condition_2 = winner_checker(players_numbers[current_player]);

        // This conditional statement prints the winner if one exists
        if (condition_2) {

            //print the winner player and the number that make him win.
            cout << "***** Player " << current_player + 1 << " win *****\n\n";

            cout<<"write \"yes\" if you Would like to play again and if you don not press any thing: ";
            cin>>choice;
            // this part convert the choice to upper case
            transform(choice.begin(), choice.end(), choice.begin(), ::toupper);
            if (choice == "YES"){
                // this part will clear all lists and assign the num_list again the repeat the game
                num_list.clear();
                players_numbers[1].clear();
                players_numbers[0].clear();
                num_list.assign({1,2,3,4,5,6,7,8,9});
                main();

            }else
                cout<<"Thank you for playing.\n";
                this_thread::sleep_for(chrono::seconds(2));
                return 0;

        }
        current_player = (current_player + 1) % players;  //this part switch between player 1 and player 2

    }


    //If all numbers in the array are selected, the word "Draw" will be printed.
    cout << "****** Draw ******" << endl;
    cout<<"write \"yes\" if you Would like to play again and if you don not press any thing: ";

    cin>>choice;
    // this part convert the choice to upper case
    transform(choice.begin(), choice.end(), choice.begin(), ::toupper);
    if (choice == "YES"){
        // this part will clear all lists and assign the num_list again the repeat the game

        num_list.clear();
        players_numbers[1].clear();
        players_numbers[0].clear();
        num_list.assign({1,2,3,4,5,6,7,8,9});
        main();

    }else {
        cout << "Thank you for playing.\n";
        this_thread::sleep_for(chrono::seconds(2));

        return 0;
    }
    return 0;
}


bool winner_checker(vector<int> &selected_numbers) {
/*This function to check who win after every choice by adding the selected numbers for the player who chose the last
 in different types to get the goal(15), then if the goal has been achieved the function will return the numbers
 which achieved our goal else it will return false and will not return the numbers.*/
    int size = selected_numbers.size();
    for (int i = 0; i < size - 2; ++i) {
        for (int j = i + 1; j < size - 1; ++j) {
            for (int k = j + 1; k < size; ++k) {
                if (selected_numbers[i] + selected_numbers[j] + selected_numbers[k] == 15) {
                    return true;
                }
            }
        }
    }
    return false;
}


int check_for_string() {
    // this function to check for the input if string or digit and if it is digit I will cast it to longlong and
    // return it. if it string T will  demand the input again until the user write a digit
    string temp;
    cin>>temp;
    while(true){
        bool is_digit=true;

        for(int i=0; i<temp.length(); i++){
            if(isdigit(temp[i])==0){
                is_digit= false;
                break;
            }
        }

        if(is_digit){
            int y= stoll(temp);

            return y;
        }
        else{
            cout<<"Please select a correct integer from the list: "<<endl;
            cin>>temp;
        }
    }
}



