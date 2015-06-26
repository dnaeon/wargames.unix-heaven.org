#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <syslog.h>

int 
main(int argc, char *argv[]) 
{
  FILE *fp;
  /* keyfile is represented using char + 13 (rot13) for the abs path,
     useful for avoing strings(1) to dump the file name
  */ 
  int keyfile[] = { 
		  60, 131, 110, 127, 60,
		  121, 118, 111, 60, 113,
		  125, 120, 116, 60, 129,
		  127, 118, 116, 116, 114,
		  127, 128, 60, 115, 127,
		  125, 114, 127, 116, 58,
                  133, 127, 121, 59, 62, 64
		 };

  int i;
  int keylen = 36;
  char buf[1024];
  pid_t pid, sid;


  /* some fake strings in here.. */
  const char *fake1 = "you.think.you.found.the.key?";

  /* Clone ourselves to make a child */
  pid = fork(); 

  /* If the pid is less than zero,
   *    something went wrong when forking */
  if (pid < 0) {
    exit(EXIT_FAILURE);
  }

  /* If the pid we got back was greater
   *    than zero, then the clone was
   *       successful and we are the parent. */
  if (pid > 0) {
    exit(EXIT_SUCCESS);
  }

  /* If execution reaches this point we are the child */
  /* Set the umask to zero */
  umask(0);

  /* Open a connection to the syslog server */
  openlog(argv[0], LOG_NOWAIT|LOG_PID,LOG_USER); 

  /* Sends a message to the syslog daemon */
  syslog(LOG_NOTICE, "Successfully started beastie\n"); 

  const char *fake2 = "seriously.there.is.nothing.here.for.you!";

  /* Try to create our own process group */
  sid = setsid();
  if (sid < 0) {
    syslog(LOG_ERR, "Could not create process group\n");
    exit(EXIT_FAILURE);
  }

  /* Change the current working directory */
  if ((chdir("/")) < 0) {
    syslog(LOG_ERR, "Could not change working directory to /\n");
    exit(EXIT_FAILURE);
  }

  const char *fake3 = "are.you.still.reading.these.strings???";

  /* Close the standard file descriptors */
  close(STDIN_FILENO);
  close(STDOUT_FILENO);
  close(STDERR_FILENO);

  /* decode the keyfile */
  for (i = 0; i < keylen; i++)
	buf[i] = keyfile[i] - 13;

  buf[i] = '\0';

  /* Open the secret-key file */
  if ((fp = fopen(buf, "r")) == NULL) {
    syslog(LOG_NOTICE, "Cannot open the secret-key file\n");
    exit(EXIT_FAILURE);
  }

  /* A useless payload ... */
  while (1) {
    sleep(3600);
  }

  /* Close the secret-key file */
  fclose(fp);

  /* this is optional and only needs to be done when your daemon exits */
  closelog();

  return (0);
}
