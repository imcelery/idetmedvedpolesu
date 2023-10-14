#include <set> // подключаем set
#include <string> // подключаем строки string
#include <iostream> // подключаем cout
 
using namespace std; // чтобы не писать std::
 
int main()
{
 set <int> s; // инициализация set
 s.insert(3);
 s.insert(2);
 
for (const int &number : s) {
  cout << number;
}
}