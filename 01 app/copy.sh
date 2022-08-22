#!/bin/bash
echo "Bash version ${BASH_VERSION}..."

for i in {0..100}
do
  echo "-----go to cooky_images and push github"
  cd /Volumes/PhoData/tep 
  git pull
  git add .
  git commit -m "update"
  git push
  echo "-----go to image source and copy to cooky_images"
  cd /Volumes/PhoData/tep_new
  find  . | head -n 10 | xargs -I {} mv -v {} /Volumes/PhoData/tep 
done