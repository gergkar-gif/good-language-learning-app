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
    lesson_files = sorted(glob.glob(f"content/es-latam/lessons/b1/b1-{unit}-*.json"))
    print(f"=== {unit} ===")
    for lf in lesson_files:
        if "consolidation" in lf: continue
        d = json.load(open(lf, encoding='utf-8'))
        story_ref = ""
        for sec in d.get('sections', []):
            if sec.get('type') == 'story':
                story_ref = sec.get('ref')
        print(f"  {d.get('id')}: story = {story_ref}")
