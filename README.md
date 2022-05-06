
# Passport Index Dashboard

The passport index is a passport ranking tool. Currently, it rankings passports in real-time, updating frequently as new changes are implemented. 

Users can can select a country from the drop down to get the passport mobility score.


## Dashboard Description
## Data Sources
The  csv files were located from github. Below is a description, from that github, describing the datasets


There are 6 datasets with identical visa requirements data. Three datasets are matrix and three are long (tidy) format. Each comes in 3 versions: with country codes as specified in ISO-2 (two-letter codes), ISO-3 (three-letter codes), and full country names from no particular standard.

In distance matrices (files with matrix in the filename), the first column represents a passport (=from), each remaining column represents a destination (=to).
Files in tidy format (with tidy in filename) have three columns: passport (from), destination (to), and the requirement.
## Additional Comments
This project was inspired by the Passport Index project. 
It can be accessed here: https://www.passportindex.org/

The github where the original files are located here: https://github.com/ilyankou/passport-index-dataset