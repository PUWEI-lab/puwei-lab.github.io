# 吳柏葳 PUWEI WU

原生 HTML、CSS、JavaScript 的藝術家網站。此為 `website-preview` 的第三版，未合併至 main、未啟用 GitHub Pages。

## 版型預覽畫面

以下為實際網站的瀏覽器截圖，並非正式上線網址：

- 首頁：[桌機](preview/home-desktop.png)／[手機](preview/home-mobile.png)
- 左側系列選單與作品入口：[桌機](preview/series-index-desktop.png)／[手機](preview/series-index-mobile.png)
- 《怪獸繁榮》逐件展開：[桌機](preview/kaiju-boom-desktop.png)／[手機](preview/kaiju-boom-mobile.png)
- 李神原作與拷貝：[桌機完整頁](preview/li-shen-desktop.png)
- 展覽列表，一列一檔：[桌機](preview/exhibitions-desktop.png)／[手機](preview/exhibitions-mobile.png)
- 《直至綻放》照片與展出連結：[桌機](preview/until-it-blooms-desktop.png)／[手機](preview/until-it-blooms-mobile.png)
- `not / A SOLDIER` 展覽照片及本展作品：[桌機](preview/not-a-soldier-desktop.png)／[手機](preview/not-a-soldier-mobile.png)

## 本版架構

- 左側「作品」旁的＋可展開所有系列與獨立計畫名稱。
- 作品依既有系列與獨立計畫分組，主導覽不再以繪畫／裝置區分。
- 《怪獸繁榮》、《大決闘》各有系列頁，完整圖片與作品資料由上而下逐件展開。
- 《李神到厚櫃間的________》與「拷貝」放在同一入口，原作與拷貝仍保留各自名稱及資料。
- 《走著瞧！》、《茫茫》、《看他一臉扁平》等沒有共同系列名稱的現地創作，各有獨立入口，不另外建立一個「扁平幽靈」作品系列。
- 《青青的睡去》保留整體計畫與三個具名組件；《藍幕劇組》保留同一計畫圖集與六個組件資料，不逐張配對，15張照片署名為劉耀鈞。
- 首頁使用姓名與創作代表照，手機直幅、電腦橫幅。繪畫仍使用完整照，現地創作使用現場照，保留構圖。
- 展覽列表一列一檔，以大圖往下瀏覽；每檔展覽有自己的照片圖庫。展覽與作品系列分開記錄。
- 已確認參展對應的作品頁及系列內單件項目，加入「展出紀錄」連結；展覽頁也可由「本展作品」返回作品頁。只依作者確認及照片中可辨識的作品建立對應，不把同系列全數算進同一展覽。
- 作者最新補充的馬祖藝術島、黃金町巴扎、北藝當代創作獎、城西生活節、基隆潮藝術、Signal Z、水谷《歡迎光臨介力屋》及《小事一樁，大戰一場》等，已依提供資料建立對應。未提供的展期不推測；作品年份、展期、駐村日期分開。
- 《直至綻放／Until It Blooms》依作者新決定恢復列入，獨立對應2025年黃金町 `not / A SOLDIER` 聯展。已補入作者提供的6張作品與展場紀錄，包含全景、直幅、局部及展覽海報。
- 未取得連結的兩支個展紀錄影片與《怪獸早已出現》錄像作品暫不顯示播放器。
- About、CV、Contact保留已核對資料。作者排除的其他作品與經歷不列入；售價、內部筆記和原始文件不放入網站。

## 預覽及檔案

所有頁面都是靜態HTML，不需要安裝或編譯。可直接在自己的電腦以瀏覽器開啟 `index.html`，或在儲存庫目錄啟動靜態伺服器：

```sh
python3 -m http.server 8000
```

再用同一台電腦開啟 `http://localhost:8000`；雲端工作區的本機埠不是可分享的預覽網址。

- `index.html`：首頁。
- `works.html`：系列與獨立計畫入口；`series/`：多件作品逐件展開的系列頁。
- `works/`：個別作品／計畫及細節圖；組件在母計畫頁中列出。
- `exhibitions.html`、`exhibitions/`：單欄展覽索引與各展覽圖庫。
- `about.html`、`cv.html`、`contact.html`：藝術家資料。
- `assets/style.css`：樣式與響應式排版；`assets/site.js`：可用鍵盤操作的圖片檢視器。
- `assets/images/`：WebP網頁版。來源原檔保留在內容整理區；僅縮放、色彩描述檔轉換及壓縮，不重畫、不調整彩度或亮度。
- `assets/catalogue.json`、`assets/series.json`、`assets/exhibitions.json`：公開資料對照。頁面內容已直接寫入HTML，不依賴執行時讀取JSON。
- 舊的 `paintings.html` 與 `installations.html` 保留為相同的系列索引，以相容先前連結。

## 如何修改

直接修改對應HTML，並同步更新公開JSON對照資料；單獨修改JSON不會自動重建HTML。

替換圖片可沿用檔名，或同步修改HTML的 `src`、`srcset`、`href`、`width`、`height` 與 `alt`。首頁 `<picture>` 中手機的 `<source media="(max-width: 700px)">` 使用直幅，其後 `<img>` 使用橫幅。圖片使用 `object-fit: contain`，保留完整作品，勿改為裁切。

內部連結使用相對路徑，根目錄的圖檔以 `assets/` 開頭，子頁以 `../assets/` 開頭。新增系列需同步調整各頁左右兩套導覽（桌機／手機）、系列頁及作品索引。

補影片時將已確認的連結放入對應展覽頁，《看他一臉扁平》、《怪獸繁榮》的個展紀錄與《怪獸早已出現》的錄像作品分開標示。

## 確認後才發布

目前只更新 `website-preview`，不合併、不啟用Pages。待作者確認版型、分類、展覽對應及選圖後，才合併至 `main`，並於GitHub Settings → Pages選擇從main根目錄部署。本次不執行發布設定。
