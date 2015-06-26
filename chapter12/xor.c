#include <stdio.h>
#include <string.h>

int
main(void)
{
	//int f[] = { 115 , 118, 121, 114 };
	char f[] = "/var/lib/dpkg/triggers/frperg-xrl.13";
	char buf[1024];
	char key[] = "key";

	int i;
	for (i = 0; i < strlen(f); i++) {
		printf("%i, ", f[i] + 13 );
}


/*
	buf[i] = '\0';
	printf("%s", buf);
	return 0;
*/
}
	
