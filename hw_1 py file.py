def compareTriplets(Alice_user_input = input(), Bob_user_input = input()):

    total_comparison_dict = {"Alice":0,"Bob":0} # the dict to be returned as a result of the comparison 
        
    Alice_input = [int(inp) for inp in Alice_user_input.split(" ")]
    Bob_input = [int(inp) for inp in Bob_user_input.split(" ")]
    
    for index in range(len(Alice_input)):
        if Alice_input[index] > Bob_input[index]:
            total_comparison_dict["Alice"] += 1
        elif Alice_input[index] < Bob_input[index]:
            total_comparison_dict["Bob"] += 1
        else:
            pass

    comparison_list = [i for i in total_comparison_dict.values()]
    return comparison_list
    
print(compareTriplets())