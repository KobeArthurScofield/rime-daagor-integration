# 专治上游灵机一动

print("Initializing")

import os
from datetime import date

print("Building functions and objects")

scriptver = "25.333"
upstreamdate = "2025-11-28"

old_path = "./download/dicts/"
new_path = "./"

# MAPPING LIST OF THE REVERTING
reverter = {
    "zi": "dnt.l.chars",
    "jichu": "dnt.l.words",
    "duoyin": "dnt.l.heteronym",
    "lianxiang": "dnt.l.continuous",
    "shici": "dnt.l.poetry",
    "dikuang": "dnt.l.geo_mine",
    "diming": "dnt.l.toponymy",
    "renming": "dnt.l.personal_name",
    "shuxue": "dnt.l.math",
    "wu-hua-sheng-yi-yao": "dnt.l.industry",
    "wuzhong": "dnt.l.biotaxonomy",
}

def Detect_EOL(rawdata):
    if b"\r\n" in rawdata:
        return "\r\n"
    else:
        return "\n"

def Search_And_Replace(decoded_line, newname, eol_mark, datefmt):
    name_updated = False
    version_updated = False

    for lnl, line in enumerate(decoded_line):
        if line.startswith("name: ") and not name_updated:
            print("The content of the name line is:\n" + line)
            if "#" in line:
                bc, comment = line.split("#", 1)
                comment = "#" + comment
            else:
                comment = ""

            replacement = "name: " + newname + "  " + comment
            print("The content of the replacement is:\n" + replacement)

            decoded_line[lnl] = f"{replacement}"
            print("Replace line number is " + str(lnl) + "\nThe replaced line is:\n" + decoded_line[lnl])

            name_updated = True
            continue

        if line.startswith("version: ") and not version_updated:
            print("The content of the version line is:\n" + line)
            if "#" in line:
                bc, comment = line.split("#", 1)
                comment = "#" + comment
            else:
                comment = ""

            replacement = "version: " + datefmt + "  " + comment
            print("The content of the replacement is:\n" + replacement)

            decoded_line[lnl] = f"{replacement}"
            print("Replace line number is " + str(lnl) + "\nThe replaced line is:\n" + decoded_line[lnl])

            version_updated = True
            continue

        if name_updated and version_updated:
            print("Name and version update completed")
            break

    decoded_line.append("")
    new_data = eol_mark.join(decoded_line)
    print("Combining completed")
    return new_data

def Data_Processing(raw_data, newname):
    eol_mark = Detect_EOL(raw_data)
    print("End of line mark has been detected")

    decode_pool = raw_data.decode("utf-8")
    print("Text extraction completed")

    line_pool = decode_pool.splitlines()
    print("Lines splitted")

    date_value = date.today().strftime("%Y-%m-%d")
    print("Date acquired. Value is " + date_value)

    new_data = Search_And_Replace(line_pool, newname, eol_mark, date_value)
    print("Lines of " + newname + " has been processed")

    return new_data.encode("utf-8")

print("Preparing main")

# Main section

print("Starting Execution")

print("")
print("Converter version: " + scriptver)
print("Use with upstream release since " + upstreamdate)
print("")

for oldname, newname in reverter.items():
    print("Old file name is " + oldname)
    print("New file name is " + newname)

    old_file_path = os.path.join(old_path, oldname + ".dict.yaml")
    print("Reading file " + old_file_path)

    with open(old_file_path, "rb") as rdr:
        raw_pool = rdr.read()
        print(old_file_path + " has been read")

    new_pool = Data_Processing(raw_pool, newname)
    print("Retrieve new data completed")

    new_file_path = os.path.join(new_path, newname + ".dict.yaml")
    print("The new file path is " + new_file_path)

    with open(new_file_path, "wb") as wdr:
        wdr.write(new_pool)
        print("New file " + new_file_path + " has been written")
    
    print("Converting " + oldname + " to " + newname + " completed.\n")

print("Procedure completed")
