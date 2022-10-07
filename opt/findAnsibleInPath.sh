#!/bin/bash



path_var=$(more /etc/environment | grep PATH)
search_substr='ansible'

if [[ $path_var = *$search_var*]]; then
    new_path='/home/ansible/.local/bin:$path_var';
    echo "newpath=$new_path";
#    cat >> /etc/environment
#    $new_path
#    EOF
  else
     echo " $path_var enthält schon $search_substr";
fi
  