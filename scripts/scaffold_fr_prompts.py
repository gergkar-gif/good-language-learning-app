#!/usr/bin/env python3
"""
Scaffold comprehensive French prompts, scenarios, communicative challenges,
translation sentence pairs, and skill registry entries for Parlour.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {path.relative_to(ROOT)} ({len(json.dumps(data))} bytes)")

def build_writing_prompts():
    return {
        "language": "fr",
        "prompts": [
            {
                "id": "fr-b2-debate",
                "cefrLevel": "B2",
                "taskType": "written_argument",
                "title": "Débat : Villes sans voitures",
                "prompt": "Dans votre ville, la municipalité débat de l'interdiction progressive des voitures individuelles dans le centre historique. Écrivez un article pour le journal local dans lequel vous présentez les arguments pour et contre cette mesure, et exposez votre propre point de vue de manière argumentée et nuancée.",
                "minWords": 180,
                "targetWords": 250,
                "maxWords": 350,
                "targetSkills": [
                    {"id": "expression_opinion", "description": "Nuancer son point de vue avec clarté au niveau B2"},
                    {"id": "argumentation", "description": "Développer une argumentation logique avec thèse et antithèse"},
                    {"id": "connecteurs_logiques", "description": "Emploi de connecteurs logiques (d'une part, néanmoins, bien que, en revanche)"},
                    {"id": "subjonctif_concession", "description": "Emploi du subjonctif dans les structures concessives"}
                ]
            },
            {
                "id": "fr-b1-recit-voyage",
                "cefrLevel": "B1",
                "taskType": "travel_recount",
                "title": "Un voyage mémorable",
                "prompt": "Racontez une expérience de voyage marquante dans un blog de voyage. Décrivez où vous êtes allé, les péripéties rencontrées, ce qui vous a surpris et pourquoi vous recommandez (ou non) cette destination.",
                "minWords": 120,
                "targetWords": 160,
                "maxWords": 220,
                "targetSkills": [
                    {"id": "passe_compose_imparfait", "description": "Alternance correcte entre passé composé et imparfait"},
                    {"id": "chronologie", "description": "Marqueurs temporels (d'abord, soudain, ensuite, finalement)"}
                ]
            },
            {
                "id": "fr-a2-lettre-reclamation",
                "cefrLevel": "A2",
                "taskType": "formal_complaint",
                "title": "Réclamation après un séjour",
                "prompt": "Vous avez séjourné dans un hôtel le week-end dernier et plusieurs services n'étaient pas conformes (bruit, chambre non nettoyée, petit-déjeuner manquant). Écrivez un e-mail à la direction de l'hôtel pour expliquer les problèmes et demander un dédommagement.",
                "minWords": 70,
                "targetWords": 90,
                "maxWords": 130
            },
            {
                "id": "fr-a1-w01",
                "cefrLevel": "A1",
                "taskType": "a_message_about_your_daily_routine",
                "title": "Un message sur votre quotidien",
                "situation": "You have a new French-speaking friend who wants to know what you usually do during the week.",
                "task": "Write a short message to your friend.",
                "points": [
                    "say what time you get up",
                    "say what you do during the day",
                    "say what you do in the evening",
                    "say what time you usually go to bed"
                ],
                "prompt": "Situation: You have a new French-speaking friend who wants to know what you usually do during the week.\n\nTask: Write a short message to your friend. Include: say what time you get up; say what you do during the day; say what you do in the evening; say what time you usually go to bed.\n\nWrite approximately 40-50 words.",
                "minWords": 40,
                "targetWords": 45,
                "maxWords": 60
            },
            {
                "id": "fr-a1-w02",
                "cefrLevel": "A1",
                "taskType": "an_invitation",
                "title": "Une invitation",
                "situation": "You are organizing a birthday party and want to invite a French colleague.",
                "task": "Write a short invitation message.",
                "points": [
                    "give the date and time",
                    "give the location or address",
                    "mention what to bring",
                    "ask for confirmation"
                ],
                "prompt": "Situation: You are organizing a birthday party and want to invite a French colleague.\n\nTask: Write a short invitation message. Include date, time, address, and ask for confirmation.\n\nWrite approximately 35-50 words.",
                "minWords": 35,
                "targetWords": 45,
                "maxWords": 60
            }
        ]
    }

def build_speaking_prompts():
    return {
        "language": "fr",
        "prompts": [
            {
                "id": "fr-a1-s01",
                "cefrLevel": "A1",
                "taskType": "personal_information",
                "title": "Présentation personnelle",
                "situation": "You are meeting a French-speaking person for the first time.",
                "task": "Answer questions about yourself.",
                "points": [
                    "your name and where you are from",
                    "where you live",
                    "your work or studies",
                    "the languages you speak",
                    "your hobbies"
                ],
                "prompt": "Situation: You are meeting a French-speaking person for the first time.\n\nTask: Introduce yourself in French. Include your name, origin, city, occupation, languages, and hobbies.\n\nSpeak for approximately 1-2 minutes.",
                "minSeconds": 60,
                "targetSeconds": 90,
                "maxSeconds": 150
            },
            {
                "id": "fr-a1-s02",
                "cefrLevel": "A1",
                "taskType": "describe_your_family",
                "title": "Décrire votre famille",
                "situation": "You are showing a French friend photos of your family and friends.",
                "task": "Describe the people in the photograph.",
                "points": [
                    "who the people are",
                    "their names and occupations",
                    "what they are like",
                    "one activity you enjoy together"
                ],
                "prompt": "Situation: You are showing a French friend photos of your family.\n\nTask: Describe the people, their relationship to you, their traits, and what you do together.\n\nSpeak for approximately 1-2 minutes.",
                "minSeconds": 60,
                "targetSeconds": 90,
                "maxSeconds": 150
            },
            {
                "id": "fr-a2-s01",
                "cefrLevel": "A2",
                "taskType": "last_weekend",
                "title": "Le week-end dernier",
                "situation": "A French colleague asks you about your weekend activities.",
                "task": "Tell what you did last weekend.",
                "points": [
                    "where you went and with whom",
                    "what the weather was like",
                    "two or three activities you completed",
                    "how you felt about the weekend"
                ],
                "prompt": "Situation: A colleague asks about your weekend.\n\nTask: Recount your weekend in the past tense (passé composé). Describe where you went, what you did, and how it was.\n\nSpeak for approximately 1-2 minutes.",
                "minSeconds": 60,
                "targetSeconds": 90,
                "maxSeconds": 150
            },
            {
                "id": "fr-b1-s01",
                "cefrLevel": "B1",
                "taskType": "work_life_balance",
                "title": "L'équilibre vie professionnelle et personnelle",
                "situation": "You participate in an online French conversation club on lifestyle.",
                "task": "Express your thoughts on telecommuting and work-life balance.",
                "points": [
                    "the advantages of remote work",
                    "the challenges or drawbacks",
                    "your personal preferences",
                    "advice for maintaining balance"
                ],
                "prompt": "Task: Discuss remote work and work-life balance. Share advantages, disadvantages, and your personal experience.\n\nSpeak for approximately 2 minutes.",
                "minSeconds": 90,
                "targetSeconds": 120,
                "maxSeconds": 180
            }
        ]
    }

def build_writing_exchanges():
    return {
        "language": "fr",
        "scenarios": [
            {
                "id": "fr-a1-wx01-marche",
                "cefrLevel": "A1",
                "title": "Au marché",
                "titleEn": "At the Market",
                "situation": "Votre colocataire Julien est au marché du quartier et vous envoie un SMS pour savoir ce qu'il faut acheter pour le dîner.",
                "situationEn": "Your flatmate Julien is at the local market and texts you to ask what to buy for dinner.",
                "roleplay": {
                    "interlocutorRole": "Julien (Colocataire)",
                    "interlocutorRoleEn": "Julien (Flatmate)",
                    "learnerRole": "Vous",
                    "learnerRoleEn": "You"
                },
                "targetCompetency": "I can exchange short text messages about everyday food shopping",
                "targetSkills": ["shopping", "food_and_drink", "requests"],
                "unitIds": ["unit.a1.01"],
                "requiredLemmas": ["salut", "pain", "fromage", "pomme", "s'il te plaît", "merci"],
                "turns": [
                    {
                        "turnIndex": 1,
                        "interlocutorPrompt": "Salut ! Je suis au marché des Batignolles. De quoi avons-nous besoin pour ce soir ?",
                        "interlocutorTranslation": "Hi! I am at the Batignolles market. What do we need for tonight?",
                        "learnerCue": "Salue Julien et demande-lui d'acheter du pain, du fromage et des pommes.",
                        "learnerCueEn": "Greet Julien and ask him to buy bread, cheese, and apples.",
                        "vocabularyHints": [
                            "salut Julien — hi Julien",
                            "achète du pain — buy some bread",
                            "du fromage et des pommes — cheese and apples",
                            "s'il te plaît — please"
                        ],
                        "validationCriteria": {
                            "minWords": 3,
                            "targetKeywords": ["salut", "pain", "fromage", "pommes", "pomme", "achète", "prends", "plaît"]
                        }
                    },
                    {
                        "turnIndex": 2,
                        "interlocutorPrompt": "Parfait, je prends une baguette et du comté. Veux-tu aussi une bouteille de vin ou du jus de fruits ?",
                        "interlocutorTranslation": "Great, I'll take a baguette and some comté. Do you also want a bottle of wine or fruit juice?",
                        "learnerCue": "Dis que tu préfères une bouteille de vin rouge et remercie-le.",
                        "learnerCueEn": "Say that you prefer a bottle of red wine and thank him.",
                        "vocabularyHints": [
                            "je préfère — I prefer",
                            "une bouteille de vin rouge — a bottle of red wine",
                            "merci beaucoup — thank you very much"
                        ],
                        "validationCriteria": {
                            "minWords": 3,
                            "targetKeywords": ["vin", "rouge", "préfère", "veux", "bouteille", "merci"]
                        }
                    }
                ]
            },
            {
                "id": "fr-a2-wx01-rdv",
                "cefrLevel": "A2",
                "title": "Prendre un rendez-vous",
                "titleEn": "Making an Appointment",
                "situation": "Vous écrivez à la secrétaire du cabinet médical pour décaler un rendez-vous.",
                "situationEn": "You write to the medical office secretary to reschedule an appointment.",
                "roleplay": {
                    "interlocutorRole": "Secrétaire médicale",
                    "interlocutorRoleEn": "Medical secretary",
                    "learnerRole": "Patient",
                    "learnerRoleEn": "Patient"
                },
                "targetCompetency": "I can write a message to arrange or change an appointment",
                "targetSkills": ["appointments", "politeness", "time_dates"],
                "unitIds": ["unit.a2.01"],
                "requiredLemmas": ["bonjour", "rendez-vous", "possible", "mardi", "mercredi", "merci"],
                "turns": [
                    {
                        "turnIndex": 1,
                        "interlocutorPrompt": "Cabinet médical Saint-Louis, bonjour. Comment puis-je vous aider ?",
                        "interlocutorTranslation": "Saint-Louis Medical Practice, hello. How can I help you?",
                        "learnerCue": "Dis que tu as un rendez-vous mardi et que tu souhaites le décaler à mercredi si possible.",
                        "learnerCueEn": "Say you have an appointment on Tuesday and would like to move it to Wednesday if possible.",
                        "vocabularyHints": [
                            "j'ai un rendez-vous — I have an appointment",
                            "décaler à mercredi — move to Wednesday",
                            "est-ce possible — is it possible"
                        ],
                        "validationCriteria": {
                            "minWords": 4,
                            "targetKeywords": ["rendez-vous", "mardi", "mercredi", "décaler", "changer", "possible"]
                        }
                    }
                ]
            }
        ]
    }

def build_conversation_scenarios():
    return {
        "language": "fr",
        "scenarios": [
            {
                "id": "fr-a1-sc01-cafe",
                "cefrLevel": "A1",
                "title": "Au Café parisien",
                "titleEn": "At the Parisian Café",
                "situation": "Vous êtes en terrasse dans un café à Paris et vous souhaitez commander une boisson, un en-cas et demander l'addition.",
                "situationEn": "You are on the terrace of a café in Paris and want to order a drink, a snack, and ask for the bill.",
                "roleplay": {
                    "interlocutorRole": "Serveur",
                    "interlocutorRoleEn": "Waiter",
                    "learnerRole": "Client",
                    "learnerRoleEn": "Customer",
                    "interlocutorVoice": "fr-FR"
                },
                "targetCompetency": "I can order food and drink in a French café and pay the bill",
                "targetSkills": ["ordering_food", "social_interaction", "numbers_and_prices"],
                "unitIds": ["unit.a1.01"],
                "requiredLemmas": ["bonjour", "café", "croissant", "eau", "addition", "s'il vous plaît", "merci"],
                "turns": [
                    {
                        "turnIndex": 1,
                        "interlocutorPrompt": "Bonjour madame, monsieur. Que puis-je vous servir ?",
                        "interlocutorTranslation": "Good morning. What can I get you?",
                        "learnerCue": "Salue poliment et commande un café crème (ou un thé) et un croissant.",
                        "learnerCueEn": "Greet politely and order a café crème (or tea) and a croissant.",
                        "vocabularyHints": [
                            "bonjour — hello",
                            "je voudrais un café — I would like a coffee",
                            "un croissant — a croissant",
                            "s'il vous plaît — please"
                        ],
                        "validationCriteria": {
                            "minWords": 3,
                            "targetKeywords": ["bonjour", "café", "thé", "croissant", "voudrais", "prends", "plaît"]
                        }
                    },
                    {
                        "turnIndex": 2,
                        "interlocutorPrompt": "Très bien, un café crème et un croissant. Désirez-vous également une carafe d'eau ?",
                        "interlocutorTranslation": "Very well, a coffee with milk and a croissant. Would you also like a jug of water?",
                        "learnerCue": "Accepte l'eau avec plaisir et remercie le serveur.",
                        "learnerCueEn": "Accept the water with pleasure and thank the waiter.",
                        "vocabularyHints": [
                            "oui, avec plaisir — yes, with pleasure",
                            "une carafe d'eau — a jug of water",
                            "merci — thank you"
                        ],
                        "validationCriteria": {
                            "minWords": 2,
                            "targetKeywords": ["oui", "eau", "carafe", "plaisir", "merci"]
                        }
                    },
                    {
                        "turnIndex": 3,
                        "interlocutorPrompt": "Voilà pour vous. Tout s'est bien passé ? Vous désirez autre chose ?",
                        "interlocutorTranslation": "Here you are. Was everything fine? Would you like anything else?",
                        "learnerCue": "Dis que c'était très bon et demande l'addition.",
                        "learnerCueEn": "Say that it was very good and ask for the bill.",
                        "vocabularyHints": [
                            "c'était très bon — it was very good",
                            "l'addition, s'il vous plaît — the bill, please"
                        ],
                        "validationCriteria": {
                            "minWords": 3,
                            "targetKeywords": ["addition", "très bon", "bon", "plaît", "note", "payer"]
                        }
                    }
                ]
            },
            {
                "id": "fr-a1-sc02-boulangerie",
                "cefrLevel": "A1",
                "title": "À la Boulangerie",
                "titleEn": "At the Bakery",
                "situation": "Vous entrez dans une boulangerie pour acheter du pain frais et des viennoiseries.",
                "situationEn": "You enter a bakery to buy fresh bread and pastries.",
                "roleplay": {
                    "interlocutorRole": "Boulangère",
                    "interlocutorRoleEn": "Baker",
                    "learnerRole": "Client",
                    "learnerRoleEn": "Customer",
                    "interlocutorVoice": "fr-FR"
                },
                "targetCompetency": "I can buy bread and pastries at a French bakery",
                "targetSkills": ["shopping", "food_and_drink"],
                "unitIds": ["unit.a1.01"],
                "requiredLemmas": ["bonjour", "baguette", "pain", "chocolat", "s'il vous plaît", "merci"],
                "turns": [
                    {
                        "turnIndex": 1,
                        "interlocutorPrompt": "Bonjour ! Qu'est-ce qu'il vous faudra aujourd'hui ?",
                        "interlocutorTranslation": "Hello! What can I get you today?",
                        "learnerCue": "Demande une baguette tradition bien cuite et deux pains au chocolat.",
                        "learnerCueEn": "Ask for a well-baked traditional baguette and two chocolate croissants.",
                        "vocabularyHints": [
                            "une baguette tradition — a traditional baguette",
                            "deux pains au chocolat — two chocolate croissants",
                            "s'il vous plaît — please"
                        ],
                        "validationCriteria": {
                            "minWords": 3,
                            "targetKeywords": ["baguette", "tradition", "pain", "chocolat", "deux", "plaît"]
                        }
                    }
                ]
            }
        ]
    }

def build_challenges():
    return {
        "version": "1.0",
        "language": "fr",
        "challenges": {
            "a1-01": {
                "tier": "tier1",
                "level": "A1",
                "title": "Défi communicatif : Les salutations",
                "scenario": "Vous rencontrez un collègue francophone lors d'une conférence à Paris.",
                "prompt": "Saluez poliment, dites votre nom et votre pays d'origine.",
                "cues": [
                    "Salutation (Bonjour / Enchanté)",
                    "Prénom (Je m'appelle... / Je suis...)",
                    "Origine (Je viens de... / Je suis...)"
                ],
                "target": "Bonjour, je m'appelle Sophie et je viens du Canada.",
                "english": "Hello, my name is Sophie and I come from Canada.",
                "canDo": "I can greet someone and introduce myself."
            },
            "a1-restaurant": {
                "tier": "tier1",
                "level": "A1",
                "title": "Défi communicatif : Commander au bistro",
                "scenario": "Vous êtes dans un bistrot à Lyon.",
                "prompt": "Commandez poliment un plat du jour et une carafe d'eau.",
                "cues": [
                    "Demander le plat (Je voudrais le plat du jour, s'il vous plaît)",
                    "Demander l'eau (Et une carafe d'eau)"
                ],
                "target": "Je voudrais le plat du jour et une carafe d'eau, s'il vous plaît.",
                "english": "I would like the daily special and a jug of water, please.",
                "canDo": "I can order simple meals and drinks."
            },
            "a2-directions": {
                "tier": "tier2",
                "level": "A2",
                "title": "Défi communicatif : Demander son chemin",
                "scenario": "Vous cherchez la station de métro la plus proche dans le centre de Paris.",
                "prompt": "Arrêtez un passant avec politesse, demandez où est le métro et si c'est loin à pied.",
                "cues": [
                    "Formule de politesse (Pardon monsieur / Excusez-moi madame)",
                    "Direction (Où se trouve la station de métro ?)",
                    "Distance (Est-ce que c'est loin à pied ?)"
                ],
                "target": "Excusez-moi madame, où se trouve le métro ? Est-ce que c'est loin à pied ?",
                "english": "Excuse me, where is the metro? Is it far on foot?",
                "canDo": "I can ask for and follow simple directions in town."
            }
        }
    }

def build_translation_index():
    # A curated, verified collection of French sentence pairs spanning A1 to B2
    pairs = [
        # A1 Greetings & Basics
        ("Bonjour, comment allez-vous ?", "Hello, how are you?", "A1", "Greetings & Introductions"),
        ("Je m'appelle Pierre et je suis français.", "My name is Pierre and I am French.", "A1", "Greetings & Introductions"),
        ("Enchanté de faire votre connaissance.", "Pleased to meet you.", "A1", "Greetings & Introductions"),
        ("Je viens de Paris, mais j'habite à Lyon.", "I come from Paris, but I live in Lyon.", "A1", "Greetings & Introductions"),
        ("Quel est votre numéro de téléphone ?", "What is your phone number?", "A1", "Greetings & Introductions"),
        
        # A1 Café & Dining
        ("Un café et un croissant, s'il vous plaît.", "A coffee and a croissant, please.", "A1", "At the Café"),
        ("Combien coûte ce gâteau ?", "How much does this cake cost?", "A1", "At the Café"),
        ("L'addition, s'il vous plaît.", "The bill, please.", "A1", "At the Café"),
        ("Avez-vous une table pour deux personnes ?", "Do you have a table for two?", "A1", "At the Café"),
        ("Je prends une salade verte et de l'eau.", "I'll take a green salad and some water.", "A1", "At the Café"),
        
        # A1 Daily Routine & Home
        ("Je me réveille à sept heures tous les matins.", "I wake up at seven every morning.", "A1", "Daily Routine"),
        ("Il prend son petit-déjeuner dans la cuisine.", "He has his breakfast in the kitchen.", "A1", "Daily Routine"),
        ("Nous partons au travail en métro.", "We leave for work by metro.", "A1", "Daily Routine"),
        ("Elle se couche généralement vers onze heures.", "She usually goes to bed around eleven.", "A1", "Daily Routine"),
        ("Il y a trois pièces dans mon appartement.", "There are three rooms in my apartment.", "A1", "Home"),
        
        # A1 Family & Friends
        ("J'ai un frère aîné et deux sœurs cadettes.", "I have an older brother and two younger sisters.", "A1", "Family"),
        ("Mon père est ingénieur et ma mère est médecin.", "My father is an engineer and my mother is a doctor.", "A1", "Family"),
        ("Ce sont mes meilleurs amis.", "These are my best friends.", "A1", "Family"),
        
        # A2 Directions & City
        ("Où se trouve la gare ferroviaire ?", "Where is the railway station?", "A2", "Directions"),
        ("Tournez à droite après le carrefour.", "Turn right after the crossroads.", "A2", "Directions"),
        ("Continuez tout droit jusqu'au feu rouge.", "Go straight ahead until the traffic light.", "A2", "Directions"),
        ("La pharmacie est juste à côté de la banque.", "The pharmacy is right next to the bank.", "A2", "Directions"),
        ("Est-ce que c'est loin d'ici ?", "Is it far from here?", "A2", "Directions"),
        
        # A2 Past tense (Passé composé & Imparfait)
        ("Hier soir, j'ai mangé dans un très bon restaurant.", "Yesterday evening, I ate in a very good restaurant.", "A2", "Past Events"),
        ("Elle est arrivée à la gare avec dix minutes de retard.", "She arrived at the station ten minutes late.", "A2", "Past Events"),
        ("Quand j'étais enfant, nous habitions à la campagne.", "When I was a child, we lived in the countryside.", "A2", "Past Events"),
        ("Il pleuvait beaucoup quand nous sommes sortis.", "It was raining heavily when we went out.", "A2", "Past Events"),
        ("Nous avons visité le musée du Louvre samedi dernier.", "We visited the Louvre museum last Saturday.", "A2", "Past Events"),
        
        # A2 Object Pronouns
        ("Je le vois tous les jours au bureau.", "I see him every day at the office.", "A2", "Pronouns"),
        ("Elle lui a donné les clés de la maison.", "She gave him the house keys.", "A2", "Pronouns"),
        ("Tu leur as téléphoné ce matin ?", "Did you phone them this morning?", "A2", "Pronouns"),
        ("Ne me dérange pas pendant que je travaille.", "Don't disturb me while I am working.", "A2", "Pronouns"),
        ("Je vais lui poser la question.", "I am going to ask him the question.", "A2", "Pronouns"),
        
        # B1 Work, Travel & Plans
        ("Si j'ai le temps demain, je passerai te voir.", "If I have time tomorrow, I will come by to see you.", "B1", "Work & Study"),
        ("Il cherche un nouvel emploi depuis trois mois.", "He has been looking for a new job for three months.", "B1", "Work & Study"),
        ("Nous devrions réserver les billets de train à l'avance.", "We should book the train tickets in advance.", "B1", "Travel"),
        ("Bien qu'il soit fatigué, il continue de travailler.", "Although he is tired, he keeps working.", "B1", "Complex Structures"),
        ("Je ne pense pas que ce soit la meilleure solution.", "I don't think that is the best solution.", "B1", "Subjunctive"),
        ("Il faut que vous fassiez attention aux détails.", "You must pay attention to the details.", "B1", "Subjunctive"),
        
        # B2 Nuance, Opinion & Argumentation
        ("Il est primordial de concilier croissance économique et préservation de l'environnement.", "It is crucial to balance economic growth and environmental preservation.", "B2", "Debate & Society"),
        ("D'un côté, cette mesure favorise l'emploi, mais de l'autre, elle fragilise les acquis sociaux.", "On one hand, this measure boosts employment, but on the other, it weakens social benefits.", "B2", "Debate & Society"),
        ("Quoi qu'il en soit, nous devons prendre des mesures immédiates.", "Be that as it may, we must take immediate action.", "B2", "Debate & Society"),
        ("À supposer qu'il réussisse son examen, il pourra intégrer cette grande école.", "Assuming he passes his exam, he will be able to enter this prestigious school.", "B2", "Hypothesis & Concession"),
        ("Ce phénomène s'explique principalement par l'évolution rapide des technologies.", "This phenomenon is mainly explained by the rapid evolution of technology.", "B2", "Analysis")
    ]
    
    formatted_pairs = []
    for idx, (target_fr, en, lvl, top) in enumerate(pairs):
        formatted_pairs.append({
            "id": f"fr.{lvl.lower()}.{idx+1:03d}",
            "spanish": target_fr,  # 'spanish' is the engine's target language key
            "english": en,
            "level": lvl,
            "source": "curated",
            "topic": top
        })
    return {"pairs": formatted_pairs}

def build_skills():
    skills = {
        "a1-greetings-introductions-vocab": {
            "kind": "vocabulary",
            "level": "A1",
            "family": ["personal-identity"],
            "title": "reading",
            "unit": "greetings-introductions"
        },
        "a1-at-the-cafe-vocab": {
            "kind": "vocabulary",
            "level": "A1",
            "family": ["food-drink"],
            "title": "reading",
            "unit": "at-the-cafe"
        },
        "a1-daily-routine-vocab": {
            "kind": "vocabulary",
            "level": "A1",
            "family": ["daily-life"],
            "title": "reading",
            "unit": "daily-routine"
        },
        "a1-family-friends-vocab": {
            "kind": "vocabulary",
            "level": "A1",
            "family": ["relationships"],
            "title": "reading",
            "unit": "family-friends"
        },
        "fr-present-er": {
            "kind": "grammar",
            "level": "A1",
            "family": "verb-forms",
            "title": "regular -er verbs in the present tense",
            "requires": []
        },
        "fr-present-etre-avoir": {
            "kind": "grammar",
            "level": "A1",
            "family": "verb-forms",
            "title": "être and avoir in the present tense",
            "requires": []
        },
        "fr-articles-gender": {
            "kind": "grammar",
            "level": "A1",
            "family": "articles-demonstratives",
            "title": "definite and indefinite articles",
            "requires": []
        },
        "fr-negation-ne-pas": {
            "kind": "grammar",
            "level": "A1",
            "family": "negation",
            "title": "simple negation with ne and pas",
            "requires": []
        },
        "fr-passe-compose-avoir": {
            "kind": "grammar",
            "level": "A2",
            "family": "past",
            "title": "the passé composé with avoir",
            "requires": ["fr-present-etre-avoir"]
        },
        "fr-passe-compose-etre": {
            "kind": "grammar",
            "level": "A2",
            "family": "past",
            "title": "the passé composé with être",
            "requires": ["fr-passe-compose-avoir"]
        },
        "fr-cod-pronouns": {
            "kind": "grammar",
            "level": "A2",
            "family": "pronouns",
            "title": "direct object pronouns le, la, and les",
            "requires": []
        },
        "fr-coi-pronouns": {
            "kind": "grammar",
            "level": "A2",
            "family": "pronouns",
            "title": "indirect object pronouns lui and leur",
            "requires": ["fr-cod-pronouns"]
        },
        "fr-imparfait": {
            "kind": "grammar",
            "level": "A2",
            "family": "past",
            "title": "the imperfect tense",
            "requires": ["fr-passe-compose-avoir"]
        },
        "fr-subjonctif-present": {
            "kind": "grammar",
            "level": "B1",
            "family": "subjunctive",
            "title": "the present subjunctive and its triggers",
            "requires": ["fr-imparfait"]
        },
        "fr-participle-agreement": {
            "kind": "grammar",
            "level": "B1",
            "family": "non-finite",
            "title": "past participle agreement",
            "requires": ["fr-passe-compose-etre", "fr-cod-pronouns"]
        }
    }
    
    frozen = {
        "_comment": "The frozen fr skill list. Every skill in skills/fr.json must be listed here.",
        "skills": {slug: "2026-10-16: initial French skill list" for slug in skills}
    }
    
    fr_registry_src = {
        "_comment": "Source of truth for the French skill registry.",
        "language": "fr",
        "courses": ["fr"],
        "skills": skills
    }
    return fr_registry_src, frozen

def main():
    write_json(ROOT / "content/fr/writing-prompts.json", build_writing_prompts())
    write_json(ROOT / "content/fr/speaking-prompts.json", build_speaking_prompts())
    write_json(ROOT / "content/fr/writing-exchanges.json", build_writing_exchanges())
    write_json(ROOT / "content/fr/conversation-scenarios.json", build_conversation_scenarios())
    write_json(ROOT / "content/fr/curriculum/challenges.json", build_challenges())
    write_json(ROOT / "content/fr/indexes/translation-index.json", build_translation_index())
    
    fr_src, frozen = build_skills()
    write_json(ROOT / "skills/fr.json", fr_src)
    write_json(ROOT / "skills/frozen-fr.json", frozen)
    print("Done scaffolding French prompt and skill files.")

if __name__ == "__main__":
    main()
