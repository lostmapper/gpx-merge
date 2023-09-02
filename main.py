import glob
import gpxpy.gpx

if __name__ == '__main__':
    gpx_files = glob.glob('./input/*.gpx')

    print(f' {len(gpx_files)} GPX files found')

    combined_gpx = gpxpy.gpx.GPX()
    combined_gpx.nsmap['gpxtpx'] = 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1'

    for filename in gpx_files:
        gpx_file = open(filename, 'r')
        gpx = gpxpy.parse(gpx_file)

        for track in gpx.tracks:
            print(f'- {track.name}')
            combined_gpx.tracks.append(track)

    combined_file = open('./output/combined.gpx', 'w')
    combined_file.write(combined_gpx.to_xml("1.1"))

    print(f'{len(combined_gpx.tracks)} tracks successfully added.')
