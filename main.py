"""Merge tracks from multiple Strava GPX files into one Geopackage file and one GPX file"""
import glob

import geopandas
import pandas

if __name__ == "__main__":
    gpx_files = glob.glob("./input/*.gpx")

    print(f"{len(gpx_files)} GPX files found")

    combined = geopandas.GeoDataFrame(
        columns=["name", "type", "geometry"], geometry="geometry"
    )

    for filename in gpx_files:
        tracks = geopandas.read_file(filename, layer="tracks")
        combined = pandas.concat([combined, tracks[["name", "type", "geometry"]]])

    combined.to_file("./output/combined.gpkg", driver="GPKG")
    combined.to_file("./output/combined.gpx", driver="GPX")
