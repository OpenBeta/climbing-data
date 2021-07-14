# Open Beta Curated Datasets

## Motivation
This directory contains datasets collected and curated from the raw Open Beta data, the idea being to provide data in a rapidly useable format for data science projects.

## Current Status
The datasets can be downloaded as compressed (zip) pickles of Pandas data frames or as .csv files.
* Curated_OpenBetaAug2020_RytherAnderson.pkl.zip is a dataset containing only technical rock climbs, with simplified types and reformatted grades. Please see the OpenBetaData_Curation Jupyter notebook for more information on how this set was built.
* CuratedWithRatings_OpenBetaAug2020_RytherAnderson.pkl.zip contains the same data as the previous point but is merged with all the available user rating data.
* All_Ratings.pkl.zip contains all the user rating data concatenated into one file.
* Boulder_Safety_and_Stars.csv contains the star ratings and safety grades of 24,278 boulder problems collected by Ryther Anderson using the Mountain Project API. Note that this set is not comprehensive (does not cover all states). However, it can be used to augment to existing Open Beta database in some cases.
