[Back to the index](../CAPABILITIES.md)

# Data, backups and misc

- download a big Google Drive folder reliably -> [Drive Downloader](../apps/DRIVE_DOWNLOADER.md) (macOS/Web; API: http 5055) - call: `curl -s -XPOST 127.0.0.1:5055/api/jobs -H 'Content-Type: application/json' -d '{"url":"https://drive.google.com/drive/folders/<id>"}' # creates a job; body field names are not in the docs`
- resume a broken Drive download -> [Drive Downloader](../apps/DRIVE_DOWNLOADER.md) (macOS/Web; API: http 5055)
- fetch a 4 GB video from Drive over a bad connection -> [Drive Downloader](../apps/DRIVE_DOWNLOADER.md) (macOS/Web; API: http 5055)
- download a whole Google Drive folder to this Mac -> [GDrive Downloader (Flask, macOS)](../apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (macOS/Web; API: http 5055) - call: `curl -s -XPOST 127.0.0.1:5055/api/jobs/1/start`
- resume a big Drive download after the connection dropped -> [GDrive Downloader (Flask, macOS)](../apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (macOS/Web; API: http 5055)
- check how big a Drive folder is -> [GDrive Downloader (Flask, macOS)](../apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (macOS/Web; API: http 5055)
- tell me when the Lenovo Legion tablet is in stock -> [Lenovo Hunter](../apps/LENOVO_HUNTER.md) (Android; API: none)
- compare prices of the Y700 across shops -> [Lenovo Hunter](../apps/LENOVO_HUNTER.md) (Android; API: none)
- watch a product's stock in many shops -> [Lenovo Hunter](../apps/LENOVO_HUNTER.md) (Android; API: none)
- open an online Photoshop-like editor full screen -> [Photopea Studio](../apps/marko-photoshop.md) (Web/Cloud; API: none)
- Photopea without the start screen -> [Photopea Studio](../apps/marko-photoshop.md) (Web/Cloud; API: none)
- markdown notes app on Android -> [TataTalk (Quillpad notes fork)](../apps/TataTalk.md) (Android; API: none)
- notes with task lists -> [TataTalk (Quillpad notes fork)](../apps/TataTalk.md) (Android; API: none)
- Quillpad -> [TataTalk (Quillpad notes fork)](../apps/TataTalk.md) (Android; API: none)
