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

TEX_EXTS = [
    ".aux",".bbl",".bbg",".log",".out",".synctex.gz"
    ]

module_text = ""
with open("standalone2.tex") as f:
    module_text = f.read()

print(module_text)


for module in MODULES:
    print(module)
    new_text = module_text.replace("_MODULE_",module)

    with open("mod_" + module + ".tex", "w") as f:
        f.write(new_text)

    os.system('pdflatex.exe -synctex=1 -output-directory pdf -interaction=nonstopmode "mod_' + module + '".tex')

    for ext in TEX_EXTS:
        try:
            os.remove("pdf/mod_" + module + ext)
        except:
            print("Cant delete " + "pdf/mod_" + module + ext)

    
