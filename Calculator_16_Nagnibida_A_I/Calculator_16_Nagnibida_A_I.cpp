#include <iostream> //Библиотека ввода вывода
#include <string> //Библиотека работы со строками
#include <sstream> //Библиотека для преобразования строк в числа
#include <iomanip> //Библиотека для форматирования вывода

int a = 0;
int b = 0;
int result = 0;
//Функция для ввода шестнадцатеричного числа, принимает строку подсказку, возврачает число в десятичном виде

int inputHex(std::string promt) {
	std::string input;
	int number;
	std::cout << promt;
	getline(std::cin, input);
	std::stringstream ss; //Создаем поток для проебразовании строки в число
	ss << std::hex << input; //Записываем строку в поток, hex означает что число в шестнадцатеричной системе
	ss >> number; //Преобразуем поток в число
	return number;
}

//Функция сложения на ассемблере принимает 2 числа и возвращает их сумму
int addAsm(int x, int y) {
	int result_asm = 0;
	__asm {
		mov eax, x //Загружаем 1 число
		mov ebx, y //Загружаем 2 число
		add eax, ebx //Складываем в eax
		mov result_asm, eax //Сохраняем результат из eax в переменную
	}
	return result_asm;
}

int main()
{
	setlocale(LC_ALL, "Rus");
	std::cout << "================" << std::endl;
	std::cout << "Введите числа в HEX (Например: 1F, A3, 100)"<<std::endl;
	a = inputHex("Введите первое число в HEX: ");
	b = inputHex("Введите второе число в HEX: ");
	result = addAsm(a, b);

	std::cout << "Результат: " << result;
	return 0;
}