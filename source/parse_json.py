import json

with open("ocr.json", "r") as f:
    j = json.loads(f.read())
text = ""

for a in j["responses"]:
    for b in a["fullTextAnnotation"]["pages"]:
        for c in b["blocks"]:
            text += "\n"
            for d in c["paragraphs"]:
                for e in d["words"]:
                    text += " "
                    for f in e["symbols"]:
                        text += f["text"]

print(text)

