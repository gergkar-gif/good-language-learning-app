import json
import glob
import os
import sys

BLOCK_UNITS = {
    1: ['precolombina', 'civilizaciones', 'llegadaeuropeos', 'conquista', 'sociedadcolonial', 'economiacolonial'],
    2: ['razaclasepoder', 'independencia', 'nuevasrepublicas', 'caudillismo', 'nacionnacionalismo', 'liberalismomodernizacion'],
    3: ['economiasexportacion', 'cambiosocial', 'revolucion', 'revolucionmexicana', 'nacionalismo', 'grandepresion'],
    4: ['populismo', 'industrializacion', 'revolucioncubana', 'guerrafria', 'eeuu', 'gobiernosmilitares'],
    5: ['represionpolitica', 'centroamerica', 'conosur', 'crisisdeuda', 'neoliberalismo', 'democratizacion'],
    6: ['movimientosindigenas', 'integracionregional', 'finalguerrafria', 'latamnoventa', 'legadosigloveinte', 'americalatinadosmil'],
}

def get_block_reqs(block_num):
    units = BLOCK_UNITS[block_num]
    reqs = {}
    for unit in units:
        for i in range(1, 6):
            num = f"{i:02d}"
            key = f"{unit}-{num}"
            gr_files = glob.glob(f"content/es-latam/grammar/b1/b1-{unit}-{num}-*.json")
            st_files = glob.glob(f"content/es-latam/stories/world/b1/b1-{unit}-{num}-*.json")
            voc_files = glob.glob(f"content/es-latam/vocabulary/b1/b1-{unit}-{num}-*.json")
            ex_files = glob.glob(f"content/es-latam/exercises/b1/b1-{unit}-{num}-*.json")
            
            grammar_sentences = []
            for gf in sorted(gr_files):
                gr = json.load(open(gf, encoding='utf-8'))
                for sec in gr.get('sections', []):
                    if sec.get('type') == 'examples':
                        for it in sec.get('items', []):
                            esp = it.get('spanish', '').strip()
                            if esp and esp not in grammar_sentences:
                                grammar_sentences.append(esp)
                                
            vocab_words = []
            for vf in sorted(voc_files):
                voc = json.load(open(vf, encoding='utf-8'))
                for w in voc.get('words', []):
                    vocab_words.append(w.get('lemma') or w.get('word'))
                    
            st_file = os.path.basename(st_files[0]) if st_files else f"b1-{unit}-{num}.json"
            st_id = f"story.b1.{unit}.{num}"
            st_title = ""
            if st_files:
                st_data = json.load(open(st_files[0], encoding='utf-8'))
                st_title = st_data.get('title', '')
                st_id = st_data.get('id', st_id)
                
            reqs[key] = {
                'st_file': st_file,
                'st_id': st_id,
                'st_title': st_title,
                'grammar_sentences': grammar_sentences,
                'vocab_words': vocab_words
            }
    return reqs

if __name__ == '__main__':
    block_num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    reqs = get_block_reqs(block_num)
    out_path = f"scripts/block{block_num}_all_reqs.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(reqs, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(reqs)} lesson requirements for Block {block_num} to {out_path}")
