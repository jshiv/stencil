Install anaconda
curl -O https://repo.continuum.io/miniconda/Miniconda-latest-MacOSX-x86_64.sh
sh Miniconda-latest-MacOSX-x86_64.sh
rm Miniconda-latest-MacOSX-x86_64.sh

source ~/.bash_profile

conda install numpy
conda install scipy
conda install pandas
conda install matplotlib
conda install scikit-learn