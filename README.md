# Ulauncher Discogs Search
> Ulauncher extension for quickly searching for Discogs releases.

## Install
Open Ulauncher Preferences and click "Add Extension" link, then paste the url of this repository:
```https://github.com/slurpyb/ulauncher-discogs-search```
[About Extensions](https://ext.ulauncher.io/about)

### Requirements
* [ulauncher 5](https://ulauncher.io/)
* A Discogs API Personal Access Token
    * Search queries require Authentication. 
    * Create a Discogs account and/or create a Personal Access Token [here](https://www.discogs.com/settings/developers)
    * Enter your Discogs Personal Access Token inside this extensions preferences inside the Ulauncher settings UI.

### Usage
> Use the `dc` prefix followed by your search term
``` dc Voodoo People```

### Configuration
The extensions settings has support for:
* API/Personal Access Token (default=None)
* Description formatting (default='{id} • {genre} • {label}: {country}')
    * Supported fields:
        * id
        * title
        * label
        * genre
        * country
        * url
        * thumb
* Max results to display (default=5)

### Todo
* Marketplace statistics
* Add support for search types:
    * release
    * master
    * artist 
    * label
* add support for additional parameters to narrow search:
    * year
    * artist
    * label
    * genre
    * format
    * track names
    * style
    * credit
    * catno

* Collection / wantlist support
* Find only releases with videos, and launch them directly
* Thumbnail/icon support

### Contributions
Pull requests, contributions and feature requests are welcome.

### License

MIT License

