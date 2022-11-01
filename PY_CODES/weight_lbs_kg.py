#converting a user given lbs to kg

Weight_in_lbs = float(input("insert the weight per kg\n\n"))
weight_in_kgs = float(Weight_in_lbs * 2.20462)
roundedWeight = round(weight_in_kgs, 3) #print round number in 3 digit decimal
print(f"The weight in lbs: {Weight_in_lbs}, and the equivalent in kgs is: {roundedWeight} Thank You\n")