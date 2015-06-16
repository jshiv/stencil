#install homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#brew install gcc and freetds
brew install gcc
brew install freetds


curl -k https://stash.teslamotors.com/projects/REL/repos/relpy/browse/scripts/requirements.txt?raw -o requirements.txt
#install numpy, scipy, pandas, sklearn, seaborn
sudo pip install -r requirements.txt

