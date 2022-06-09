// Holamundo.cpp
#include <iostream>
using namespace std;

int main(){
    double numero1;
    double numero2;
    double divide;
    cout << "Valor inicial numero1: " << numero1 << endl
        << "Valor inicial numero2: " << numero2 << endl;
    cout << "Valor inicial de divide: " << divide <<endl;
    cout << "Ingrese primer valor: ";
    cin >> numero1;
    cout << "Ingrese segundo Valor: ";
    cin >> numero2;
    divide = numero1 / numero2;
    cout << "La division: " << divide <<endl;
    return 0;
 }
