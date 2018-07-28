#include <stdio.h>
#include <unistd.h>

void main()
{
	int pid = 0;

	printf("the parent is going to fork\n");
	if((pid = fork()) != 0)
		printf("I am the father of %d\n", pid);
	else
		printf("I am the child\n");
}
