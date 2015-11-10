#https://github.com/barryclark/bashstrap
echo "updating bash"

#make sublime text work
sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/bin/subl

mv ~/.bash_profile ~/.bash_profile_backup
#get the .bash_profile
curl -k https://gist.githubusercontent.com/anmolgarg/9eccfe9ff975e22149fe/raw/.bash_profile -o ~/.bash_profile

#get the z script
curl -k https://raw.githubusercontent.com/rupa/z/master/z.sh -o ~/z.sh

 


source ~/.bash_profile
