# PyPoll Analysis Challenge

## Overview of Election Audit

The election audit consists of the tabulated results for US congressional present in Colorado. Three primary methods are taken into account to cast votes: main-In ballots, punch cards and direct recording. All three methods are collected in the central office and compiled in a .csv file which is used as the source of the data set for the audit.

The objective of the audit is as follows:
* Count the total number of votes cast
* Number of votes for each candidate
* Percentage of votes for each candidate 
* Winner of the election based on the popular vote

In order to complete the task, the manager has asked if there is a way to automate the process using python so it can be used to audit not only other congressional districts but also senatorial districts and local elections. Once the votes are counted, a vote count report is expected to be generated to certify the US congressional race.

In addition to the previous task, the election commission has requested additional data to complete the audit. These include the following:
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

The additional task is also expected to be added to the vote count report.

---
## Election-Audit Results

In order to complete the objectives of the election audit, the following script was built:

* Added dependencies csv and os to read/write .csv and txt files and get their paths 

	import csv
	import os
* Added two variables, one to load a file from a path and another to save the file to a path 

	file_to_load = os.path.join("Resources", "election_results.csv")
	file_to_save = os.path.join("analysis", "election_analysis.txt")

* For the total votes casted in the congressional election:
	*The variable total_votes counter was initialized to 0
	
		total_votes = 0
		
	*The data set in the csv file is open and read with the following code
	
		with open(file_to_load) as election_data:
    			reader = csv.reader(election_data)
			
	*For loop was created in order to go through each row and add the total vote count
	
			for row in reader:
 				total_votes = total_votes + 1
	
The results showed that the total votes casted were 369,711

![](Total_Votes.png)

* The number of votes and percentage of total votes for each county was estimated as follows:

	*A county list and a county dictionary were created
  
		county_options = []
		county_votes = {}
    
	*An if statement created to check if a county name doesn’t match an existing county in the county list then the county name is added to the list of counties. The county’s vote starts tracking and adding votes to that county’s vote count
  
       if county_name not in county_options:
            county_options.append(county_name)	
      			county_votes[county_name] = 0
 			    county_votes[county_name] += 1
      
	*For the percentage a for loop was created to get the county from the county dictionary. The county vote count was retrieve and the percentage of votes for the county was calculated 
  
		  for county_name in county_votes:
        	votescounty = county_votes.get(county_name)
        	votescounty_percentage = float(votescounty) / float(total_votes) * 100

The breakdown of the number of votes and the percentage of total votes for each county is shown in image below:

![](County_Votes.png)

* The county with the largest amount of votes was determine using an if statement:

    	  if (votescounty > winning_county_count):
            	winning_county_count = votescounty
            	winning_county = county_name

The largest county turnout was Denver, see image below:

![](Largest_County_Turnout.png)

* The number of votes and percentage of total votes for each candidate received was determined using the same logic as for each county, the code is show bellow:

		candidate_options = []
		candidate_votes = {}

    
    
        if candidate_name not in candidate_options:
          candidate_options.append(candidate_name)
          candidate_votes[candidate_name] = 0
          candidate_votes[candidate_name] += 1

    
        for candidate_name in candidate_votes:
              votes = candidate_votes.get(candidate_name)
              votes_percentage = float(votes) / float(total_votes) * 100

The breakdown of the number of votes and the percentage of total votes for each candidate is shown in image below:

![](Candidates_Votes.png)

* The candidate that won the election with its respective vote count and percentage is show below and it was determined with an if statement
 
![](Winner.png)



---
## Summary

* In general the advantages of refactoring is less time taken by the programmer to build a script compared to building it from scratch. It takes fewer steps, uses less memory and improves the logic of the code to make it easier for future users. Some disadvantages could be if the refactoring of the code is done on a script without enough documentation this could be time consuming.
* On the current Stock Analysis refactoring code, there was an improvement in execution time making easier for the user to incorporate more data for future analysis.


---
