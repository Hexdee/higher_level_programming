#include <stdio.h>
void change(int *);

struct Car {
	int data;
	car *next;
};

typedef struct Car car;




int main(void)
{
	Car my_car;

	my_car.year = 2001;
	my_car.model = "camry";

	printf("The model of my car is %s\n", my_car.model);
}
/**
int main(void)
{
	int x = 5;
	int *ptr;
	change(&x);
	printf("The value of x is %d\n", x);
	//printf("Address of x is: %p", &x);
}

void change(int *num_ptr)
{
	*num_ptr = 98;
}
**/
