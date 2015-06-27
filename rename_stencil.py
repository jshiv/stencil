#use: 
#Change the top level directory to the name you want to use and run this file via 'sh rename_stencil.sh'

repo_name=${PWD##*/} 
echo "Changing folders and files from 'stencil' to '$repo_name'" 
mv ./stencil ./$repo_name
find . -type f -name "*.py" -exec sed -i -e 's/stencil/$repo_name/g' {} +
