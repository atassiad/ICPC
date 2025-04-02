#include <math.h>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    //return vector
    vector<long double> returnVals;

    //get number of lines
    int t = 0;
    cin >> t;
    
    //iterate number of line times and find solution
    for (int i = 0; i < t; i++){
        long double R = 0;
        long double H1 = 0;
        long double H2 = 0;

        cin >> R >> H1 >> H2;
        H1 *= 0.001;
        H2 *= 0.001;

        
        //long double B1 = sqrt(pow(R + H1, 2)-pow(R, 2));
        //long double B2 = sqrt(pow(R + H2, 2)-pow(R, 2));

        //returnVals.push_back(B1+B2);

        long double Surface = R*acos(R/(R+H1)) + R*acos(R/(R+H2));
        returnVals.push_back(Surface);
    }

    //print all output values
    for (int i = 0; i < returnVals.size(); i++){
        cout << fixed << returnVals[i] << setprecision(9) << endl;
    }

    //return 0
    return 0;
}