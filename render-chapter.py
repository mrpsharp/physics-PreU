import os,subprocess
"""
Builds individual chapters to pdf and deletes aux files

FIXME: Currently references to equations are broken and will show up as a bold double question mark
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

TEX_EXTS = [
    ".aux",".bbl",".bbg",".log",".out",".synctex.gz",".blg"
    ]


for module in MODULES:

    print (module)

    #os.system('pdflatex.exe -synctex=1 -output-directory pdf -interaction=nonstopmode "' + module + '".tex')
    #os.system('pdflatex.exe -synctex=1 -interaction=nonstopmode "' + module + '".tex')
    subprocess.call(["pdflatex.exe","-synctex=1", "-interaction=nonstopmode", "-output-directory=pdf", '"' + module + '"' + ".tex"])
    #subprocess.call(["pdflatex.exe","-synctex=1", "-interaction=nonstopmode", '"' + module + '"' + ".tex"])
for module in MODULES:
    for ext in TEX_EXTS:
        try:
            os.remove("pdf/" + module + ext)
        except:
            print("Cant delete " + "pdf/" + module + ext)
