
def top():
    top_companies = [
        "Google India",
        "Amazon India",
        "Microsoft India",
        "Goldman Sachs",
        "Morgan Stanley",
        "Adobe",
        "IBM",
        "Samsung Research Institute, Bangalore",
        "Samsung Research Institute, Noida",
        "Intuit",
        "Barclays"
    ]
    return  top_companies

def passer(sector):
    if sector=='IT':
        return tech
    elif sector=='Analytics/Consulting':
        return analytics
    elif sector=='Finance':
        return finance
    elif sector=='Core':
        return core_eng
    elif sector=='PSU':
        return psu
    elif sector=='Banking':
        return banking
    elif sector=='Telecom':
        return telecom
    elif sector=='Healthcare':
        return health
    elif sector=='Others':
        return others

tech = [
    "Google India", "Amazon India", "Amazon India(wow)", "Microsoft India", "Adobe", "IBM", "Intuit", "Atlassian",
    "Arista Networks", "Instabase", "Inmobi", "Indeed", "Meesho", "Flipkart", "Cashfree", "Field Genie Pvt Ltd",
    "Expedia", "Amdocs", "Wipro Limited", "Cognizent", "Capgemini", "Nineleaps", "Toppr", "Unacademy",
    "Accenture India", "Accenture Japan", "Accenture India (2nd Drive)", "PwC", "PWC", "Newzera", "Simpl Technology"
]
    

analytics= [
"Axtria", "Merilytics", "Tiger analytics", "ZS Associates", "Quantiphi", "Cubation Consulting",
"Axxela Advisory", "Latent Analytics", "Decimal Technologies", "Brigosha Technologies", "Cogoport",
"Beehyv", "DarwinBox"
]
    


finance= [
"Goldman Sachs", "Morgan Stanley", "Standard Chartered", "Barclays", "American Express", "Florance Capital",
"Florence Capital (2nd Drive)", "Razorpay", "Sliceit", "Money Forward", "Navi Technology", "Paytm"
]
    
core_eng = [
"Tata Steel", "Tata Steel_Enviro", "Tata Steel Long Product Ltd", "Tata Electronics Pvt. Ltd",
"Vedanta Ltd", "Vedanta_ESL Ltd.", "L&T Construction", "L&T Infotech", "Schneider Electric",
"Scheneider Electic", "Sterlite Technologies LTD", "Texas Instrument", "Aarti Industries",
"Aditya Birla", "Cairn Oil &Gas", "Essar enp", "ExxonMobil", "Jaguar Landrover", "Hitachi Vantara",
"John Deere", "Terex", "Holcim Group_ACC cement", "Bajaj Auto", "DG Takano", "Mathwork"
]


banking= [
"ICICI Bank",
"Axis Bank",
"SUDLife",
"Standard Chartered",
"CRISIL",
"Deutsch Bank" 
]
    

health = [
"Medibuddy", "MediBuddy", "Innovaccer", "Jubilant Pharmova Ltd"
]
    


telecom = [
"Reliance Jio", "Reliance Jio (TS1)", "Reliance Jio (TS2)", "Reliance Industries (E&P)", "Sling Media", "Swiggy"
]
    

psu = [
"ONGC", "CDAC", "Bharat Electronics Ltd."
]
    


others = [
"Toyokoh",
"Instalimb",
"I'm Beside You",
"Simwell",
"Lumenci",
"Addverb"
]
     