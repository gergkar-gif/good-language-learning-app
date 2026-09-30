import json, glob, os, sys

block_units = {
    2: ['razaclasepoder', 'independencia', 'nuevasrepublicas', 'caudillismo', 'nacionnacionalismo', 'liberalismomodernizacion'],
    3: ['economiasexportacion', 'cambiosocial', 'revolucion', 'revolucionmexicana', 'nacionalismo', 'grandepresion'],
    4: ['populismo', 'industrializacion', 'revolucioncubana', 'guerrafria', 'eeuu', 'gobiernosmilitares'],
    5: ['represionpolitica', 'centroamerica', 'conosur', 'crisisdeuda', 'neoliberalismo', 'democratizacion'],
    6: ['movimientosindigenas', 'integracionregional', 'finalguerrafria', 'latamnoventa', 'legadosigloveinte', 'americalatinadosmil'],
}

block_num = int(sys.argv[1]) if len(sys.argv) > 1 else 2
units = block_units[block_num]

for unit in units:
    print(f"==================================================")
    print(f" UNIT: {unit} ")
    print(f"==================================================")
    for i in range(1, 6):
        num = f"{i:02d}"
        gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
        ex_file = f"content/es-latam/exercises/b1/b1-{unit}-{num}-ex.json"
        voc_file = f"content/es-latam/vocabulary/b1/b1-{unit}-{num}-voc.json"
        st_files = glob.glob(f"content/es-latam/stories/world/b1/b1-{unit}-{num}-*.json")
        
        print(f"\n--- {unit} {num} ---")
        if st_files:
            st = json.load(open(st_files[0], encoding='utf-8'))
            print("STORY ID:", st.get('id'), "| TITLE:", st.get('title'))
        
        if gr_files:
            gr = json.load(open(gr_files[0], encoding='utf-8'))
            print("GRAMMAR:", gr.get('id'), "|", gr.get('title'))
            for sec in gr.get('sections', []):
                if sec.get('type') == 'examples':
                    for ex in sec.get('items', []):
                        esp = ex.get('spanish', '')
                        eng = ex.get('english', '')
                        print(f"  GR: {esp}")
        
        if os.path.exists(voc_file):
            voc = json.load(open(voc_file, encoding='utf-8'))
            words = [w.get('lemma') or w.get('word') for w in voc.get('words', [])]
            print("VOCAB:", ", ".join(words))
            
        if os.path.exists(ex_file):
            ex_data = json.load(open(ex_file, encoding='utf-8'))
            for ex in ex_data.get('exercises', []):
                t = ex.get('type')
                q = ex.get('question')
                ans = ex.get('answer')
                opts = ex.get('options', [])
                if q:
                    print(f"  EX [{t}]: {q} -> {ans}")
