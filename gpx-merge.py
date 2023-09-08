#!/usr/bin/env python3

"""Merge tracks from multiple GPX files into one GeoPackage file and one GPX file"""
import glob

import geopandas
import pandas

if __name__ == "__main__":
    gpx_files = glob.glob("./input/*.gpx")

    print(f"{len(gpx_files)} GPX files found")

    merged_tracks = geopandas.GeoDataFrame(
        columns=["name", "type", "geometry"], geometry="geometry"
    )

    print("Merging", end="")
    for filename in gpx_files:
        tracks = geopandas.read_file(filename, layer="tracks")
        merged_tracks = pandas.concat(
            [merged_tracks, tracks[["name", "type", "geometry"]]]
        )
        print(".", end="", flush=True)
    print("")

    merged_tracks.to_file("./output/merged.gpkg", driver="GPKG")
    merged_tracks.to_file("./output/merged.gpx", driver="GPX")

    print(f"{len(merged_tracks.index)} tracks merged into the following files:")
    print("- output/merged.gpkg")
    print("- output/merged.gpx")
