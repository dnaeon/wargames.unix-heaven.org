#include <stdio.h>
#include <string.h>

int
main(void)
{
  char *password = "you.wont.guess.it!";
  char buf[1024];

  printf("What is the password: ");
  fgets(buf, 1024, stdin);
  buf[strlen(buf) - 1] = '\0';

  if (strcmp(buf, password) == 0) {
    printf("\nYou guessed it! Now, proceed to the next chapter! :)\n");
  } else {
    printf("\nI don't think so...\n\n");
  }

  return (0);
}
