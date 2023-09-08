// с++.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

int* gen() {
    int *a = new int[10];
    for (int i = 0; i < 10; i++) {
        a[i] = rand() % 200 - 100;
    }
    return a;
}

int max(int * a) {
    int m = a[0];
    for (int i = 1; i < 10; i++) {
        if (m < a[i]) m = a[i];
    }
    return m;
}
int main()
{
    int * a = gen();
    for (int i = 0; i < 10; i++) {
        std::cout << a[i] << " ";
    }
    std::cout << "\n" << max(a);
}

