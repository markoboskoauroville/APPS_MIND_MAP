[Back to the index](../CAPABILITIES.md)

# Data, backups and misc

### [Drive Downloader](../apps/DRIVE_DOWNLOADER.md)

macOS/Web; API: http 5055. Main call: `curl -s -XPOST 127.0.0.1:5055/api/jobs -H 'Content-Type: application/json' -d '{"url":"https://drive.google.com/drive/folders/<id>"}' # creates a job; body field names are not in the docs`

Before: Flask app on 5055; connect the Google account first with POST /api/connect.

- download a big Google Drive folder reliably (Drive Downloader)
- resume a broken Drive download (Drive Downloader)
- fetch a 4 GB video from Drive over a bad connection (Drive Downloader)

### [GDrive Downloader (Flask, macOS)](../apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md)

macOS/Web; API: http 5055. Main call: `curl -s -XPOST 127.0.0.1:5055/api/jobs/1/start`

Before: Flask app on 5055; sign in and connect first (POST /api/signin, POST /api/connect); same API as DRIVE_DOWNLOADER.

- download a whole Google Drive folder to this Mac (GDrive Downloader)
- resume a big Drive download after the connection dropped (GDrive Downloader)
- check how big a Drive folder is (GDrive Downloader)

### [Lenovo Hunter](../apps/LENOVO_HUNTER.md)

Android; API: none

- tell me when the Lenovo Legion tablet is in stock (Lenovo Hunter)
- compare prices of the Y700 across shops (Lenovo Hunter)
- watch a product's stock in many shops (Lenovo Hunter)

### [Photopea Studio](../apps/marko-photoshop.md)

Web/Cloud; API: none

- open an online Photoshop-like editor full screen (Photopea Studio)
- Photopea without the start screen (Photopea Studio)

### [TataTalk (Quillpad notes fork)](../apps/TataTalk.md)

Android; API: none

- markdown notes app on Android (TataTalk)
- notes with task lists (TataTalk)
- Quillpad (TataTalk)

