import os 

def export_vars(request):
    data = {}
    data['DEVELOPMENT'] = os.environ.get("DEVELOPMENT")
    return data