from skyfield.api import EarthSatellite


def get_EarthSatellite_obj(line1,line2,satName):
    return EarthSatellite(line1,line2,satName)

def return_EarthSatellite_obj_iss(satName,catnr,line1,line2):
    return {
        "name": satName,
        "catnr": catnr,
        "EarthSatelliteObj": get_EarthSatellite_obj(line1, line2, satName)
    }

def return_EarthSatellite_obj_debris(debri):
    debris_obj=[]
    for debris in debri:
        debris_obj.append({
            "name":debris["objName"],
            "catnr":debris["catnr"],
            "EarthSatelliteObj":get_EarthSatellite_obj(debris["line1"],debris["line2"],debris["objName"])
        })
    return debris_obj