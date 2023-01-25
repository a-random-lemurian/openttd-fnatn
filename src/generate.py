VER = "1"
MIN_COMPAT = "1"

TOP = """
// Copyright (c) 2023 Lemuria

grf {
    grfid: "fntn";
    name: string(STR_GRF_NAME);
    desc: string(STR_GRF_DESCRIPTION);
    url: string(STR_GRF_URL);
    version: """+VER+""";
    min_compatible_version: """+MIN_COMPAT+""";
}

town_names(FNATA_MAIN) {{
"""

BOTTOM = """
}}

town_names {
    styles: string(STR_GAME_OPTIONS_TOWN_NAME);
    {
        town_names(FNATA_MAIN, 1)
    }
}
"""

NAMES_FILE = "names.txt"
OUT_FILE  = "fnatn.nml"

def make_nml_text_code(name):
    return "text(\""+name+"\",1),\n"

def main():
    names_list = open(NAMES_FILE, mode='r').read().split("\n")
    nml_calls = [make_nml_text_code(name.strip()) for name in names_list]
    with open(OUT_FILE, mode='w') as outfile:
        outfile.write(TOP+''.join(nml_calls)+BOTTOM)

if __name__ == '__main__':
    main()
