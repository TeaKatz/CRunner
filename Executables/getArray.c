#include <stdio.h>

int main(int argc, char *argv[]) {
	int input_size;
	int inputs[999];
	
	scanf("%d", &input_size);
	for (int i=0; i<input_size; i++)
	{
		scanf("%d", &inputs[i]);
	}

	for (int i=0; i<input_size; i++)
	{
		printf("%d ", inputs[i]);
	}
}