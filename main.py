from geojson import Feature, Point, FeatureCollection
import geojson
import random


def calc_xy(min_point, max_point, step):
    return_list = []

    lng = min_point[0]
    lat = min_point[1]

    while lat <= max_point[1]:
        while lng <= max_point[0]:
            # print("%s %s" % (lng, lat))
            return_list.append((lng, lat))
            lng += step
        lng = min_point[0]
        lat += step

    return return_list


def rand_pm(defined_pm):
    return defined_pm + random.randint(-5, 3)


def rand_property(counter, defined_pm1_0, defined_pm2_5, defined_pm10):
    return {"id": counter, "valueType": "double", "Accel_value": [0.79487495117187, 0.22266075439453, 9.3182328613281], "Gyro_value": [-4.2442748091603, -1.9389312977099, 0.12213740458015], "Angle_value": [4.8743244857828, 1.3638805285541, 5.0624319560414], "Heading_value": 74.36789465706832, "FineDust_value": [rand_pm(defined_pm1_0), rand_pm(defined_pm2_5), rand_pm(defined_pm10)], "FineDust_instant": None, "Temp_value": 2.2947, "instant": 1571639038}


def generate_feature(counter, geometry, defined_pm1_0, defined_pm2_5, defined_pm10):
    return Feature(geometry=Point(geometry), properties=rand_property(counter, defined_pm1_0, defined_pm2_5, defined_pm10))

def generate_features(geometry_list, pm):
    feature_list = []
    for idx, geo in enumerate(geometry_list):
        feature_list.append(generate_feature(idx, geo, pm[0], pm[1], pm[2]))

    return FeatureCollection(feature_list)


def export_coordinate_to_csv(geometry_list):
    f = open('./coordinates.csv', 'w')
    for geo in geometry_list:
        f.write("%f,%f\n" % geo)
    f.close()


def export_geojson(json):
    f = open('./export.json', 'w')
    f.write(json)
    f.close()


if __name__ == "__main__":
    min_point = (127.106029, 35.821002)
    max_point = (127.111782, 35.825264)
    geometry_list = calc_xy(min_point, max_point, 0.0005)

    pm = [float(27), float(31), float(28)]

    my_features = generate_features(geometry_list, pm)
    json = geojson.dumps(my_features, indent=4)






