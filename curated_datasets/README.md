# OpenBeta Curated Datasets

## Motivation
This directory contains datasets collected and curated from the raw OpenBeta data, the idea being to provide data in a rapidly useable format for data science projects.

## Current Status
The datasets can be downloaded as compressed (zip) pickles of Pandas data frames or as .csv files.
* __Curated_OpenBetaAug2020_RytherAnderson.pkl.zip__ is a dataset containing only technical rock climbs, with simplified types and reformatted grades. Please see the OpenBetaData_Curation Jupyter notebook for more information on how this set was built.
* __CuratedWithRatings_OpenBetaAug2020_RytherAnderson.pkl.zip__ contains the same data as the previous point but is merged with all the available user rating data.
* __All_Ratings.pkl.zip__ contains all the user rating data concatenated into one file.
* __BoulderSafety_and_Stars.csv__ contains the star ratings and safety grades of 24,278 boulder problems collected by Ryther Anderson using the Mountain Project API. Note that this set is not comprehensive (does not cover all states). However, it can be used to augment to existing OpenBeta database in some cases.
* __RouteQualityData.pkl.zip__ contains route and sector identifiers as well as several metrics of route quality calculated in the corresponding Jupyter notebook.

## Reading the Files
The pickle files can be read with Pandas, thus:
```
import pandas as pd
df = pd.read_pickle('CuratedWithRatings_OpenBetaAug2020_RytherAnderson.pkl.zip', compression='zip')
```
