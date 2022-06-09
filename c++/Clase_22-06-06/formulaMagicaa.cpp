//Formula magica
#include <iostream>
using namespace std;

int main(){
    int N;
    double numero1;
    double numero2;
    double divide;
    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout << "¿Cuántos dígitos decimales?";
    cin >> N;
    cout.precision(N);
    cout << "Valor inicial numero1: " << numero1 << endl
         << "Valor inicial numero2: " << numero2 << endl;
    cout << "Valor inicial de divide: " << divide <<endl;
    cout << "Ingrese primer valor: ";
    cin >>numero1;
    cout << "Ingrese segundo valor: ";
    cin >> numero2;
    divide = numero1 / numero2;
    cout << "La division: " << divide << endl;
    return 0;
}
