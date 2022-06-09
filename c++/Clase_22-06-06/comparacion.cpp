//comparacion booleanos
#include <iostream>
using namespace std;
int main(){
    char car1,car2,car3= '=';
    bool salida;
    cout << "Ingrese dos caracteres separados entre si: ";
    cin >> car1 >> car2;
    salida = (car1 == car2);
    cout << "Resultado: " << car1 << car3 << car3 << car2
         << ": " << salida << endl;
    return 0;
}
