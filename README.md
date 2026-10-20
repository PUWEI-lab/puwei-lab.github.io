# 吳柏葳 PUWEI WU

原生 HTML、CSS、JavaScript 的藝術家網站。這是供確認的第二版，未合併至 main、未啟用 GitHub Pages。

## 版型預覽畫面

以下是實際網站在瀏覽器渲染的截圖，並非已發布的網站入口：

- 首頁：[桌機](preview/home-desktop.png)／[手機](preview/home-mobile.png)
- 繪畫：[桌機](preview/paintings-desktop.png)／[手機](preview/paintings-mobile.png)
- 裝置／現地創作：[桌機](preview/installations-desktop.png)／[手機](preview/installations-mobile.png)
- 展覽：[桌機](preview/exhibitions-desktop.png)／[手機](preview/exhibitions-mobile.png)
- 《茫茫》詳情：[桌機](preview/bong-bong-desktop.png)／[手機](preview/bong-bong-mobile.png)

## 本版架構

- 首頁：姓名與創作代表照；手機直幅、電腦橫幅，保留完整構圖。
- 繪畫：獨立列表與作品詳情，以完整作品正面照為主要圖片，不裁切作品。
- 裝置／現地創作：以展覽現場、空間與觀看情境呈現；《茫茫》在此類。
- 展覽：各展覽分開的現場圖庫，目前依已提供資料列出《倒風內山：文明發酵術》、《怪獸繁榮》、《遺物址》與2023年《看他一臉扁平》。這是本版分類，待藝術家確認。
- About、CV、Contact：已核對的簡介、學歷、經歷與聯絡資料。
- 《藍幕劇組》使用同一計畫圖集，六個具名組件的資料在計畫頁內列出，不逐張配對照片。其15張照片署名為劉耀鈞。
- 《青青的睡去》保留整體計畫與三個組件。《顯視錯誤：404》保留共同創作署名與整體材料清單。
- 作者排除的作品與經歷不列入。售價、內部核對筆記、私人資料與原始文件不放入網站。
- 未提供連結的影片暫不顯示播放器，不使用無效的播放按鈕。

## 預覽與檔案位置

直接以瀏覽器開啟根目錄 `index.html` 即可；所有頁面都是靜態 HTML，不需要安裝、編譯或執行 Python。也可在自己的電腦、儲存庫目錄啟動靜態伺服器：

```sh
python3 -m http.server 8000
```

然後在同一台電腦的瀏覽器開啟 `http://localhost:8000`。雲端環境的本機埠不是對外預覽網址。

- `index.html`：首頁。
- `paintings.html`、`installations.html`：兩個作品入口。
- `works/`：單件作品與計畫頁；組件位於母計畫頁內。
- `exhibitions.html`、`exhibitions/`：展覽索引與各展覽圖庫。
- `about.html`、`cv.html`、`contact.html`：藝術家資料。
- `assets/style.css`：樣式與響應式排版。
- `assets/site.js`：鍵盤可操作的圖片檢視器；停用JavaScript仍可使用導覽、閱讀作品及開啟圖片。
- `assets/images/`：供網頁使用的WebP圖檔。原檔留存在內容整理區，網站版本只做尺寸、色彩描述檔轉換與壓縮，不改動畫面或調整彩度、亮度。
- `assets/catalogue.json`：本版公開作品資料索引，供對照；頁面直接寫入HTML，執行時不依賴讀取此檔案。

## 如何修改

在對應的HTML頁面直接修改文字、媒材、尺寸或連結。`assets/catalogue.json`是對照資料，單獨修改它不會自動改變HTML頁面；兩邊應同步更新。

替換圖片時可保留原檔名，或同步修改HTML中的 `src`、`srcset`、`href`、`width`、`height` 及 `alt`。首頁 `<picture>` 的 `<source media="(max-width: 700px)">` 使用直幅，後面的 `<img>` 使用橫幅。作品圖片使用 `object-fit: contain`，勿改為 `cover`，以免裁切完整作品。

網站內部連結使用相對路徑，根目錄圖片以 `assets/` 開頭，子資料夾頁面以 `../assets/` 開頭，部署至GitHub Pages不需重寫路徑。

補影片時在對應展覽頁加入已確認的影片網址與嵌入碼。《看他一臉扁平》、《怪獸繁榮》的個展紀錄影片與《怪獸早已出現》的錄像作品應分開標示。

## 確認後才發布

目前修改僅用於 `website-preview` 分支，不啟用Pages、不合併。待藝術家確認版型、分類、內容與選圖後，再合併至 `main`；屆時才到GitHub儲存庫 Settings → Pages 選擇由 `main` 的根目錄部署。本次不執行發布設定。
