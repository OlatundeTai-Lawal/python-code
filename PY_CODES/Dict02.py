print("********print out the last of the Employees\n*******")

WORKERS  ={
    "Employees":[
        {
            "firstName":"John",
            "lastName":"Doe"
        },
        {
            "firstName":"Anna",
            "lastName":"Smith"
        },
        {
            "firstName":"Peter",
            "lastName":"Jones"
        }
    ],
    "Owners":[
        {
            "firstName":"Jack",
            "lastName":"Petter"
        },
        {
            "firstName":"Jessy",
            "lastName":"Petter"
        }
    ]
}

print("The Last Name of the second employee is: "+WORKERS["Employees"][1]["lastName"])
#Best = WORKERS["Employees"][2]["lastName"] # another method to print the name
#print(Best)