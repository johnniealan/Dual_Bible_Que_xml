import xml.etree.ElementTree as ET

# --------------------------------------------------
# Files
# --------------------------------------------------

NIV_FILE = "NIV.xml"
TAMIL_FILE = "BSI.xml"
OUTPUT_FILE = "NIV_Tamil_Bilingual.xml"

# --------------------------------------------------
# Bible book names
# --------------------------------------------------

BOOK_NAMES = {
    "1": "Genesis", "2": "Exodus", "3": "Leviticus", "4": "Numbers",
    "5": "Deuteronomy", "6": "Joshua", "7": "Judges", "8": "Ruth",
    "9": "1 Samuel", "10": "2 Samuel", "11": "1 Kings", "12": "2 Kings",
    "13": "1 Chronicles", "14": "2 Chronicles", "15": "Ezra", "16": "Nehemiah",
    "17": "Esther", "18": "Job", "19": "Psalms", "20": "Proverbs",
    "21": "Ecclesiastes", "22": "Song of Solomon", "23": "Isaiah",
    "24": "Jeremiah", "25": "Lamentations", "26": "Ezekiel", "27": "Daniel",
    "28": "Hosea", "29": "Joel", "30": "Amos", "31": "Obadiah",
    "32": "Jonah", "33": "Micah", "34": "Nahum", "35": "Habakkuk",
    "36": "Zephaniah", "37": "Haggai", "38": "Zechariah", "39": "Malachi",
    "40": "Matthew", "41": "Mark", "42": "Luke", "43": "John",
    "44": "Acts", "45": "Romans", "46": "1 Corinthians", "47": "2 Corinthians",
    "48": "Galatians", "49": "Ephesians", "50": "Philippians", "51": "Colossians",
    "52": "1 Thessalonians", "53": "2 Thessalonians", "54": "1 Timothy",
    "55": "2 Timothy", "56": "Titus", "57": "Philemon", "58": "Hebrews",
    "59": "James", "60": "1 Peter", "61": "2 Peter", "62": "1 John",
    "63": "2 John", "64": "3 John", "65": "Jude", "66": "Revelation"
}

# --------------------------------------------------
# Load NIV
# --------------------------------------------------

niv_root = ET.parse(NIV_FILE).getroot()

english = {}

for testament in niv_root.findall("testament"):
    for book in testament.findall("book"):

        bnum = str(int(book.attrib.get("number", "0")))

        for chapter in book.findall("chapter"):
            cnum = chapter.attrib.get("number")

            for verse in chapter.findall("verse"):
                vnum = verse.attrib.get("number")

                english[(bnum, cnum, vnum)] = verse.text or ""

print("NIV verses loaded:", len(english))

# --------------------------------------------------
# Load Tamil
# --------------------------------------------------

tamil_tree = ET.parse(TAMIL_FILE)
tamil_root = tamil_tree.getroot()

# --------------------------------------------------
# FIX: Presenter metadata
# --------------------------------------------------

tamil_root.attrib["biblename"] = "Tamil (BSI) + English (NIV)"

info = tamil_root.find("INFORMATION")
if info is not None:
    title = info.find("title")
    if title is not None:
        title.text = "Tamil (BSI) + English (NIV)"

# --------------------------------------------------
# Merge process
# --------------------------------------------------

for book in tamil_root.findall("BIBLEBOOK"):

    # normalize book number
    bnum_raw = book.attrib.get("bnumber", "")

    try:
        bnum = str(int(bnum_raw))
    except:
        bnum = bnum_raw.strip()

    tamil_name = book.attrib.get("bname", "")

    # set correct names
    book.attrib["tamil_name"] = tamil_name
    book.attrib["bname"] = BOOK_NAMES.get(bnum, f"Book {bnum}")

    print(f"{bnum}: {book.attrib['bname']} ({tamil_name})")

    for chapter in book.findall("CHAPTER"):

        cnum = chapter.attrib.get("cnumber")

        for verse in chapter.findall("VERS"):

            vnum = verse.attrib.get("vnumber")

            tamil_text = verse.text or ""
            english_text = english.get((bnum, cnum, vnum), "")

            if not english_text:
                print(f"Missing NIV: {bnum}:{cnum}:{vnum}")

            verse.text = english_text + "\n" + tamil_text

# --------------------------------------------------
# Save output
# --------------------------------------------------

tamil_tree.write(
    OUTPUT_FILE,
    encoding="utf-8",
    xml_declaration=True
)

print("\nDONE ->", OUTPUT_FILE)
