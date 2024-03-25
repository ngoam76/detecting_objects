import src.data_preprocessing.extract_map as extract_map
from shapely import wkt
from shapely.geometry import Polygon

polygon_coords = []

def process_input(address1, address2, address3, address4, color, weight, zoom, size, maptype):
    address = [address1, address2, address3, address4]
    polygon_coords = []
    for i in address:
        polygon_coords.append(extract_map.extract_lat_lng(i))
    print(polygon_coords)
    # finding center point of 4 coords 
    polygon = Polygon(polygon_coords) # a list
    print(polygon)
    poly_wkt = polygon.wkt
    center_point = wkt.loads(f"{poly_wkt}").centroid.wkt
    lat_lng = center_point.replace("(", ")").replace(")", "").split(" ") # list

    coords_for_path = []
    # define path from 4 points
    for coord in polygon_coords:
        point_lat_lng = f"{coord[0]}, {coord[1]}"
        coords_for_path.append(point_lat_lng)
    path = f"color:{color}|weight:{weight}|{coords_for_path[0]}|{coords_for_path[1]}|{coords_for_path[2]}|{coords_for_path[3]}|{coords_for_path[0]}"

    # define parameters for the function
    center = f"{lat_lng[1]},{lat_lng[2]}"
    #print(extracting_map.plot_map(center, zoom, size, path))
    return str(extract_map.plot_map(center, zoom, size, path, maptype))