# QRCode to ISBN by Nivyan

> The following script converts a QR Code to it's ISBN alternative, and then uses the [Google Books API](https://developers.google.com/books) to fetch the meta data. 

The script currently outputs the following: 

- **Title:** `volume_info["volumeInfo"]["title"])`
- **Date of Publication:** `volume_info["volumeInfo"]["publishedDate"]`
- **Summary:** `(volume_info["searchInfo"]["textSnippet"]`
- **Author(s):** `.join(authors)`
- **Public Domain Access:** `volume_info["accessInfo"]["publicDomain"]`
- **Page Count:** `volume_info["volumeInfo"]["pageCount"]`
- **Language:** `volume_info["volumeInfo"]["language"]`
- **Publisher:** `volume_info["volumeInfo"]["publisher"]`

### Screenshot(s)

![image](https://user-images.githubusercontent.com/79858886/158030703-029c53fb-41fa-4f43-a8b1-e59459a3962a.png)
