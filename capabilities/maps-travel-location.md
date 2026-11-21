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

- Croatian cadastre on a map -> [ARKOD Layer (web)](../apps/arkod_web.md) (Web/Cloud/iOS; API: http) - call: `curl -s 'https://arkod-layer.pages.dev/api/wfs?<same query string the page sends>' # proxies the state cadastral WFS as GeoJSON`
- look up a parcel number -> [ARKOD Layer (web)](../apps/arkod_web.md) (Web/Cloud/iOS; API: http)
- ARKOD parcels on iPhone -> [ARKOD Layer (web)](../apps/arkod_web.md) (Web/Cloud/iOS; API: http)
- land registry sheet for a parcel -> [ARKOD Layer (web)](../apps/arkod_web.md) (Web/Cloud/iOS; API: http)
- when is the next tram or bus near me -> [Maha Commute](../apps/MAHA_COMMUTE.md) (Android/Termux; API: http 8082) - call: `curl 'http://127.0.0.1:8084/board?city=rijeka&stop=1734&mins=90'`
- night tram positions in Zagreb -> [Maha Commute](../apps/MAHA_COMMUTE.md) (Android/Termux; API: http 8082)
- public transport board for Rijeka -> [Maha Commute](../apps/MAHA_COMMUTE.md) (Android/Termux; API: http 8082)
- install the commute apps on the phone -> [Maha Commute](../apps/MAHA_COMMUTE.md) (Android/Termux; API: http 8082)
- look up a land parcel in Croatia -> [Mantra ARKOD](../apps/mantra_arkod.md) (Android/Cloud; API: none)
- who owns this cadastral parcel -> [Mantra ARKOD](../apps/mantra_arkod.md) (Android/Cloud; API: none)
- offline cadastre map for walking -> [Mantra ARKOD](../apps/mantra_arkod.md) (Android/Cloud; API: none)
- find my parcels on a map -> [Mantra ARKOD](../apps/mantra_arkod.md) (Android/Cloud; API: none)
- serve offline maps as tiles -> [Mantra Map Server](../apps/MANTRA_MAP_SERVER.md) (Android; API: http 8088) - call: `curl -s http://127.0.0.1:8088/tiles/croatia/10/553/366.png -o tile.png`
- give my laptop or tablet the phone's offline map -> [Mantra Map Server](../apps/MANTRA_MAP_SERVER.md) (Android; API: http 8088)
- map tile server on Android -> [Mantra Map Server](../apps/MANTRA_MAP_SERVER.md) (Android; API: http 8088)
- download the offline Croatia map -> [Mantra Maps](../apps/MANTRA_MAPS.md) (Android; API: none)
- offline map file for Mantra Trail -> [Mantra Maps](../apps/MANTRA_MAPS.md) (Android; API: none)
- mapsforge map of Croatia -> [Mantra Maps](../apps/MANTRA_MAPS.md) (Android; API: none)
- offline hiking map on Android -> [Mantra Trail](../apps/MANTRA_TRAIL.md) (Android; API: none)
- record a hike as GPX -> [Mantra Trail](../apps/MANTRA_TRAIL.md) (Android; API: none)
- navigate in the mountains without signal -> [Mantra Trail](../apps/MANTRA_TRAIL.md) (Android; API: none)
- route on foot offline -> [Mantra Trail](../apps/MANTRA_TRAIL.md) (Android; API: none)
- which SPAR is open now -> [Spar Locator / DM Finder](../apps/spar_locator.md) (Android; API: none)
- find an open supermarket in Croatia on a map -> [Spar Locator / DM Finder](../apps/spar_locator.md) (Android; API: none)
- DM store opening hours Croatia -> [Spar Locator / DM Finder](../apps/spar_locator.md) (Android; API: none)
- nearest shop open now -> [Store & Pool Finder](../apps/SHOP_FINDER.md) (Termux/Linux/Web/Cloud; API: http 8900) - call: `curl -s http://127.0.0.1:8900/shopfinder/health # only health is documented as a call; the finder is a map page`
- Zagreb pool opening hours -> [Store & Pool Finder](../apps/SHOP_FINDER.md) (Termux/Linux/Web/Cloud; API: http 8900)
- find a Spar or dm near me -> [Store & Pool Finder](../apps/SHOP_FINDER.md) (Termux/Linux/Web/Cloud; API: http 8900)
- store and pool finder -> [Store & Pool Finder](../apps/SHOP_FINDER.md) (Termux/Linux/Web/Cloud; API: http 8900)
- what trams are running in Zagreb now -> [ZET Strike](../apps/zet_strike.md) (Android/Termux; API: http 8100) - call: `zet near # the next ZET trams and buses at the nearest stop`
- next bus near me in Zagreb -> [ZET Strike](../apps/zet_strike.md) (Android/Termux; API: http 8100)
- Zagreb public transport strike news -> [ZET Strike](../apps/zet_strike.md) (Android/Termux; API: http 8100)
- ZET map -> [ZET Strike](../apps/zet_strike.md) (Android/Termux; API: http 8100)
