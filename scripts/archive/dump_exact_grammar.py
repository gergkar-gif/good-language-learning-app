import json, glob, sys

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

for unit in units:
    for i in range(1, 6):
        num = f"{i:02d}"
        gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
        ex_files = glob.glob(f"content/es-latam/exercises/b1/b1-{unit}-{num}-ex.json")
        voc_files = glob.glob(f"content/es-latam/vocabulary/b1/b1-{unit}-{num}-voc.json")
        
        print(f"=== {unit}-{num} ===")
        if gr_files:
            gr = json.load(open(gr_files[0], encoding='utf-8'))
            print("TITLE:", gr.get('title'))
            for sec in gr.get('sections', []):
                if sec.get('type') == 'examples':
                    for item in sec.get('items', []):
                        print("  GR:", repr(item.get('spanish')))
        if voc_files:
            voc = json.load(open(voc_files[0], encoding='utf-8'))
            words = [w.get('lemma') or w.get('word') for w in voc.get('words', [])]
            print("  VOC:", words)
        if ex_files:
            ex_data = json.load(open(ex_files[0], encoding='utf-8'))
            for ex in ex_data.get('exercises', []):
                if ex.get('type') in ['multiple-choice', 'reading']:
                    print("  EX_Q:", repr(ex.get('question')))
                    print("  EX_A:", repr(ex.get('answer')))
                    print("  EX_OPTS:", ex.get('options'))
