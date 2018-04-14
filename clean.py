import os

"""
Builds individual chapters to pdf and deletes aux files
"""

MODULES = [
    "1-mechanics",
    "2-gravitational-fields",
    "3-deformation-of-solids",
    "4-energy-concepts",
    "5-electricity",
    "6-waves",
    "7-superposition",
    "8-atomic-and-nuclear-processes",
    "9-quantum-ideas",
    "10-rotational-mechanics",
    "11-oscillations",
    "12-electric-fields",
    "13-gravitation",
    "14-electromagnetism",
    "15-special-relativity",
    "16-molecular-kinetic-theory",
    "17-nuclear-physics",
    "18-the-quantum-atom",
    "19-interpreting-quantum-theory",
    "20-astronomy-and-cosmology",
    "A-equations"
    ]

MAIN_FILE_NAME = "revision-guide"

TEX_EXTS = [
    ".aux",".bbl",".bbg",".log",".out",".synctex.gz",".blg"
    ]

print("Do you want to clean pdfs?")
pdf_choice = input("(Y/N) >")
if pdf_choice == "Y": TEX_EXTS.append(".pdf")
else: print("Not cleaning pdfs")

print("Do you want to clean the main file?")
main_choice = input("(Y/N) >")
if main_choice == "Y": MODULES.append(MAIN_FILE_NAME)
else: print("Not cleaning pdfs")


for module in MODULES:

    print (module)

    for ext in TEX_EXTS:
        try:
            os.remove(module + ext)
        except:
            print("Cant delete " + module + ext)
