#include <stdio.h>
#include "junto.h"

void
show_me_the_secret_key(void)
{
  char *key = "begin 644 -\n"
	      "M(E1E;&P@;64@86YD($D@9F]R9V5T+@I496%C:\"!M92!A;F0@22!R96UE;6)E\n"
    	      "M<BX*26YV;VQV92!M92!A;F0@22!L96%R;BXB\"@D*(\"`@(\"`@(\"T@0F5N:F%M\n"
    	      "M:6X@1G)A;FML:6X*\"E1H92!S96-R970@:V5Y('EO=2!A<F4@;&]O:VEN9R!F\n"
    	      "3;W(@:7,@(FMN;W=L961G92(N\"@``\n"
    	      "`\n"
    	      "end\n";

  printf("%s", key);
}

