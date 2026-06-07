# 📖 NIV + Tamil Bible Merger (Multi-Language Parallel Bible Tool)

This project merges an **English Bible (NIV format)** with a **Tamil Bible (BSI)** into a single bilingual XML file compatible with Bible Presenter and similar Bible applications.

It creates a **parallel Bible view** where each verse contains both English and Tamil text in a single structured format.

---

## ✨ Features

- Merges **English (NIV)** + **Tamil Bible** verse-by-verse
- Keeps original XML structure intact
- Adds proper English book names (Genesis, Exodus, etc.)
- Preserves Tamil book names using `tamil_name`
- Fixes book numbering issues (e.g., `01 → 1`)
- Produces clean bilingual Bible XML output
- Updates metadata so Bible Presenter shows correct title
- Fully supports **multi-language Bible merging**
- Automatically aligns verses using `(book, chapter, verse)` keys
- Safe handling of missing verses
- Works with standard Bible XML structures

---

## 🌍 Multi-Language Support

This script can merge **any two Bible translations** as long as they follow a compatible structure.

Supported combinations:
- English + Tamil
- English + Hindi
- English + Spanish
- Tamil + Malayalam
- Any structured Bible XML pair

Requirements:
- Same book order (or mappable numbers)
- Same chapter structure
- Same verse numbering system
- Standard hierarchical XML format

---

## 📂 Input Files

Place both files in the same folder:

- `NIV.xml` → English Bible
- `TamilBSI.xml` → Tamil Bible

---

## 🚀 How to Run

### 1. Install Python
Python 3.x required.

### 2. Run script

```bash
python Dual_bible_cue_xml.py
```

---

## 📤 Output

```
NIV_Tamil_Bilingual.xml
```

Contains:
- English verse text
- Tamil verse text
- Proper structure
- Updated metadata

---

## 🖥️ Bible Presenter Output

After importing:

> Tamil (BSI) + English (NIV)

---

## 🧱 XML STRUCTURE

### 📘 English (NIV)

```xml
<bible>
  <testament name="Old">
    <book number="1">
      <chapter number="1">
        <verse number="1">In the beginning God created the heavens and the earth.</verse>
      </chapter>
    </book>
  </testament>
</bible>
```

---

### 📗 Tamil Bible

```xml
<XMLBIBLE biblename="Tamil (BSI)">
  <BIBLEBOOK bnumber="1" bname="ஆதியாகமம்">
    <CHAPTER cnumber="1">
      <VERS vnumber="1">ஆதியிலே தேவன் வானத்தையும் பூமியையும் சிருஷ்டித்தார்.</VERS>
    </CHAPTER>
  </BIBLEBOOK>
</XMLBIBLE>
```

---

## 🔄 VERSE MATCHING LOGIC

Uses:

```
(Book Number, Chapter Number, Verse Number)
```

Example:

```
(1,1,1) → Genesis 1:1
(1,1,2) → Genesis 1:2
```

## 📜 License

Free for:
- Personal study
- Church use
- Ministry use
- Educational use

---

## 💡 Summary

This tool:
- Merges NIV + Tamil Bible
- Produces bilingual XML
- Keeps structure intact
- Works for multiple languages
- Compatible with Bible Presenter
