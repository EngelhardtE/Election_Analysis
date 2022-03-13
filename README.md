# Election_Analysis

##Overview of Election Audit

The purpose of this election audit analysis is to use Python to process a .csv file of votes into easy to read results. Intead of manually counting or having ti import the .csv into Excel everytime an election occurs, one can now simply use the provided .py file to obtain the election results. One is also given the breakdown on a county level, which allows for further analysis to be made on voter turnout.  

##Election Audit Results

-There were a total of 369,711 votes cast in the election
-The county vote breakdown was as follows: Denver 306,055 votes (82.8%), Jefferson 38,855 votes (10.5%), and Arapahoe 24,801 votes (6.7%)
-Denver county had the largest voter turnout
-The candidate vote breakdown is as follows: Diana DeGette 272,892 (73.8%), Charles Casper Stockham 85,213 (23%), and Raymon Anthony Doane 11,606 (3.1%)
-Diane DeGette won the election with a total of 272,892 votes, which was 73.8% of the total votes cast.

##Election-Audit Summary
While this code works effectively for the data provided for this particular election, it could also be used for other elections with some minor modifications. Depending on how deep the desired analysis is, different amounts of variables may be provided. This could lead to rows in the .csv file being shifted around, which means that the following two lines of code would have to be altered: 
            
          county_name = row[1]
          
          candidate_name = row[2]
          
For example, if the county_name row were shifted two to the right in order to make space for new variables, or if the .csv file for the new election was simply formatted differently, then the new code would have to read: 
         
         county_name = row[3]
          
Furthermore, it should be noted that "county" and "candidate" are just variable names that can be changed to suit different types of elections. Candidate can be changed to "organization" or "party" and county can be changed to "district" or "state". As long as it is changed consistently throughout the code's variables, it will function the same.        
