
# Passport Index Dashboard

The passport index is a passport ranking tool. Currently, it rankings passports in real-time, updating frequently as new changes are implemented. 

Users can can select a country from the drop down to get the passport mobility score.


## Dashboard Description
Select a country from the dropdown list to see the mobility score

## Data Sources
The  csv files were located from github. Below is a description, from that github, describing the datasets

There are 6 datasets with identical visa requirements data. Three datasets are matrix and three are long (tidy) format. Each comes in 3 versions: with country codes as specified in ISO-2 (two-letter codes), ISO-3 (three-letter codes), and full country names from no particular standard.

In distance matrices (files with matrix in the filename), the first column represents a passport (=from), each remaining column represents a destination (=to).
Files in tidy format (with tidy in filename) have three columns: passport (from), destination (to), and the requirement.

### Dataset values

For visa-free regimes, the number of days (a positive integer) is specified whenever available. When not available, `visa free` code is used (for example, in the EU countries with the freedom of movement days are not limited).

| Value | Explanation |
|---|---|
|`7`-`360`| Number of visa-free days, where available |
|`visa free`| Visa-free travel (where number of days is unknown or not applicable, such as freedom of movement), including tourist registration requirement for Seychelles|
|`visa on arrival`| Destinations that grant visa on arrival, basically visa-free |
|`e-visa`| Includes  [ESTA](https://esta.cbp.dhs.gov/) (Electronic System for Travel Authorization for the USA) and [eTA](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html) (Electronic Travel Authorization for Canada), eVisas, [eVisitors](https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/evisitor-651) in Australia, [eTourist cards](https://www.surinametourism.sr/tourist-card/) for Suriname, pre-enrollment for Ivory Coast, and UK's [electronic visa waivers](https://www.gov.uk/get-electronic-visa-waiver) |
|`visa required`| Obtaining a visa is required for travel. Includes Cuba's tourist cards |
|`covid ban`| Travelling is banned for most people. This is perhaps the most dynamic category right now, with varying exemptions|
|`no admission`| Includes rare tricky situations, such as war conflicts |
|`-1`| where passport=destination|


## Additional Comments
This project was inspired by the Passport Index project.

It can be accessed here: https://www.passportindex.org/

The github where the original files are located here: https://github.com/ilyankou/passport-index-dataset
