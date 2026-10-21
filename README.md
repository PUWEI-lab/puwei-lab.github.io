# 吳柏葳 PUWEI WU

原生 HTML、CSS、JavaScript 的藝術家網站。目前為 `website-preview` 的三層導覽預覽版，未合併至 main、未啟用 GitHub Pages。

## 版型預覽畫面

以下為實際網站的瀏覽器截圖，並非正式上線網址：

- 首頁：[桌機](preview/home-desktop.png)／[手機](preview/home-mobile.png)
- 左側系列選單與作品入口：[桌機](preview/series-index-desktop.png)／[手機](preview/series-index-mobile.png)
- 《青青的睡去》第三級與分件照片：[桌機](preview/herb-series-desktop.png)／[手機](preview/herb-series-mobile.png)／[手機展開選單](preview/navigation-mobile-open.png)
- 《藍幕劇組》兩級入口及共用圖集：[桌機](preview/chroma-set-desktop.png)／[手機](preview/chroma-set-mobile.png)
- 《怪獸繁榮》逐件展開：[桌機](preview/kaiju-boom-desktop.png)／[手機](preview/kaiju-boom-mobile.png)
- 李神原作與拷貝：[桌機完整頁](preview/li-shen-desktop.png)
- 展覽列表，一列一檔：[桌機](preview/exhibitions-desktop.png)／[手機](preview/exhibitions-mobile.png)
- 《直至綻放》照片與展出連結：[桌機](preview/until-it-blooms-desktop.png)／[手機](preview/until-it-blooms-mobile.png)
- `not / A SOLDIER` 展覽照片及本展作品：[桌機](preview/not-a-soldier-desktop.png)／[手機](preview/not-a-soldier-mobile.png)

## 本版架構

- 左側僅放文字。第一級依序為CV、About、展覽、作品、Contact；圖片放在右側主內容。
- 「展覽」第二級列出已有現場照的展覽；「作品」第二級列出既有系列及獨立作品名稱。點文字開啟主內容，點右側＋／−展開或收合下層。
- 展覽第二級以「個展」「聯展」作兩個非互動分類標題，各標題下只列年份與正式展名；各組內按時間倒序，不逐筆重複冠上展覽類型，也不增加第三級。右側展覽總覽及首頁展覽列表使用相同分組。
- 作品入口、系列內作品與右側索引使用同一排序，依各系列最新作品創作時間倒序；有作者確認月份者使用該月份。同年僅知年份者置於已知月份之後，彼此保留既有順序，不推定月份。《顯視錯誤：404》為2023.07、李神「拷貝」為2023.03，標示創作年月；李神原作仍保留2023。展覽依已知開展日期倒序，只有年份者按年份排列、置於同年有完整日期的項目之後並保留彼此原順序，不補造月日。
- 《看他一臉扁平》入口依作者E3已確認的2023–2025新舊作品範圍，以2025排序；原2023創作及個展資料保留，不以單純重展日期改寫作品年份。
- 多件作品系列的第三級只列作品名稱，點選後定位到右側該件作品的大圖與資訊；原生展開選單與連結不依賴JavaScript。
- 作品依既有系列與獨立計畫分組，主導覽不再以繪畫／裝置區分。
- 《怪獸繁榮》、《大決闘》各有系列頁，完整圖片與作品資料由上而下逐件展開。
- 《片廠佈景》與《電塔山景》均在《怪獸繁榮》系列下；《片廠佈景》不另設第二級獨立入口。
- 李神系列名稱使用《李神到厚櫃間的________》，第三級列原作及「拷貝」，兩件保留各自名稱與資料。
- 《走著瞧！》、《茫茫》、《看他一臉扁平》等沒有共同系列名稱的現地創作，各有獨立入口，不另外建立一個「扁平幽靈」作品系列。
- 《青青的睡去》提供失眠、採藥、青草巷三個第三級入口；右側各段使用對應的3、6、5張照片及各自資料。《藍幕劇組》不設第三級，右側保留六個組件資料和共用圖集，不逐張配對，15張照片署名為劉耀鈞。
- 首頁使用姓名與創作代表照，手機直幅、電腦橫幅。繪畫仍使用完整照，現地創作使用現場照，保留構圖。
- 展覽列表一列一檔，以大圖往下瀏覽；每檔展覽有自己的照片圖庫。展覽與作品系列分開記錄。
- 已確認參展對應的作品頁及系列內單件項目，加入「展出紀錄」連結；展覽頁也可由「本展作品」返回作品頁。只依作者確認及照片中可辨識的作品建立對應，不把同系列全數算進同一展覽。
- 作者最新補充的馬祖藝術島、《The World, Not According to Art》、北藝當代創作獎、城西生活節、基隆潮藝術、Signal Z、水谷《歡迎光臨介力屋》及《小事一樁，大戰一場》等，已依提供資料建立對應。未提供的展期不推測；作品年份、展期、駐村日期分開。
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
