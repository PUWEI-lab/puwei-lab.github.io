# 吳柏葳 PUWEI WU — Artist portfolio

原生 HTML、CSS、JavaScript 靜態網站，不需安裝套件或編譯。第一版待確認，尚未部署。

## 預覽

直接用瀏覽器開啟根目錄 `index.html`；或在儲存庫目錄執行：

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

在執行指令的電腦開啟 `http://127.0.0.1:8000`，按 Ctrl+C 停止。雲端工作區可使用平台支援的連接埠轉送，或下載檔案至本機預覽。

## 替換圖片與內容

- 文字在 `index.html`，樣式在 `assets/style.css`，導覽輔助程式在 `assets/site.js`。
- SVG 圖片僅為版面佔位，非藝術家作品。將真實圖片放入 `assets/`，例如 `assets/work-01.jpg`。建議壓縮 JPG 或 WebP、長邊約 1600–2400 像素，檔名使用小寫英數與連字號。
- 在 HTML 替換 `placeholder-wide.svg`、`placeholder-portrait.svg` 對應的 `src`，首頁、列表、詳情都要更新；同步修改 `alt`、真實 `width` 與 `height`。使用 `assets/...` 相對路徑並注意大小寫。
- 填入作品名稱、年份、媒材、尺寸、介紹、中英文簡介、展覽與駐村紀錄。未取得資料繼續標示「待補」，不填入虛構資訊。
- 新增作品需複製列表卡片及對應 `article`，讓 `href="#work-04"` 對應唯一 `id="work-04"`，同步修改標題 ID 與 `aria-labelledby`。詳情透過 CSS `:target` 顯示，不依賴 JavaScript。
- 聯絡欄目前不含假連結。收到資料後，Email 的 `dd` 改為 `<a href="mailto:實際信箱">實際信箱</a>`，Instagram 改為 `<a href="https://www.instagram.com/實際帳號/">@實際帳號</a>`。
- 正式發布前移除首頁草稿標示與作品區佔位說明，確認公開內容與圖片授權。

## 確認第一版後，發布到 GitHub Pages

1. 確認設計、補齊資料。本次不推送、不啟用 Pages。
2. 將確認後的檔案提交並推送到 GitHub `main` 分支。
3. 儲存庫 **Settings → Pages → Build and deployment**，Source 選 **Deploy from a branch**。
4. Branch 選 `main`，資料夾選 `/ (root)`，儲存。
5. 等待部署成功，使用 Settings → Pages 顯示的正式網址，檢查手機排版、作品詳情、圖片與聯絡連結。

此帳號網站預期網址為 `https://puwei-lab.github.io/`；以 GitHub Pages 顯示為準。啟用後推送到來源分支可能更新正式網站。
