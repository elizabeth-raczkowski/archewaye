#Archewaye Pricing

interiors = {

    #Residential Interiors
    'trailer':3000,
    'auction':5000,
    'the crest':4500,
    'fixer-upper':4000,
    'studio':1000,
    'ranch':5500,
    'philips':1500,
    'modest':1500,
    'modern':1500,
    'de santa':3500,
    'classic':4000,
    'city view':3500,
    'clinton':2500,
    'banham':5000,
    'paul':10000,

    #Warehouses

    #Offices

    #Storefronts
}

#Variables for the equation
designer_amount = float(input("Enter the amount of designers working on this project: "))
interior = input("Enter the interior: ")
furniture = float(input("Enter the furniture estimation: "))
construction = float(input("Enter the construction fee: "))
consultation = 2000
designer = furniture * 0.40

#Equation for project
projectAmount = consultation + furniture + designer + construction + interiors.get(interior)

#Equation for designer pay
payOut = (projectAmount - furniture) / designer_amount

#Display prices
print("The project costs ", projectAmount)
print("Each designer is paid ", payOut)

