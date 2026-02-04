total_money=int(input("Enter the total amount of money in MAD: \n"))
num_200=int(total_money//200)
# calculate remaining money after extracting 200 MAD bills
remaining_money=total_money%200
# calculate number of 100 MAD bills
num_100=remaining_money//100
# calculate remaining money 2 after extracting 100 MAD bills
remaining_money_2=remaining_money%100
# calculate number of 50 MAD bills 
num_50=remaining_money_2//50
# calculate remaining money 3 after extracting 50 MAD bills
remaining_money_3=remaining_money_2%50
# calculate number of 20 MAD bills
num_20=remaining_money_3//20
print(f"Results: \n200 MAD bills: {num_200} \n100 MAD bills: {num_100} \n50 MAD bills: {num_50} \n20 MAD bills: {num_20} ")
