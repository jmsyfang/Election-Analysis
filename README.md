# Election-Analysis

## Project Overview
The Coloardo Board of ELections need to audit a recent local election, and would like us to calculate totals and the winning candidate. Our tasks were to

1. Calculate the total number of votes
2. Track each candidate
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of voters each candidate won
5. Determine who the overall winner is based on votes won/cast

## Resources
1. Data source: election_results.csv
2. Software: Python 3.7.6 and VSCode

## Results
- THere was a total of 369,711 votes cast
- Charles Casper Stockham won 23% of the votes (85,213)
- Diana DeGette won 73.8% of the votes (272,892)
- Anthony Doane won 3.1% of the votes (11,606)

-The final winner was Diana DeGette with 272,892 votes (73.8% of total votes)

## Summary
The python script can be worked again for future audits, as it scans results for candidates and tallies their votes. The results must be sorted by name to work correctly, but should find all candidates and their totals. It may be prudent to hard code the candidates (or a separate file) so tampering data is less of a security risk/incentive. For something like the presidential election (electoral college) you would need an if statement so that the winning candidate for each county (state) would take all their electoral points (either included in data or joined from other source/dictionary)
