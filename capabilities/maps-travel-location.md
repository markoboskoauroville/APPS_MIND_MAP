[Back to the index](../CAPABILITIES.md)

# Maps, travel and location

## Which one to pick: Maps, location, transit

Offline maps: Mantra Map Server (MANTRA_MAP_SERVER, 8088) serves mapsforge maps as z/x/y PNG tiles from a phone; MANTRA_MAPS holds the map files; Mantra Trail (MANTRA_TRAIL) is the Android outdoor map for Croatian mountains. Croatian cadastral parcels: ARKOD (mantra_arkod Android, arkod_web PWA). Everyday finders: SHOP_FINDER (shops and pools), spar_locator, Maha Commute (MAHA_COMMUTE, Zagreb and Rijeka transit) and ZET Strike (zet_strike, 8100).

| You want | Use | How |
|---|---|---|
| get an offline map tile | [Mantra Map Server (MANTRA_MAP_SERVER)](../apps/MANTRA_MAP_SERVER.md) | `curl -s http://127.0.0.1:8088/tiles/croatia/10/553/366.png -o tile.png` |
| hike with offline maps and routing | [Mantra Trail (MANTRA_TRAIL)](../apps/MANTRA_TRAIL.md) |  |
| see Croatian cadastral parcels on a map | [ARKOD Layer (web) (arkod_web)](../apps/arkod_web.md) |  |
| find the nearest shop or pool | [Store & Pool Finder (SHOP_FINDER)](../apps/SHOP_FINDER.md) | `curl -s http://127.0.0.1:8900/shopfinder/health` |
| next tram or bus in Zagreb or Rijeka | [Maha Commute (MAHA_COMMUTE)](../apps/MAHA_COMMUTE.md) | `curl 'http://127.0.0.1:8084/board?city=rijeka&stop=1734&mins=90'` |
| next ZET tram during the strike | [ZET Strike (zet_strike)](../apps/zet_strike.md) | `zet near` |

### [ARKOD Layer (web)](../apps/arkod_web.md)

Web/Cloud/iOS; API: http. Main call: `curl -s 'https://arkod-layer.pages.dev/api/wfs?<same query string the page sends>' # proxies the state cadastral WFS as GeoJSON`

Before: Parameters of the proxy routes are not in the harvested docs; open the page and copy the request it makes.

- Croatian cadastre on a map (ARKOD Layer)
- look up a parcel number (ARKOD Layer)
- ARKOD parcels on iPhone (ARKOD Layer)
- land registry sheet for a parcel (ARKOD Layer)

### [Maha Commute](../apps/MAHA_COMMUTE.md)

Android/Termux; API: http 8082. Main call: `curl 'http://127.0.0.1:8084/board?city=rijeka&stop=1734&mins=90'`

Before: Termux app on the phone: 8082 day, 8087 night, 8084 all-in-one; get.sh --apps picks which.

- when is the next tram or bus near me (Maha Commute)
- night tram positions in Zagreb (Maha Commute)
- public transport board for Rijeka (Maha Commute)
- install the commute apps on the phone (Maha Commute)

### [Mantra ARKOD](../apps/mantra_arkod.md)

Android/Cloud; API: none

- look up a land parcel in Croatia (Mantra ARKOD)
- who owns this cadastral parcel (Mantra ARKOD)
- offline cadastre map for walking (Mantra ARKOD)
- find my parcels on a map (Mantra ARKOD)

### [Mantra Map Server](../apps/MANTRA_MAP_SERVER.md)

Android; API: http 8088. Main call: `curl -s http://127.0.0.1:8088/tiles/croatia/10/553/366.png -o tile.png`

Before: Serves offline map tiles from local files; /maps lists the regions available.

- serve offline maps as tiles (Mantra Map Server) - call: `curl -s 127.0.0.1:8088/maps`
- give my laptop or tablet the phone's offline map (Mantra Map Server)
- map tile server on Android (Mantra Map Server)

### [Mantra Maps](../apps/MANTRA_MAPS.md)

Android; API: none

- download the offline Croatia map (Mantra Maps)
- offline map file for Mantra Trail (Mantra Maps)
- mapsforge map of Croatia (Mantra Maps)

### [Mantra Trail](../apps/MANTRA_TRAIL.md)

Android; API: none

- offline hiking map on Android (Mantra Trail)
- record a hike as GPX (Mantra Trail)
- navigate in the mountains without signal (Mantra Trail)
- route on foot offline (Mantra Trail)

### [Spar Locator / DM Finder](../apps/spar_locator.md)

Android; API: none

- which SPAR is open now (Spar Locator / DM Finder)
- find an open supermarket in Croatia on a map (Spar Locator / DM Finder)
- DM store opening hours Croatia (Spar Locator / DM Finder)

### [Store & Pool Finder](../apps/SHOP_FINDER.md)

Termux/Linux/Web/Cloud; API: http 8900. Main call: `curl -s http://127.0.0.1:8900/shopfinder/health # only health is documented as a call; the finder is a map page`

Before: Server on 8900 behind Caddy; local serve.py on 8080; on the phone: mapool.

- nearest shop open now (Store & Pool Finder)
- Zagreb pool opening hours (Store & Pool Finder)
- find a Spar or dm near me (Store & Pool Finder)
- store and pool finder (Store & Pool Finder)

### [ZET Strike](../apps/zet_strike.md)

Android/Termux; API: http 8100. Main call: `zet near # the next ZET trams and buses at the nearest stop`

Before: Flask server on 8100 (zet map); every /api call needs the X-ZET header (local guard).

- what trams are running in Zagreb now (ZET Strike)
- next bus near me in Zagreb (ZET Strike)
- Zagreb public transport strike news (ZET Strike) - call: `zet news`
- ZET map (ZET Strike)

