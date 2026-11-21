# Maha Commute

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Termux umbrella installer for the Zagreb (and Rijeka) transit family: day.commute, night.commute and all.commute, one command to install, one word to open.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_COMMUTE](https://github.com/markoboskoauroville/MAHA_COMMUTE) |
| Also called | maha.commute, maha-commute, day.commute, night.commute, all.commute, Zagreb transit |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android, Termux |
| Language | Shell (embedded Python/HTML) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Install three transit apps from one verified file (get.sh, checked four ways before running)
- Show day commute corridors (day.commute)
- Show the four Zagreb night trams and a dashboard per stop (night.commute)
- Show every station around you for Zagreb and Rijeka in colour (all.commute)
- Serve local HTTP endpoints for status, stations, stops, departures board and vehicles
- Self-update from GitHub and keep timetables and keys across updates

## Ask for it when

- when is the next tram or bus near me
- night tram positions in Zagreb
- public transport board for Rijeka
- install the commute apps on the phone

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8082 day, 8087 night, 8084 all

Actions:

- `GET /status?city=rijeka`
- `GET /stations.json?city=rijeka`
- `GET /stops?city=&lat=&lon=&r=`
- `GET /board?city=&stop=&mins=`
- `GET /vehicles?city=&lat=&lon=&r=`
- `CLI: maha.commute`
- `CLI: maha.commute-update`
- `get.sh --apps 1|2|3|12|13|23`

**Before you call:** Termux app on the phone: 8082 day, 8087 night, 8084 all-in-one; get.sh --apps picks which.

Example:

```
curl 'http://127.0.0.1:8084/board?city=rijeka&stop=1734&mins=90'
```

More calls:

- stops around a point: `curl -s 'http://127.0.0.1:8084/stops?city=rijeka&lat=45.33&lon=14.44&r=500'`
- vehicles nearby: `curl -s 'http://127.0.0.1:8084/vehicles?city=rijeka&lat=45.33&lon=14.44&r=500'`
- status: `curl -s 'http://127.0.0.1:8084/status?city=rijeka'`

Evidence: TAKEOVER.md section 0 (all_commute_server.py endpoints); README.md table of ports

## Inputs / Outputs

Inputs:

- Zagreb and Rijeka public transport feeds
- PDF timetables
- optional Google Maps key

Outputs:

- local web dashboards
- departure boards

## Works with

- Uses: [Keyring](KEYRING_TERMUX.md)

## Code worth reusing

- `30-maha_commute_v30.sh`: self-contained installer carrying all three apps and a verified-download pattern (get.sh)

## Notes

Repo holds many numbered versioned installer scripts (v10 to v30) plus field-test logs; use the newest. Ports as stated in README; the Google key is optional. Unmerged work lives on named branches in the harvest notes.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MAHA_COMMUTE/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MAHA_COMMUTE/blob/HEAD/TAKEOVER.md)
