# GPX Tracks Merge

A small Python script to merge the tracks from multiple GPX files into a single GPX and single GeoPackage file.

## Usage

1. Place your GPX files in the `input` folder.
2. Run the script.
3. Find your combined tracks in `output/combined.gpkz` and `output/combined.gpx`.

### Downloading Bulk Data from Strava

If you're looking to download all your GPX files from Strava at once:

1. Head to <https://www.strava.com/athlete/delete_your_account>
2. Click on `Request Your Archive`
3. Don't delete your account!
4. Wait for an email from Strava
5. Unzip the archive
6. Copy the GPX files from the archive into the `input` directory of this project.
7. Follow the instructions in Usage
