# Google Playstore vs Apple Store

Data analysis using Juypiter Notebooks/Google Colab of two csv files.

- googleplaystore.csv
- AppleStore.csv


The data is from a few years ago and taken from a Dataquest.io project that introduces how to use Juypter Notebooks along with how to edit data on csv files.

Data from the spreadsheets included data from around the world.  Analysis task completed for the project included:

<br>
<br>

**Distingquishing which apps were in an English language format using the title of each application.**
- Python's ord fuction was used to assist with this process since any character under 127 is concidered English.

**Comparing the number of free vs paid apps in both stores.**
- To determine this, the headers for each csv file could be read to find the 'Price' Column, then a loop was created for each app store to find the number of free vs. paid apps there were in each store.

**Removing duplicate file names.**
- Some applications in the spreadsheets were duplicated.  It was discovered that many of these applications were duplicated based on number appstore reviews.  All information for each duplicate app was the same except the the number of reviews.  Over time the number of reviews would increase.  A max of all review could be determined and then delete any app this did not equal the max review number.

**Error Correction**
- Data from the Google Playstore included some erros with data types.  Pandas unique and sort functions were used to analysis the 'Rating' and 'Categories' columns to find datatypes that didn't match.  The 'Rating's column had an error in which one rating was 19, when it should have been within a range of 0-5.
