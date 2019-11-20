import os 

def export_vars(request):
    data = {}
    data['DEVELOPMENT'] = os.environ.get("DEVELOPMENT")
    data['CONTINENTS'] = [('ASIA','Asia'),('AFRICA','Africa'),('ANTARCTICA', 'Antarctica'),('AUSTRALIA', 'Australia'),('N_AMERICA', 'North America'),('S_AMERICA', 'South America'),('EUROPE', 'Europe'),]
    # ['ASIA', 'AFRICA','ANTARCTICA','AUSTRALIA','N_AMERICA','S_AMERICA','EUROPE', ]
    
    return data

