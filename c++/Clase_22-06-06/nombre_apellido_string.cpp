//nombre apellido string
#include <iostream>
#include <string>
using namespace std;
int main(){
    string Nombre,Apellido;
    char c = ' ';
    cout << "Ingrese su nombre y apellido: ";
    cin >> Nombre >> Apellido;
    cout << "Bienvenido, " << Nombre << c << Apellido << endl;
    return 0;
}
