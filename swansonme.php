<?php
      $message=shell_exec("/var/www/scripts/swansonme.sh 2>&1");
      print_r($message);
    ?>  