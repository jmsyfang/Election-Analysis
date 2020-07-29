#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#for county in counties:
#    print(county)



#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, vote in counties_dict.items():
    print(f"{county} county has {vote} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
#    print(county_dict['county'])
    message_to_send = (
    f"{county_dict['county']} county has {county_dict['registered_voters']} number of votes. ")
# 
    print(message_to_send)
