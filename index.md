# Audio Comparison

This page displays audio files organized by number and type for easy comparison.

# 聆聽測試說明 / Listening Test Instructions

感謝您參與我們的合成器 Preset 轉換評估研究。請務必先閱讀此頁內容，再進行測驗，以確保結果的公平與有效性。接下來你將3組音檔，整體測驗時常大約1分鐘。<br>

Thank you for participating in our study on synthesizer preset conversion. Please read this page carefully before starting the test to ensure fairness and validity. You will be presented with four sets of audio files, with each set containing results from five models. The overall test duration is approximately five minutes.<br>

---

## 測試主題 / Test Theme

在此測試中，我們希望了解模型是否能正確地將一段 Original Audio（原始演奏內容）轉換成具有 Reference Audio（參考音檔）的音色 (Timbre) 與 ADSR (Attack, Decay, Sustain, Release)。<br>

In this test, we evaluate whether models can take the Original Audio (note content) and convert it into the Timbre and ADSR envelope of the Reference Audio.<br>

**每個生成結果都應該：**<br>
- **保留 Original Audio 的演奏內容（彈什麼音）**<br>
- **轉換出 Reference Audio 的 Timbre 與 ADSR**<br>

**Each generated result should:**<br>
- **Preserve the musical content of the Original Audio (what notes are played)**<br>
- **Transform into the Timbre and ADSR of the Reference Audio**<br>

---

## 評估指標 / Evaluation Metrics

### 音色相似度 (Timbre Similarity)
- **定義**：聲音的「質感」，例如明亮或暗沉、厚實或輕薄、金屬感或柔和感<br>
- **重點**：聆聽聲音本身的「材料感」與頻譜特性，不考慮長短或變化<br>
- **評分**：越接近參考音色，分數越高<br>

- **Definition**: The "texture" of sound, such as bright vs dark, thick vs thin, metallic vs soft<br>
- **Focus**: Listen to the "material feel" and spectral characteristics of the sound itself, regardless of duration or variation<br>
- **Scoring**: Higher scores for closer match to reference timbre<br>

### ADSR Envelope 相似度 (ADSR Similarity)
- **定義**：聲音隨時間的「形狀」，包含起音 (Attack)、衰減 (Decay)、延音 (Sustain)、收尾 (Release)<br>
- **重點**：專注於聲音的動態變化，例如一開始是否快速衝出、尾音是否緩慢消退<br>
- **評分**：時間變化模式越接近參考，分數越高<br>

- **Definition**: The "shape" of sound over time, including Attack, Decay, Sustain, and Release<br>
- **Focus**: Focus on dynamic changes, such as how quickly the sound starts and how slowly it fades<br>
- **Scoring**: Higher scores for closer match to reference envelope pattern<br>

### 內容相似度 (Content Similarity)
- **定義**：評估生成音檔是否保留了原始音檔的演奏內容，例如音符、節奏、旋律等<br>
- **重點**：專注於內容的保留程度，是否彈奏的音、內容與原始音檔相似<br>
- **評分**：越接近原始內容，分數越高<br>

- **Definition**: Evaluates whether the generated audio preserves the musical content of the original audio, such as notes, rhythm, and melody<br>
- **Focus**: Focus on content preservation - whether the played notes and content match the original audio<br>
- **Scoring**: Higher scores for closer match to original content<br>

---

## 測試流程 / Test Procedure

1. Listen to Original Audio（決定演奏內容）<br>
2. Listen to Reference Audio（提供 Timbre 與 ADSR 資訊）<br>
3. Listen to Generated Audio, and rate from 1 to 5：<br>
- **1**：完全不相似 / Not similar at all<br>
- **2**：稍微相似 / Slightly similar<br>
- **3**：中等相似 / Moderately similar<br>
- **4**：接近 / Close<br>
- **5**：非常相似 / Very similar<br>

---

## 指引 / Guidelines

- 使用耳機，在安靜環境中進行，以避免干擾 / Use headphones in a quiet environment to avoid interference<br>
- 測試無時間限制，可反覆播放任意樣本 / No time limit, you can replay any sample as many times as needed<br>
- 請於一次會話中完成，若中斷將遺失進度 / Please complete in one session, progress will be lost if interrupted<br>
- 使用 Chrome 或 Safari 瀏覽器，確保網路穩定 / Use Chrome or Safari browser and ensure stable internet connection<br>

---

## 開始測試 / Start Test

接下來請仔細比較各指標的相似度。當您準備好，請點擊「開始測試」。<br>

Please rate the samples based on similarity for each metric. When you are ready, click Start Test.<br>

祝您測試愉快！/ Enjoy the test!


## Audio Files Table

<table class="table table-sm text-center" style="vertical-align: middle;">
  <colgroup>
      <col style="width: 120px;">
      <col style="width: 200px;">
      <col style="width: 200px;">
      <col style="width: 200px;">
    </colgroup>
  <thead>
    <tr>
      <th style="text-align:center;">Number</th>
      <th style="text-align:center;">Original</th>
      <th style="text-align:center;">Reference</th>
      <th style="text-align:center;">Reconstructed (Ablated)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Audio 1</td>
      <td><audio src="Audio/11_orig.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/11_ref.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/11_recon_abl.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>Audio 2</td>
      <td><audio src="Audio/15_orig.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/15_ref.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/15_recon_abl.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>Audio 3</td>
      <td><audio src="Audio/16_orig.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/16_ref.wav" controls style="width: 200px"></audio></td>
      <td><audio src="Audio/16_recon_abl.wav" controls style="width: 200px"></audio></td>
    </tr>
  </tbody>
</table>

## 請回答給我
| Sample | TimbreMOS (1-5) | ADSRMOS (1-5) | ContentMOS (1-5) |
| --- | --- | --- | --- |
| Audio 1 | | | |
| Audio 2 | | | |
| Audio 3 | | | |