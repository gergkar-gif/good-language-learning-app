import json, glob, os, sys

block_units = {
    1: ['precolombina', 'civilizaciones', 'llegadaeuropeos', 'conquista', 'sociedadcolonial', 'economiacolonial'],
    2: ['razaclasepoder', 'independencia', 'nuevasrepublicas', 'caudillismo', 'nacionnacionalismo', 'liberalismomodernizacion'],
    3: ['economiasexportacion', 'cambiosocial', 'revolucion', 'revolucionmexicana', 'nacionalismo', 'grandepresion'],
    4: ['populismo', 'industrializacion', 'revolucioncubana', 'guerrafria', 'eeuu', 'gobiernosmilitares'],
    5: ['represionpolitica', 'centroamerica', 'conosur', 'crisisdeuda', 'neoliberalismo', 'democratizacion'],
    6: ['movimientosindigenas', 'integracionregional', 'finalguerrafria', 'latamnoventa', 'legadosigloveinte', 'americalatinadosmil'],
}

block_num = int(sys.argv[1]) if len(sys.argv) > 1 else 2
units = block_units[block_num]

all_ok = True
for unit in units:
    for i in range(1, 6):
        num = f"{i:02d}"
        gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
        st_files = glob.glob(f"content/es-latam/stories/world/b1/b1-{unit}-{num}-*.json")
        if not gr_files or not st_files:
            continue
        st = json.load(open(st_files[0], encoding='utf-8'))
        st_text = ' '.join(p['text'] if isinstance(p, dict) else str(p) for p in st.get('paragraphs', []))
        
        for gpath in gr_files:
            gr = json.load(open(gpath, encoding='utf-8'))
            for sec in gr.get('sections', []):
                if sec.get('type') == 'examples':
                    for ex in sec.get('items', []):
                        esp = ex.get('spanish', '').strip()
                        if esp and esp not in st_text:
                            print(f"MISSING in {unit}-{num} ({os.path.basename(gpath)}): '{esp}'")
                            all_ok = False

if all_ok:
    print(f"Block {block_num}: ALL grammar examples are perfectly embedded verbatim!")
