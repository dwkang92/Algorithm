#include <iostream>

int main()
{
    using namespace std;

    int birthYear;
    int birthMonth;
    int birthDay;

    cout << "Year?" << endl;
    cin >> birthYear;

    cout << "Month?" << endl;
    cin >> birthMonth;

    cout << "Day?" << endl;
    cin >> birthDay;

    cout << "You broned in " << birthYear << "/" << birthMonth << "/" << birthDay << " " << endl;

    return 0;
}
