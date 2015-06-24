#https://github.com/barryclark/bashstrap
echo "updating bash"


mv ~/.bash_profile ~/.bash_profile_backup
#get the .bash_profile
curl -k https://gist.githubusercontent.com/jshiv/41cc660b317abaf7a82b/raw/8e681877bc7ab7c49b644cfe77cfc49d5b1730f3/.bash_profile -o ~/.bash_profile

#get the z script
curl -k https://raw.githubusercontent.com/rupa/z/master/z.sh -o ~/z.sh



 
check_if_line_exists()
{
    # grep wont care if one or both files dont exist.
    grep -qsFx "$LINE_TO_ADD" ~/.profile ~/.bash_profile
}
 
add_line_to_profile()
{
    profile=~/.profile
    [ -w "$profile" ] || profile=~/.bash_profile
    printf "%s\n" "$LINE_TO_ADD" >> "$profile"
}
 




echo "Please enter your desired default startup directory: Example ~/Documents"
read LOC
LINE_TO_ADD="cd $LOC"
check_if_line_exists || add_line_to_profile



source ~/.bash_profile
