# pyGAPS-v.4.4.0-python3.8-template


## tested with Ubumtu 20.04 LTS or Ubumtu 22.04 LTS (on Windows 10).


## Install (New)
1. cd ~
2. sudo apt update
3. sudo apt -y install python3-pip
4. pip3 install pygaps==4.4.0
5. git clone https://github.com/by-student-2017/pyGAPS-v.4.4.0-python3.8-template.git
6. cd ~/pyGAPS-v.4.4.0-python3.8-template
7.  chmod +x run.sh
8.  chmod +x run_sequential.sh


## initial setting for desorption data
1. cd ~/pyGAPS-v.4.4.0-python3.8-template
2. python3 set_case.py


(2. python3 set_case_tab.py) (When the numeric data is separated by tab.)


3. mv case.csv case_original.csv
4. mv new_case.csv case.csv


## Usage -1-
1. cd ~/pyGAPS-v.4.4.0-python3.8-template
2. python3 dft_fit_csv_des.py
3. (see plot directory)
4. (write your data on case.csv, please.)


## Usage -2-
1. cd ~/pyGAPS-v.4.4.0-python3.8-template
2. ./run.sh | tee ./plot/info.txt
3. (see plot directory)
4. (write your data on case.csv, please.)


## Usage -3-
1. cd ~/pyGAPS-v.4.4.0-python3.8-template
2. ./run_sequential.sh
3. (see plot_sequential directory)
4. (write your data on *.csv file in sequential_data directory, please.)


## Ubuntu 20.04 LTS or Ubuntu 22.04 LTS (WSL version case)
1. sudo apt install x11-apps
2. echo 'export DISPLAY=localhost:0.0' >> ~/.bashrc
3. source ~/.bashrc
4. sudo apt -y install python3-tk
5. (plase install XLaunch)


## Arial font
- sudo apt -y install ttf-mscorefonts-installer


## case.csv (input condition and data) [P/P0 vs. cm^3 (STP)]
	iso_type,Isotherme
	is_real,true
	pressure_mode,relative
	pressure_unit,None
	loading_basis,molar
	loading_unit,cm3(STP)
	adsorbent_basis,mass
	adsorbent_unit,g


## delta S plot from NLDFT (kernel: carbon slit)
	dS [m2/g] = d(Cumulative V) [cm3/g] / (W [nm] / 2) * 1000


## NLDFT
* For academic societies and treatises, 23 points or more are recommended for P/P0 =< 0.02, and 26 points or more for P/P0 > 0.02.


Maybe, PSD-plot_pygaps_v303.py is for python 3.9.