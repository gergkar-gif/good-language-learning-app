#!/usr/bin/env python3
"""
Generates comprehensive CEFR-aligned conversation scenarios:
- A1: 8 scenarios (with full English descriptions & vocabulary hints)
- A2: 10 scenarios (with full English descriptions & vocabulary hints)
- B1: 10 scenarios (target language only, authentic roleplays)

Outputs:
- content/es-latam/conversation-scenarios.json
- content/es-es/conversation-scenarios.json
- content/hu/conversation-scenarios.json (preserves existing + expands key roleplays)
"""

import json
from pathlib import Path

ES_SCENARIOS = [
    # -------------------------------------------------------------
    # A1 SCENARIOS (8)
    # -------------------------------------------------------------
    {
        "id": "es-a1-sc01-cafe",
        "cefrLevel": "A1",
        "title": "En el Café",
        "titleEn": "At the Café",
        "situation": "Estás en una cafetería en Madrid y quieres pedir algo de beber y comer, y luego pedir la cuenta.",
        "situationEn": "You are in a café in Madrid and you want to order something to drink and eat, and then ask for the bill.",
        "roleplay": {
            "interlocutorRole": "Camarero / Camarera",
            "interlocutorRoleEn": "Waiter / Waitress",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Customer",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can order food and drink in a café and ask for the bill",
        "targetSkills": ["ordering_food", "social_interaction", "numbers_and_prices"],
        "unitIds": ["unit.a1.11"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola, buenas tardes! Bienvenido. ¿Qué le gustaría tomar?",
                "interlocutorTranslation": "Hello, good afternoon! Welcome. What would you like to have?",
                "learnerCue": "Saluda educadamente y pide un café con leche (o té) y un cruasán (o tostada).",
                "learnerCueEn": "Greet politely and order a white coffee (or tea) and a croissant (or toast).",
                "vocabularyHints": [
                    "un café con leche — a white coffee",
                    "una tostada — a piece of toast",
                    "un cruasán — a croissant",
                    "Quisiera... — I would like...",
                    "por favor — please"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["café", "té", "agua", "leche", "tostada", "cruasán", "por favor", "quisiera", "quiero"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Perfecto, un café con leche y una tostada. ¿Desea el café caliente o con hielo? ¿Y azúcar?",
                "interlocutorTranslation": "Perfect, a white coffee and toast. Would you like the coffee hot or iced? And sugar?",
                "learnerCue": "Responde cómo prefieres el café (caliente o frío) y si quieres azúcar o no.",
                "learnerCueEn": "Answer how you prefer your coffee (hot or cold) and if you want sugar or not.",
                "vocabularyHints": [
                    "caliente — hot",
                    "con hielo — with ice / iced",
                    "con poco azúcar — with a little sugar",
                    "sin azúcar — without sugar",
                    "gracias — thank you"
                ],
                "validationCriteria": {
                    "minWords": 2,
                    "targetKeywords": ["caliente", "frío", "hielo", "azúcar", "sin", "con", "gracias"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Aquí tiene su pedido. ¡Que lo disfrute! ¿Necesita algo más por ahora?",
                "interlocutorTranslation": "Here is your order. Enjoy! Do you need anything else for now?",
                "learnerCue": "Agradece y di que todo está bien, y pide la cuenta por favor.",
                "learnerCueEn": "Say thank you, mention that everything is fine, and ask for the bill please.",
                "vocabularyHints": [
                    "todo está muy bien — everything is fine / very good",
                    "la cuenta — the bill / check",
                    "¿Cuánto es? — How much is it?",
                    "¿Me trae...? — Can you bring me...?",
                    "nada más — nothing else"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "cuenta", "cuánto", "nada más", "por favor", "cobrar"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc02-hotel",
        "cefrLevel": "A1",
        "title": "Registro en el Hotel",
        "titleEn": "Hotel Check-in",
        "situation": "Llegas a la recepción de un hotel en Salamanca sin reserva previa buscando una habitación.",
        "situationEn": "You arrive at the reception of a hotel in Salamanca without a prior reservation looking for a room.",
        "roleplay": {
            "interlocutorRole": "Recepcionista",
            "interlocutorRoleEn": "Receptionist",
            "learnerRole": "Huésped",
            "learnerRoleEn": "Guest",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can enquire about room availability and check into a hotel",
        "targetSkills": ["hotel_checkin", "dates_and_duration", "enquiring_services"],
        "unitIds": ["unit.a1.26"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Buenas noches! Bienvenido al Hotel San Martín. ¿Tiene una reserva con nosotros?",
                "interlocutorTranslation": "Good evening! Welcome to Hotel San Martín. Do you have a reservation with us?",
                "learnerCue": "Di que no tienes reserva, pero necesitas una habitación individual para dos noches.",
                "learnerCueEn": "Say that you do not have a reservation, but you need a single room for two nights.",
                "vocabularyHints": [
                    "no tengo reserva — I don't have a reservation",
                    "necesito... — I need...",
                    "una habitación individual — a single room",
                    "para dos noches — for two nights",
                    "por favor — please"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["no", "reserva", "habitación", "individual", "dos", "noches", "tengo", "necesito"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Sí, tenemos disponibilidad. Son sesenta euros por noche. ¿Desea incluir el desayuno buffet por ocho euros más?",
                "interlocutorTranslation": "Yes, we have availability. It is sixty euros per night. Would you like to include the buffet breakfast for eight euros more?",
                "learnerCue": "Acepta (o rechaza) el desayuno y pregunta si hay conexión wifi en la habitación.",
                "learnerCueEn": "Accept (or decline) the breakfast and ask if there is Wi-Fi connection in the room.",
                "vocabularyHints": [
                    "con desayuno — with breakfast",
                    "sin desayuno — without breakfast",
                    "¿Hay wifi...? — Is there Wi-Fi...?",
                    "en la habitación — in the room",
                    "gratis — free"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["sí", "no", "desayuno", "wifi", "internet", "gratis", "habitación", "gracias", "favor"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "El wifi es gratuito en todo el hotel. La contraseña está en su tarjeta llave. ¿Puede prestarme su pasaporte o documento de identidad para el registro?",
                "interlocutorTranslation": "Wi-Fi is free throughout the hotel. The password is on your key card. Could you lend me your passport or ID card for check-in?",
                "learnerCue": "Entrega tu pasaporte amablemente y pregunta a qué hora es el check-out o la salida.",
                "learnerCueEn": "Hand over your passport politely and ask what time check-out or departure is.",
                "vocabularyHints": [
                    "aquí tiene — here you go / here is",
                    "mi pasaporte — my passport",
                    "¿A qué hora es...? — What time is...?",
                    "la salida / el check-out — check-out",
                    "mañana — tomorrow"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["aquí", "pasaporte", "documento", "tiene", "hora", "salida", "check-out", "gracias"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc03-supermercado",
        "cefrLevel": "A1",
        "title": "En el Supermercado",
        "titleEn": "At the Supermarket",
        "situation": "Estás haciendo la compra en el supermercado y necesitas encontrar productos y pagar en la caja.",
        "situationEn": "You are shopping at the supermarket and need to find items and pay at the checkout.",
        "roleplay": {
            "interlocutorRole": "Empleado / Cajero",
            "interlocutorRoleEn": "Store Clerk / Cashier",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Shopper",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can ask for grocery items, quantities, and complete a store checkout",
        "targetSkills": ["shopping_food", "asking_location", "transactions_and_payment"],
        "unitIds": ["unit.a1.09", "unit.a1.10"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! ¿Busca algo en particular?",
                "interlocutorTranslation": "Hello! Looking for something in particular?",
                "learnerCue": "Pregunta disculpándote dónde está la sección de fruta o pan.",
                "learnerCueEn": "Excuse yourself and ask where the fruit or bread section is.",
                "vocabularyHints": [
                    "disculpe — excuse me",
                    "¿Dónde está...? — Where is...?",
                    "la fruta — the fruit",
                    "el pan fresco — fresh bread",
                    "el pasillo — aisle"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["dónde", "está", "fruta", "pan", "sección", "disculpe", "por favor"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "La fruta está al fondo a la derecha y el pan en el pasillo dos. ¿Cuánto desea llevar?",
                "interlocutorTranslation": "The fruit is in the back on the right, and bread in aisle two. How much would you like to take?",
                "learnerCue": "Pide un kilo de manzanas (o plátanos) y una barra de pan.",
                "learnerCueEn": "Ask for one kilo of apples (or bananas) and a loaf of bread.",
                "vocabularyHints": [
                    "un kilo de... — a kilo of...",
                    "manzanas / plátanos — apples / bananas",
                    "una barra de pan — a loaf of bread",
                    "quisiera llevar — I would like to take"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["kilo", "manzanas", "plátanos", "pan", "barra", "quiero", "quisiera"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Muy bien. En total son cinco euros con cincuenta. ¿Necesita bolsa de plástico o papel?",
                "interlocutorTranslation": "Very well. That's 5.50 euros in total. Do you need a plastic or paper bag?",
                "learnerCue": "Responde si necesitas bolsa y di que pagarás con tarjeta.",
                "learnerCueEn": "Answer whether you need a bag and say you will pay with card.",
                "vocabularyHints": [
                    "una bolsa, por favor — a bag, please",
                    "no necesito bolsa — I don't need a bag",
                    "tengo mi propia bolsa — I have my own bag",
                    "pago con tarjeta — I pay with card"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["bolsa", "tarjeta", "sí", "no", "efectivo", "pago", "gracias"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc04-farmacia",
        "cefrLevel": "A1",
        "title": "En la Farmacia",
        "titleEn": "At the Pharmacy",
        "situation": "Tienes dolor de cabeza y resfriado, y vas a la farmacia a pedir algo para aliviar los síntomas.",
        "situationEn": "You have a headache and a cold, and you go to the pharmacy to ask for something to relieve the symptoms.",
        "roleplay": {
            "interlocutorRole": "Farmacéutico / Farmacéutica",
            "interlocutorRoleEn": "Pharmacist",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Customer",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can explain simple health ailments and ask for over-the-counter medicine",
        "targetSkills": ["describing_symptoms", "health_needs", "following_instructions"],
        "unitIds": ["unit.a1.20", "unit.a1.21"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenos días. ¿En qué le puedo colaborar hoy?",
                "interlocutorTranslation": "Good morning. How can I help you today?",
                "learnerCue": "Explica que te duele la cabeza y que tienes resfriado.",
                "learnerCueEn": "Explain that your head hurts and that you have a cold.",
                "vocabularyHints": [
                    "me duele la cabeza — my head hurts",
                    "tengo resfriado — I have a cold",
                    "no me siento bien — I don't feel well",
                    "desde ayer — since yesterday"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["duele", "cabeza", "resfriado", "gripe", "mal", "tengo"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Entiendo. Le recomiendo paracetamol o ibuprofeno. ¿Tiene alguna alergia a medicamentos?",
                "interlocutorTranslation": "I understand. I recommend paracetamol or ibuprofen. Do you have any medication allergies?",
                "learnerCue": "Di que no tienes alergias y pide una caja de paracetamol.",
                "learnerCueEn": "Say you have no allergies and ask for a box of paracetamol.",
                "vocabularyHints": [
                    "no tengo alergias — I have no allergies",
                    "una caja de paracetamol — a box of paracetamol",
                    "por favor — please",
                    "¿cuánto cuesta? — how much does it cost?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["no", "alergia", "paracetamol", "ibuprofeno", "caja", "por favor"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Aquí tiene. Tome un comprimido cada ocho horas con agua. Son cuatro euros.",
                "interlocutorTranslation": "Here you go. Take one tablet every eight hours with water. That is four euros.",
                "learnerCue": "Agradece el consejo, paga en efectivo o tarjeta y despídete.",
                "learnerCueEn": "Thank them for the advice, pay with cash or card, and say goodbye.",
                "vocabularyHints": [
                    "muchas gracias por la ayuda — thank you very much for the help",
                    "aquí tiene cuatro euros — here are four euros",
                    "con tarjeta — with card",
                    "hasta luego — goodbye / see you later"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "tarjeta", "efectivo", "euros", "adiós", "luego"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc05-tienda-ropa",
        "cefrLevel": "A1",
        "title": "Comprando Ropa",
        "titleEn": "Buying Clothes",
        "situation": "Estás en una tienda buscando una camiseta o un pantalón de tu talla y color favorito.",
        "situationEn": "You are in a clothing store looking for a t-shirt or trousers in your size and favorite color.",
        "roleplay": {
            "interlocutorRole": "Dependiente / Dependienta",
            "interlocutorRoleEn": "Sales Assistant",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Shopper",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can ask for clothing sizes, colors, and ask for the fitting room",
        "targetSkills": ["shopping_clothes", "describing_items", "asking_assistance"],
        "unitIds": ["unit.a1.10", "unit.a1.03"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! ¿Le gustaría ver alguna prenda en especial?",
                "interlocutorTranslation": "Hello! Would you like to see any garment in particular?",
                "learnerCue": "Di que buscas una camiseta azul o negra de talla mediana (M).",
                "learnerCueEn": "Say you are looking for a blue or black t-shirt in medium size (M).",
                "vocabularyHints": [
                    "busco una camiseta — I am looking for a t-shirt",
                    "color azul / negro — blue / black color",
                    "talla mediana (M) — medium size",
                    "¿tiene...? — do you have...?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["busco", "camiseta", "pantalón", "talla", "azul", "negro", "mediana"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Sí, aquí tenemos esta camiseta de algodón en azul marino. ¿Desea probársela?",
                "interlocutorTranslation": "Yes, here we have this cotton t-shirt in navy blue. Would you like to try it on?",
                "learnerCue": "Di que sí y pregunta dónde están los probadores.",
                "learnerCueEn": "Say yes and ask where the fitting rooms are.",
                "vocabularyHints": [
                    "sí, me gustaría probarla — yes, I'd like to try it on",
                    "¿Dónde están los probadores? — Where are the fitting rooms?",
                    "muchas gracias — thank you very much"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["sí", "probar", "dónde", "probador", "probadores", "gracias"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "¿Qué tal le queda la camiseta? ¿Es de su gusto?",
                "interlocutorTranslation": "How does the t-shirt fit you? Is it to your liking?",
                "learnerCue": "Di que te queda muy bien y que te la llevas.",
                "learnerCueEn": "Say that it fits very well and that you will take it.",
                "vocabularyHints": [
                    "me queda muy bien — it fits me very well",
                    "me la llevo — I'll take it",
                    "es perfecta — it is perfect",
                    "¿Dónde se paga? — Where do I pay?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["queda", "bien", "llevo", "gusta", "compro", "cuánto"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc06-presentacion",
        "cefrLevel": "A1",
        "title": "Conociendo a un Vecino",
        "titleEn": "Meeting a Neighbor",
        "situation": "Acabas de mudarte a un nuevo edificio y te encuentras con un vecino en la entrada.",
        "situationEn": "You just moved to a new building and meet a neighbor at the entrance.",
        "roleplay": {
            "interlocutorRole": "Vecino / Vecina",
            "interlocutorRoleEn": "Neighbor",
            "learnerRole": "Nuevo Residente",
            "learnerRoleEn": "New Resident",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can introduce myself, state my name, origin, and exchange simple personal information",
        "targetSkills": ["introductions", "personal_info", "social_exchange"],
        "unitIds": ["unit.a1.01", "unit.a1.02"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! Creo que eres nuevo en el edificio. Me llamo Carlos, vivo en el tercer piso.",
                "interlocutorTranslation": "Hello! I think you are new in the building. My name is Carlos, I live on the third floor.",
                "learnerCue": "Saluda, di tu nombre y di qué piso o apartamento ocupas.",
                "learnerCueEn": "Greet him, say your name, and mention which floor or apartment you live in.",
                "vocabularyHints": [
                    "mucho gusto — pleased to meet you",
                    "me llamo... — my name is...",
                    "vivo en el segundo piso — I live on the second floor",
                    "encantado / encantada — delighted"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["hola", "llamo", "soy", "vivo", "piso", "mucho gusto", "encantado", "encantada"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¡Bienvenido al barrio! Tienes un acento interesante, ¿de dónde eres originalmente?",
                "interlocutorTranslation": "Welcome to the neighborhood! You have an interesting accent, where are you from originally?",
                "learnerCue": "Di de qué país o ciudad eres y que estudias o trabajas aquí.",
                "learnerCueEn": "Say which country or city you are from and that you work or study here.",
                "vocabularyHints": [
                    "soy de... — I am from...",
                    "ahora vivo aquí — now I live here",
                    "estudio español — I study Spanish",
                    "trabajo aquí — I work here"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["soy", "de", "país", "vivo", "estudio", "trabajo"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "¡Qué bien! Si necesitas ayuda con el edificio o el barrio, no dudes en decirme. ¡Nos vemos!",
                "interlocutorTranslation": "Great! If you need help with the building or neighborhood, don't hesitate to let me know. See you around!",
                "learnerCue": "Agradece la amabilidad y despídete diciendo que tengan un buen día.",
                "learnerCueEn": "Thank him for his kindness and say goodbye wishing him a nice day.",
                "vocabularyHints": [
                    "muchas gracias por tu ayuda — thank you very much for your help",
                    "muy amable — very kind",
                    "hasta luego — see you later",
                    "buen día — good day"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "amable", "luego", "buen día", "adiós", "vemos"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc07-taxi",
        "cefrLevel": "A1",
        "title": "Tomando un Taxi",
        "titleEn": "Taking a Taxi",
        "situation": "Tomas un taxi en el centro de la ciudad para ir al aeropuerto o a tu hotel.",
        "situationEn": "You take a taxi in the city center to go to the airport or your hotel.",
        "roleplay": {
            "interlocutorRole": "Taxista",
            "interlocutorRoleEn": "Taxi Driver",
            "learnerRole": "Pasajero",
            "learnerRoleEn": "Passenger",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can state travel destinations, ask about trip duration, and pay taxi fares",
        "targetSkills": ["city_travel", "asking_time", "numbers_and_payment"],
        "unitIds": ["unit.a1.14", "unit.a1.15"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Buenas! Suba. ¿A dónde lo llevo?",
                "interlocutorTranslation": "Hello! Get in. Where should I take you?",
                "learnerCue": "Saluda y di la dirección o destino (al aeropuerto Terminal 4 o al Hotel Central).",
                "learnerCueEn": "Greet the driver and state your destination (to Airport Terminal 4 or Hotel Central).",
                "vocabularyHints": [
                    "buenas tardes — good afternoon",
                    "al aeropuerto, por favor — to the airport, please",
                    "a la calle Mayor — to Mayor street",
                    "Terminal cuatro — Terminal 4"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["aeropuerto", "hotel", "calle", "terminal", "llegar", "favor"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Muy bien, vamos al aeropuerto. Hay un poco de tráfico en la autopista hoy.",
                "interlocutorTranslation": "Very well, off to the airport. There is a bit of traffic on the highway today.",
                "learnerCue": "Pregunta cuánto tiempo durará el viaje aproximadamente.",
                "learnerCueEn": "Ask how long the trip will take approximately.",
                "vocabularyHints": [
                    "¿Cuánto tiempo dura el viaje? — How long does the trip take?",
                    "¿Cuántos minutos? — How many minutes?",
                    "¿A qué hora llegamos? — What time do we arrive?",
                    "aproximadamente — approximately"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["tiempo", "dura", "tarda", "minutos", "hora", "llegar", "cuánto"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Llegaremos en unos veinte minutos... Ya estamos aquí. Son veinticinco euros.",
                "interlocutorTranslation": "We will arrive in about twenty minutes... Here we are. That is twenty-five euros.",
                "learnerCue": "Pregunta si puedes pagar con tarjeta y agradece el servicio.",
                "learnerCueEn": "Ask if you can pay with card and thank the driver for the ride.",
                "vocabularyHints": [
                    "¿Puedo pagar con tarjeta? — Can I pay with card?",
                    "aquí tiene el dinero — here is the money",
                    "muchas gracias — thank you very much",
                    "quédese con el cambio — keep the change"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["tarjeta", "efectivo", "pagar", "gracias", "euros", "puedo"]
                }
            }
        ]
    },
    {
        "id": "es-a1-sc08-restaurante",
        "cefrLevel": "A1",
        "title": "Cena en el Restaurante",
        "titleEn": "Dinner at the Restaurant",
        "situation": "Llegas a un restaurante típico para cenar con un amigo.",
        "situationEn": "You arrive at a typical restaurant to have dinner with a friend.",
        "roleplay": {
            "interlocutorRole": "Camarero / Maître",
            "interlocutorRoleEn": "Waiter / Host",
            "learnerRole": "Comensal",
            "learnerRoleEn": "Diner",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can request a table, order dishes from a menu, and ask for tableware",
        "targetSkills": ["restaurant_dining", "food_ordering", "polite_requests"],
        "unitIds": ["unit.a1.11", "unit.a1.14"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Buenas noches! ¿Tienen reserva o desean una mesa libre?",
                "interlocutorTranslation": "Good evening! Do you have a reservation or do you want an available table?",
                "learnerCue": "Di que no tienen reserva y pide una mesa para dos personas.",
                "learnerCueEn": "Say that you don't have a reservation and ask for a table for two people.",
                "vocabularyHints": [
                    "buenas noches — good evening",
                    "no tenemos reserva — we don't have a reservation",
                    "una mesa para dos — a table for two",
                    "cerca de la ventana — near the window"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["mesa", "dos", "personas", "reserva", "por favor", "queremos"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Por aquí, por favor. Aquí tienen la carta. ¿Qué desean pedir de primer plato y bebida?",
                "interlocutorTranslation": "This way, please. Here is the menu. What would you like to order for the starter and drinks?",
                "learnerCue": "Pide una ensalada mixta, sopa y una botella de agua mineral.",
                "learnerCueEn": "Order a mixed salad, soup, and a bottle of mineral water.",
                "vocabularyHints": [
                    "de primero, una ensalada — for starter, a salad",
                    "una sopa caliente — hot soup",
                    "una botella de agua — a bottle of water",
                    "con gas / sin gas — sparkling / still"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["ensalada", "sopa", "agua", "primero", "pedir", "quisiera", "tomar"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Enseguida se lo traigo. ¿Desean pan o algo más para acompañar?",
                "interlocutorTranslation": "I will bring it right away. Would you like bread or anything else to accompany it?",
                "learnerCue": "Pide una cesta de pan y servilletas adicionales.",
                "learnerCueEn": "Ask for a bread basket and extra napkins.",
                "vocabularyHints": [
                    "sí, un poco de pan — yes, a little bread",
                    "servilletas por favor — napkins please",
                    "muchas gracias — thank you very much",
                    "todo bien — all good"
                ],
                "validationCriteria": {
                    "minWords": 2,
                    "targetKeywords": ["pan", "servilletas", "sí", "gracias", "favor"]
                }
            }
        ]
    },

    # -------------------------------------------------------------
    # A2 SCENARIOS (10)
    # -------------------------------------------------------------
    {
        "id": "es-a2-sc01-tren",
        "cefrLevel": "A2",
        "title": "Comprando un Billete de Tren",
        "titleEn": "Buying a Train Ticket",
        "situation": "Estás en la taquilla de la estación de Atocha en Madrid y necesitas comprar un billete para viajar a Sevilla.",
        "situationEn": "You are at the ticket office of Atocha station in Madrid and you need to buy a ticket to travel to Seville.",
        "roleplay": {
            "interlocutorRole": "Taquillero / Taquillera de Renfe",
            "interlocutorRoleEn": "Renfe Ticket Clerk",
            "learnerRole": "Viajero",
            "learnerRoleEn": "Traveler",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can buy a train ticket, enquire about schedules, and clarify journey details",
        "targetSkills": ["travel_arrangements", "asking_timetable", "transactional_clarification"],
        "unitIds": ["unit.a2.18", "unit.a2.01"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Siguiente, por favor. Buenos días, ¿a dónde desea viajar?",
                "interlocutorTranslation": "Next, please. Good morning, where do you wish to travel?",
                "learnerCue": "Di que quieres comprar un billete de ida y vuelta para Sevilla para este fin de semana.",
                "learnerCueEn": "Say that you want to buy a round-trip ticket to Seville for this weekend.",
                "vocabularyHints": [
                    "quisiera — I would like",
                    "un billete de ida y vuelta — a round-trip ticket",
                    "a Sevilla — to Seville",
                    "para este fin de semana — for this weekend",
                    "por favor — please"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["Sevilla", "billete", "ida", "vuelta", "viajar", "fin de semana", "quisiera", "tren"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Muy bien. El sábado por la mañana sale un tren de alta velocidad a las nueve y cuarto y otro a las once y media. ¿Cuál prefiere?",
                "interlocutorTranslation": "Very well. On Saturday morning a high-speed train leaves at 9:15 and another at 11:30. Which do you prefer?",
                "learnerCue": "Elige el tren de las nueve y cuarto y pregunta cuánto dura el viaje.",
                "learnerCueEn": "Choose the quarter past nine train and ask how long the journey takes.",
                "vocabularyHints": [
                    "prefiero — I prefer",
                    "el de las nueve y cuarto — the one at nine fifteen",
                    "¿Cuánto tiempo dura...? — How long does ... take?",
                    "el viaje — the trip / journey",
                    "¿A qué hora llega? — What time does it arrive?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["nueve", "cuarto", "once", "dura", "tiempo", "viaje", "llega", "horas", "prefiero"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "El viaje dura aproximadamente dos horas y media. Son setenta y cinco euros en total. ¿Va a pagar con tarjeta o en efectivo?",
                "interlocutorTranslation": "The trip lasts approximately two and a half hours. It is seventy-five euros in total. Will you pay by card or cash?",
                "learnerCue": "Indica que pagarás con tarjeta y pregunta desde qué vía o andén sale el tren.",
                "learnerCueEn": "Indicate that you will pay by card and ask which track or platform the train leaves from.",
                "vocabularyHints": [
                    "pagaré — I will pay",
                    "con tarjeta — by card",
                    "¿De qué andén sale...? — From which platform does ... leave?",
                    "la vía de salida — the departure track",
                    "el tren — the train"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["tarjeta", "efectivo", "vía", "andén", "sale", "tren", "pagar", "gracias"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc02-direcciones",
        "cefrLevel": "A2",
        "title": "Pidiendo Direcciones en la Ciudad",
        "titleEn": "Asking for Directions in the City",
        "situation": "Estás paseando por el centro de Valencia y estás buscando el Museo de Bellas Artes pero te has desorientado.",
        "situationEn": "You are walking through the center of Valencia and you are looking for the Museum of Fine Arts but you are disoriented.",
        "roleplay": {
            "interlocutorRole": "Transeúnte local",
            "interlocutorRoleEn": "Local passerby",
            "learnerRole": "Turista",
            "learnerRoleEn": "Tourist",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can ask for and understand directional guidance in a city",
        "targetSkills": ["asking_directions", "spatial_orientation", "polite_enquiry"],
        "unitIds": ["unit.a1.16", "unit.a2.23"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Hola, disculpe, ¿le puedo ayudar en algo? Parece que está buscando algo en el mapa.",
                "interlocutorTranslation": "Hello, excuse me, can I help you with something? It looks like you're looking for something on the map.",
                "learnerCue": "Saluda amablemente y pregunta cómo se llega al Museo de Bellas Artes o si está muy lejos.",
                "learnerCueEn": "Greet politely and ask how to get to the Museum of Fine Arts or if it is very far.",
                "vocabularyHints": [
                    "disculpe — excuse me",
                    "¿Cómo puedo llegar a...? — How can I get to...?",
                    "el Museo de Bellas Artes — the Museum of Fine Arts",
                    "¿Está muy lejos? — Is it very far?",
                    "de aquí — from here"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["museo", "llegar", "dónde", "lejos", "cerca", "bellas artes", "disculpe", "favor"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "No está muy lejos, a unos diez minutos a pie. Debe seguir todo recto por esta calle hasta cruzar el puente sobre el río.",
                "interlocutorTranslation": "It's not very far, about ten minutes on foot. You should continue straight ahead along this street until crossing the bridge over the river.",
                "learnerCue": "Confirma la indicación y pregunta si debes girar a la derecha o a la izquierda después de cruzar el puente.",
                "learnerCueEn": "Confirm the directions and ask if you should turn right or left after crossing the bridge.",
                "vocabularyHints": [
                    "entiendo — I understand",
                    "cruzar el puente — to cross the bridge",
                    "después de... — after...",
                    "¿debo girar? — should I turn?",
                    "a la derecha / a la izquierda — to the right / to the left"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["puente", "derecha", "izquierda", "girar", "doblar", "después", "recto"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Justo al cruzar el puente, gire a la derecha y verá los jardines y la entrada principal. ¡Es muy fácil!",
                "interlocutorTranslation": "Right upon crossing the bridge, turn right and you will see the gardens and the main entrance. It's very easy!",
                "learnerCue": "Agradece la ayuda con amabilidad y despídete deseándole un buen día.",
                "learnerCueEn": "Thank them kindly for their help and say goodbye wishing them a good day.",
                "vocabularyHints": [
                    "muchísimas gracias — thank you very much",
                    "por su ayuda — for your help",
                    "que tenga un buen día — have a good day",
                    "hasta luego — see you later",
                    "perfecto — perfect"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "muchas", "ayuda", "buen día", "tenga", "hasta luego", "adiós"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc03-planes-amigo",
        "cefrLevel": "A2",
        "title": "Haciendo Planes con un Amigo",
        "titleEn": "Making Weekend Plans with a Friend",
        "situation": "Estás hablando por teléfono con un amigo para organizar una salida este fin de semana.",
        "situationEn": "You are talking on the phone with a friend to organize an outing this weekend.",
        "roleplay": {
            "interlocutorRole": "Amigo / Amiga",
            "interlocutorRoleEn": "Friend",
            "learnerRole": "Amigo / Amiga",
            "learnerRoleEn": "Friend",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can propose plans, negotiate meeting times, and agree on weekend activities",
        "targetSkills": ["invitations_and_plans", "negotiating_time", "social_conversation"],
        "unitIds": ["unit.a2.08", "unit.a2.16"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! ¿Tienes planes para el sábado por la tarde? Pensaba ir al cine o al parque.",
                "interlocutorTranslation": "Hello! Do you have plans for Saturday afternoon? I was thinking of going to the cinema or the park.",
                "learnerCue": "Di que estás libre y propón ir al cine a ver una película nueva.",
                "learnerCueEn": "Say you are free and propose going to the cinema to see a new movie.",
                "vocabularyHints": [
                    "estoy libre — I am free",
                    "me parece genial — sounds great to me",
                    "¿Por qué no vamos al cine? — Why don't we go to the movies?",
                    "una película nueva — a new movie"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["libre", "cine", "película", "vamos", "parque", "sábado", "gusta"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¡Me encanta la idea! Hay una sesión a las cinco y otra a las siete y media. ¿Cuál te va mejor?",
                "interlocutorTranslation": "I love the idea! There is a screening at five and another at seven thirty. Which suits you better?",
                "learnerCue": "Elige la sesión de las siete y media y propón tomar un café antes.",
                "learnerCueEn": "Choose the 7:30 session and suggest having coffee beforehand.",
                "vocabularyHints": [
                    "prefiero la sesión de las siete — I prefer the 7 o'clock screening",
                    "¿Tomamos un café antes? — Shall we have coffee before?",
                    "a las seis y media — at six thirty",
                    "cerca del cine — near the cinema"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["siete", "media", "café", "antes", "sesión", "quedar", "ver"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Quedamos entonces a las seis y media en la cafetería enfrente del cine. ¡Hasta el sábado!",
                "interlocutorTranslation": "Let's meet then at six thirty at the café across from the cinema. See you Saturday!",
                "learnerCue": "Confirma la cita y despídete con entusiasmo.",
                "learnerCueEn": "Confirm the meeting and say goodbye enthusiastically.",
                "vocabularyHints": [
                    "perfecto, quedamos allí — perfect, we meet there",
                    "nos vemos el sábado — see you Saturday",
                    "¡Hasta pronto! — see you soon!"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["perfecto", "allí", "sábado", "vemos", "hasta", "luego"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc04-queja-hotel",
        "cefrLevel": "A2",
        "title": "Una Queja en el Hotel",
        "titleEn": "A Hotel Room Issue",
        "situation": "Estás en tu habitación de hotel y el aire acondicionado hace mucho ruido y no enfría.",
        "situationEn": "You are in your hotel room and the air conditioner is making loud noises and not cooling.",
        "roleplay": {
            "interlocutorRole": "Recepcionista de Hotel",
            "interlocutorRoleEn": "Hotel Receptionist",
            "learnerRole": "Huésped",
            "learnerRoleEn": "Hotel Guest",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can explain a problem in hotel accommodation and request a solution or room change",
        "targetSkills": ["complaints_and_problems", "polite_requests", "expressing_dissatisfaction"],
        "unitIds": ["unit.a2.15", "unit.a2.26"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Recepción, buenas tardes. ¿En qué le puedo asistir?",
                "interlocutorTranslation": "Front desk, good afternoon. How may I assist you?",
                "learnerCue": "Identifica tu número de habitación y explica que el aire acondicionado no funciona.",
                "learnerCueEn": "Identify your room number and explain that the air conditioning is not working.",
                "vocabularyHints": [
                    "llamo de la habitación... — I'm calling from room...",
                    "el aire acondicionado — the air conditioning",
                    "no funciona bien — is not working properly",
                    "hace mucho ruido — makes a lot of noise",
                    "hace mucho calor — it's very hot"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["habitación", "aire", "funciona", "ruido", "calor", "problema"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Lamento mucho el inconveniente. Puedo enviar a un técnico ahora mismo o cambiarle a otra habitación en el cuarto piso.",
                "interlocutorTranslation": "I am very sorry for the inconvenience. I can send a technician right now or move you to another room on the fourth floor.",
                "learnerCue": "Pide cambiar de habitación para poder descansar inmediatamente.",
                "learnerCueEn": "Ask to change rooms so that you can rest immediately.",
                "vocabularyHints": [
                    "prefiero cambiar de habitación — I prefer to change rooms",
                    "estoy muy cansado / cansada — I am very tired",
                    "necesito descansar — I need to rest",
                    "¿puedo tener las llaves? — can I have the keys?"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["cambiar", "habitación", "piso", "descansar", "prefiero", "gracias"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Por supuesto. Un botones subirá de inmediato con las nuevas llaves y le ayudará con el equipaje.",
                "interlocutorTranslation": "Of course. A bellboy will come up immediately with the new keys and help you with your luggage.",
                "learnerCue": "Agradece la rápida solución y amabilidad.",
                "learnerCueEn": "Thank them for the quick solution and kindness.",
                "vocabularyHints": [
                    "muchas gracias por la rapidez — thank you very much for the quick response",
                    "muy amable — very kind",
                    "aquí espero — I'll wait here"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "amabilidad", "rapidez", "ayuda", "espero"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc05-alquilar-bici",
        "cefrLevel": "A2",
        "title": "Alquilando una Bicicleta",
        "titleEn": "Renting a Bicycle",
        "situation": "Deseas alquilar una bicicleta urbana para recorrer el parque y la playa durante el día.",
        "situationEn": "You want to rent a city bike to explore the park and the beach during the day.",
        "roleplay": {
            "interlocutorRole": "Encargado / Encargada del Alquiler",
            "interlocutorRoleEn": "Rental Shop Attendant",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Customer",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can rent leisure equipment, enquire about rental terms, safety gear, and deposits",
        "targetSkills": ["rental_transactions", "clarification", "price_enquiry"],
        "unitIds": ["unit.a2.07", "unit.a2.12"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! Bienvenidos a BiciTours. ¿Busca alquilar una bicicleta de paseo o eléctrica?",
                "interlocutorTranslation": "Hello! Welcome to BiciTours. Are you looking to rent a city bike or an electric bike?",
                "learnerCue": "Pide una bicicleta de paseo para todo el día y pregunta el precio.",
                "learnerCueEn": "Ask for a city bike for the whole day and ask about the price.",
                "vocabularyHints": [
                    "quisiera alquilar — I'd like to rent",
                    "una bicicleta de paseo — a city bike",
                    "para todo el día — for the whole day",
                    "¿Cuánto cuesta el alquiler? — How much is the rental?"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["alquilar", "bicicleta", "paseo", "día", "precio", "cuesta", "cuánto"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Son quince euros el día completo. Incluye casco y candado de seguridad. ¿Qué altura tiene para ajustar el sillín?",
                "interlocutorTranslation": "It's fifteen euros for the full day. It includes a helmet and security lock. What is your height to adjust the saddle?",
                "learnerCue": "Indica tu estatura aproximada y pregunta a qué hora cierra la tienda.",
                "learnerCueEn": "State your approximate height and ask what time the shop closes.",
                "vocabularyHints": [
                    "mido un metro setenta — I am 1.70 meters tall",
                    "altura media — medium height",
                    "¿A qué hora cierran por la tarde? — What time do you close in the evening?",
                    "la devolución — return"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["mido", "metro", "hora", "cierra", "tarde", "devolver"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Cerramos a las ocho de la tarde. Necesito una fianza de veinte euros que le devolveremos al regresar.",
                "interlocutorTranslation": "We close at eight in the evening. I need a twenty euro deposit which we will return when you bring it back.",
                "learnerCue": "Acepta las condiciones, entrega la fianza y agradece las recomendaciones.",
                "learnerCueEn": "Accept the terms, hand over the deposit, and thank them for the tips.",
                "vocabularyHints": [
                    "de acuerdo — agreed / alright",
                    "aquí tiene la fianza — here is the deposit",
                    "muchas gracias — thank you very much",
                    "¡Hasta la tarde! — see you this afternoon!"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["acuerdo", "fianza", "euros", "gracias", "tarde", "aquí"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc06-objetos-perdidos",
        "cefrLevel": "A2",
        "title": "En la Oficina de Objetos Perdidos",
        "titleEn": "At the Lost and Found Office",
        "situation": "Olvidaste tu mochila en el autobús y acudes a la oficina de atención para recuperarla.",
        "situationEn": "You forgot your backpack on the bus and go to the service office to recover it.",
        "roleplay": {
            "interlocutorRole": "Oficial de Atención al Cliente",
            "interlocutorRoleEn": "Customer Service Officer",
            "learnerRole": "Pasajero",
            "learnerRoleEn": "Passenger",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can report a lost item, describe physical features and contents, and leave contact details",
        "targetSkills": ["describing_objects", "narrating_past_events", "giving_contact_info"],
        "unitIds": ["unit.a2.11", "unit.a2.14"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenos días. Dígame, ¿ha extraviado alguna pertenencia en el transporte público?",
                "interlocutorTranslation": "Good morning. Tell me, have you misplaced a belonging on public transit?",
                "learnerCue": "Explica que dejaste tu mochila en el autobús número 27 esta mañana.",
                "learnerCueEn": "Explain that you left your backpack on bus number 27 this morning.",
                "vocabularyHints": [
                    "he perdido mi mochila — I have lost my backpack",
                    "la olvidé en el autobús — I forgot it on the bus",
                    "esta mañana — this morning",
                    "línea veintisiete — line 27"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["mochila", "olvidé", "perdí", "autobús", "mañana", "línea"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¿Puede describir la mochila? ¿De qué color es y qué cosas importantes contiene?",
                "interlocutorTranslation": "Can you describe the backpack? What color is it and what important things does it contain?",
                "learnerCue": "Describe el color, tamaño y menciona que contiene un libro y unas gafas de sol.",
                "learnerCueEn": "Describe the color, size, and mention that it contains a book and sunglasses.",
                "vocabularyHints": [
                    "es negra y pequeña — it is black and small",
                    "de marca deportiva — sports brand",
                    "dentro hay un libro — inside there is a book",
                    "unas gafas de sol — sunglasses",
                    "un cargador — a charger"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["negra", "azul", "libro", "gafas", "contiene", "dentro", "pequeña"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Creo que el conductor entregó una similar hace media hora. Déjeme su nombre y número de teléfono para verificarla.",
                "interlocutorTranslation": "I think the driver handed in a similar one half an hour ago. Leave me your name and telephone number to verify it.",
                "learnerCue": "Proporciona tu nombre y número de teléfono y agradece la ayuda.",
                "learnerCueEn": "Provide your name and phone number and thank them for the help.",
                "vocabularyHints": [
                    "mi nombre es... — my name is...",
                    "mi número de teléfono es... — my phone number is...",
                    "muchísimas gracias — thank you very much",
                    "es un gran alivio — it's a great relief"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["nombre", "teléfono", "número", "gracias", "alivio"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc07-restaurante-alergia",
        "cefrLevel": "A2",
        "title": "Pidiendo con Alergias Alimentarias",
        "titleEn": "Ordering with Food Allergies",
        "situation": "Estás en un restaurante y tienes intolerancia al gluten y alergia a los frutos secos.",
        "situationEn": "You are at a restaurant and have gluten intolerance and nut allergy.",
        "roleplay": {
            "interlocutorRole": "Camarero / Camarera",
            "interlocutorRoleEn": "Waiter / Waitress",
            "learnerRole": "Cliente con Alergia",
            "learnerRoleEn": "Diner with Allergies",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can explain dietary restrictions and food allergies, and verify ingredients in a meal",
        "targetSkills": ["food_safety", "clarifying_ingredients", "polite_requests"],
        "unitIds": ["unit.a2.04", "unit.a2.26"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenas tardes. ¿Están listos para ordenar o desean alguna recomendación del chef?",
                "interlocutorTranslation": "Good afternoon. Are you ready to order or would you like a chef recommendation?",
                "learnerCue": "Explica que tienes alergia a los frutos secos y que no puedes comer gluten.",
                "learnerCueEn": "Explain that you have a nut allergy and cannot eat gluten.",
                "vocabularyHints": [
                    "tengo alergia a... — I have an allergy to...",
                    "los frutos secos — nuts",
                    "no puedo comer gluten — I cannot eat gluten",
                    "¿Tienen opciones sin gluten? — Do you have gluten-free options?"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["alergia", "gluten", "frutos secos", "intolerancia", "puedo", "comer"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Por supuesto, nos tomamos las alergias muy en serio. El pescado al horno con patatas no contiene nada de gluten ni nueces. ¿Le apetece ese plato?",
                "interlocutorTranslation": "Of course, we take allergies very seriously. The baked fish with potatoes contains no gluten or nuts. Would you like that dish?",
                "learnerCue": "Acepta el pescado y pregunta si la salsa lleva harina o trigo.",
                "learnerCueEn": "Accept the fish and ask if the sauce contains flour or wheat.",
                "vocabularyHints": [
                    "me parece muy bien — sounds great to me",
                    "¿La salsa lleva harina? — Does the sauce contain flour?",
                    "solo con aceite de oliva — just with olive oil",
                    "por precaución — as a precaution"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["pescado", "salsa", "harina", "trigo", "lleva", "perfecto"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "La salsa es únicamente de limón y aceite de oliva virgen. Le informaré a la cocina inmediatamente.",
                "interlocutorTranslation": "The sauce is only lemon and virgin olive oil. I will notify the kitchen immediately.",
                "learnerCue": "Agradece la atención y confirma el pedido.",
                "learnerCueEn": "Thank them for their attention and confirm the order.",
                "vocabularyHints": [
                    "muchas gracias por confirmar — thank you very much for confirming",
                    "se lo agradezco mucho — I appreciate it very much",
                    "entonces pido ese plato — then I'll order that dish"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "atención", "agradezco", "plato", "cocina"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc08-invitacion-cena",
        "cefrLevel": "A2",
        "title": "Visita a Casa de un Amigo",
        "titleEn": "Visiting a Friend's Home",
        "situation": "Has sido invitado a cenar a casa de un amigo local y llegas con un detalle.",
        "situationEn": "You have been invited to dinner at a local friend's home and you arrive with a small gift.",
        "roleplay": {
            "interlocutorRole": "Anfitrión / Amigo",
            "interlocutorRoleEn": "Host / Friend",
            "learnerRole": "Invitado",
            "learnerRoleEn": "Guest",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can perform social pleasantries as a houseguest, offer compliments, and offer help",
        "targetSkills": ["social_courtesy", "complimenting", "offering_assistance"],
        "unitIds": ["unit.a2.08", "unit.a2.09"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Hola! ¡Pasa adelante! Qué alegría verte, bienvenido a mi casa.",
                "interlocutorTranslation": "Hello! Come on in! Great to see you, welcome to my home.",
                "learnerCue": "Saluda calurosamente, elogia la casa y entrega un detalle (dulces o flores).",
                "learnerCueEn": "Greet warmly, compliment the home, and hand over a small gift (sweets or flowers).",
                "vocabularyHints": [
                    "gracias por invitarme — thanks for inviting me",
                    "tienes una casa preciosa — you have a lovely home",
                    "te he traído esto — I brought you this",
                    "un detalle para la cena — a small treat for dinner"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["gracias", "invitarme", "casa", "bonita", "traído", "flores", "postre"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¡Muchas gracias, qué detalle tan amable! Siéntate en el salón. ¿Cómo ha ido tu semana en el trabajo?",
                "interlocutorTranslation": "Thank you so much, what a thoughtful gesture! Sit down in the living room. How was your week at work?",
                "learnerCue": "Cuenta brevemente que tuviste una semana ocupada pero interesante.",
                "learnerCueEn": "Briefly share that you had a busy but interesting week.",
                "vocabularyHints": [
                    "bastante ocupada — quite busy",
                    "muchas reuniones — many meetings",
                    "pero todo bien — but all good",
                    "con ganas de descansar — looking forward to relaxing"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["semana", "ocupada", "trabajo", "bien", "interesante", "cansado", "tiempo"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "La cena ya casi está lista, preparé una paella de verduras. ¿Te apetece una copa de vino o agua?",
                "interlocutorTranslation": "Dinner is almost ready, I made a vegetable paella. Would you like a glass of wine or water?",
                "learnerCue": "Elige tu bebida y ofrécete a ayudar a poner la mesa.",
                "learnerCueEn": "Choose your drink and offer to help set the table.",
                "vocabularyHints": [
                    "una copa de vino blanco — a glass of white wine",
                    "agua fresca, por favor — fresh water, please",
                    "¿te ayudo a poner la mesa? — can I help set the table?",
                    "huele delicioso — smells delicious"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["vino", "agua", "ayudo", "poner", "mesa", "huele", "delicioso"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc09-cambio-talla",
        "cefrLevel": "A2",
        "title": "Cambiando un Producto en la Tienda",
        "titleEn": "Exchanging an Item at a Store",
        "situation": "Compraste un jersey hace dos días pero te queda demasiado pequeño y quieres cambiarlo.",
        "situationEn": "You bought a sweater two days ago but it is too small and you want to exchange it.",
        "roleplay": {
            "interlocutorRole": "Dependiente de Devoluciones",
            "interlocutorRoleEn": "Customer Returns Clerk",
            "learnerRole": "Cliente",
            "learnerRoleEn": "Customer",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can explain a product issue, present proof of purchase, and request a size exchange",
        "targetSkills": ["returns_and_exchanges", "explaining_defects", "consumer_interaction"],
        "unitIds": ["unit.a2.15", "unit.a2.25"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenas tardes. ¿Viene a realizar un cambio o una devolución?",
                "interlocutorTranslation": "Good afternoon. Are you here for an exchange or a refund?",
                "learnerCue": "Explica que compraste un jersey hace dos días y necesitas cambiarlo por una talla más grande.",
                "learnerCueEn": "Explain that you bought a sweater two days ago and need to exchange it for a larger size.",
                "vocabularyHints": [
                    "quisiera cambiar este jersey — I would like to exchange this sweater",
                    "me queda muy pequeño — it fits me too small",
                    "necesito una talla más grande — I need a larger size",
                    "lo compré hace dos días — I bought it two days ago"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["cambiar", "jersey", "talla", "pequeño", "grande", "compré"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Sin problema. ¿Conserva el ticket de compra y la etiqueta original de la prenda?",
                "interlocutorTranslation": "No problem. Do you keep the receipt and the original tag on the garment?",
                "learnerCue": "Di que sí y entrega el ticket de compra.",
                "learnerCueEn": "Say yes and hand over the purchase receipt.",
                "vocabularyHints": [
                    "sí, aquí tiene el ticket — yes, here is the receipt",
                    "la etiqueta está intacta — the tag is intact",
                    "no lo he usado — I have not worn it"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["ticket", "etiqueta", "aquí", "tiene", "sí", "factura"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Perfecto, todo en orden. Ya le traigo la talla grande del almacén... Aquí la tiene. ¿Desea algo más?",
                "interlocutorTranslation": "Perfect, everything in order. I'll fetch the large size from the stockroom... Here you go. Anything else?",
                "learnerCue": "Agradece la gestión y despídete amablemente.",
                "learnerCueEn": "Thank them for their help and say goodbye politely.",
                "vocabularyHints": [
                    "muchas gracias por la atención — thank you very much for your assistance",
                    "ha sido muy rápido — that was very fast",
                    "que tenga un buen día — have a good day"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["gracias", "atención", "buen día", "perfecto", "luego"]
                }
            }
        ]
    },
    {
        "id": "es-a2-sc10-clase-espanol",
        "cefrLevel": "A2",
        "title": "Hablando de Experiencias en Clase",
        "titleEn": "Talking About Language Learning",
        "situation": "Estás en tu primer día de curso de idiomas y conversas con tu nuevo profesor sobre tu aprendizaje.",
        "situationEn": "You are on your first day of a language course and chat with your new teacher about your learning.",
        "roleplay": {
            "interlocutorRole": "Profesor / Profesora de Español",
            "interlocutorRoleEn": "Spanish Teacher",
            "learnerRole": "Estudiante",
            "learnerRoleEn": "Student",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can talk about language learning background, duration, strengths, and goals",
        "targetSkills": ["describing_learning", "expressing_goals", "talking_about_time"],
        "unitIds": ["unit.a2.09", "unit.a2.29"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¡Bienvenido a la clase! Cuéntame, ¿cuánto tiempo llevas estudiando español y por qué decidiste aprenderlo?",
                "interlocutorTranslation": "Welcome to class! Tell me, how long have you been studying Spanish and why did you decide to learn it?",
                "learnerCue": "Di cuánto tiempo llevas estudiando (meses o años) y tu motivo principal.",
                "learnerCueEn": "Say how long you have been studying (months or years) and your main reason.",
                "vocabularyHints": [
                    "llevo seis meses estudiando — I've been studying for six months",
                    "empecé el año pasado — I started last year",
                    "porque me encanta viajar — because I love traveling",
                    "por motivos de trabajo — for work reasons"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["estudiando", "meses", "año", "tiempo", "viajar", "trabajo", "porque"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¡Estupendo! Y en tu opinión, ¿qué aspecto del idioma te resulta más fácil y cuál te cuesta más trabajo?",
                "interlocutorTranslation": "Great! And in your opinion, what aspect of the language do you find easiest and what is hardest?",
                "learnerCue": "Explica que la lectura es más fácil pero hablar o entender audios rápidos es más difícil.",
                "learnerCueEn": "Explain that reading is easier but speaking or understanding fast audios is harder.",
                "vocabularyHints": [
                    "la lectura es bastante fácil — reading is quite easy",
                    "la gramática me resulta sencilla — grammar is simple to me",
                    "me cuesta hablar con fluidez — speaking fluently is difficult for me",
                    "entender a los nativos — understanding native speakers"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["fácil", "difícil", "cuesta", "hablar", "escuchar", "leer", "gramática"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Es completamente normal, por eso practicaremos mucha conversación aquí. ¿Cuál es tu meta para este curso?",
                "interlocutorTranslation": "That is completely normal, which is why we will practice plenty of conversation here. What is your goal for this course?",
                "learnerCue": "Di que tu objetivo es sentirte más seguro hablando y aprobar el examen A2.",
                "learnerCueEn": "Say your goal is to feel more confident speaking and pass the A2 exam.",
                "vocabularyHints": [
                    "mi meta principal es... — my main goal is...",
                    "tener más seguridad al hablar — to have more confidence speaking",
                    "aprobar el examen — to pass the exam",
                    "comunicarme sin miedo — to communicate without fear"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["meta", "objetivo", "hablar", "seguridad", "examen", "mejorar"]
                }
            }
        ]
    },

    # -------------------------------------------------------------
    # B1 SCENARIOS (10 - Target Language Only)
    # -------------------------------------------------------------
    {
        "id": "es-b1-sc01-medico",
        "cefrLevel": "B1",
        "title": "Consulta Médica",
        "situation": "Estás de viaje en Buenos Aires y no te encuentras bien, por lo que acudes a una consulta médica para explicar tus síntomas.",
        "roleplay": {
            "interlocutorRole": "Médico / Doctora",
            "learnerRole": "Paciente",
            "interlocutorVoice": "es-AR"
        },
        "targetCompetency": "I can describe health symptoms, duration, and ask medical advice",
        "targetSkills": ["describing_illness", "past_experience", "following_medical_advice"],
        "unitIds": ["unit.b1.core.09", "unit.a1.20"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Pase, por favor, tome asiento. Cuénteme, ¿qué síntomas tiene y desde cuándo se siente mal?",
                "interlocutorTranslation": "Come in please, take a seat. Tell me, what symptoms do you have and since when have you been feeling unwell?",
                "learnerCue": "Explica que tienes fiebre, dolor de cabeza y de garganta desde hace dos días.",
                "vocabularyHints": [
                    "desde hace dos días — for two days",
                    "tengo fiebre alta — I have a high fever",
                    "dolor de cabeza — headache",
                    "me duele la garganta — my throat hurts",
                    "al tragar — when swallowing"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["fiebre", "dolor", "cabeza", "garganta", "días", "siento", "duele", "mal", "tengo"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Entiendo. Voy a examinarle la garganta y tomarle la temperatura... Sí, tiene la garganta bastante inflamada y 38 grados. ¿Tiene alguna alergia a medicamentos como la penicilina?",
                "interlocutorTranslation": "I see. I will examine your throat and take your temperature... Yes, your throat is quite swollen and you have 38 degrees. Do you have any allergies to medications like penicillin?",
                "learnerCue": "Responde que no tienes ninguna alergia conocida y pregunta si es necesario tomar antibióticos o solo analgésicos.",
                "vocabularyHints": [
                    "ninguna alergia que yo sepa — no allergies that I know of",
                    "¿Cree que necesito...? — Do you think I need...?",
                    "antibióticos — antibiotics",
                    "será suficiente con... — will it be enough with...",
                    "analgésicos — painkillers"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["no", "alergia", "penicilina", "antibiótico", "medicamento", "tomar", "analgésico", "pastillas"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Por ahora es un cuadro viral, así que le recetaré ibuprofeno cada ocho horas y mucho reposo. Si no mejora en cuarenta y ocho horas, vuelva a la clínica.",
                "interlocutorTranslation": "For now it is viral, so I will prescribe ibuprofen every eight hours and plenty of rest. If you don't improve in forty-eight hours, return to the clinic.",
                "learnerCue": "Aclara si debes tomar la medicación con las comidas y agradece las recomendaciones al médico.",
                "vocabularyHints": [
                    "comprendido — understood",
                    "¿Debo tomar...? — Should I take...?",
                    "antes o después de comer — before or after eating",
                    "muchas gracias — thank you very much",
                    "por su atención — for your attention"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["comida", "comer", "antes", "después", "gracias", "atención", "tomar", "ibuprofeno"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc02-alquiler-piso",
        "cefrLevel": "B1",
        "title": "Negociación del Alquiler de un Piso",
        "situation": "Visitas un apartamento en alquiler en Bogotá y conversas con el propietario sobre las condiciones del contrato y servicios.",
        "roleplay": {
            "interlocutorRole": "Propietario / Arrendador",
            "learnerRole": "Inquilino Interesado",
            "interlocutorVoice": "es-CO"
        },
        "targetCompetency": "I can enquire about housing lease terms, utility costs, and negotiate contract details",
        "targetSkills": ["housing_negotiation", "clarifying_conditions", "asking_details"],
        "unitIds": ["unit.b1.core.10"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenas tardes. Como ve, el apartamento tiene excelente iluminación natural y dos habitaciones. ¿Qué le parece la distribución?",
                "interlocutorTranslation": "Good afternoon. As you can see, the apartment has excellent natural lighting and two bedrooms. What do you think of the layout?",
                "learnerCue": "Elogia el espacio pero pregunta si los gastos de agua, luz e internet están incluidos en el precio del arriendo.",
                "vocabularyHints": [
                    "me parece muy luminoso — it seems very bright to me",
                    "los gastos comunitarios — community expenses",
                    "servicios incluidos — utilities included",
                    "¿cuánto se paga de media? — how much is paid on average?"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["precio", "arriendo", "alquiler", "servicios", "luz", "agua", "internet", "incluidos"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Los servicios públicos se pagan aparte según consumo. El contrato mínimo es de un año y pedimos dos meses de fianza o depósito.",
                "interlocutorTranslation": "Utilities are paid separately according to consumption. The minimum contract is one year and we require a two-month deposit.",
                "learnerCue": "Pregunta si el contrato admite cancelación anticipada en caso de traslado laboral y si se permiten mascotas.",
                "vocabularyHints": [
                    "en caso de traslado laboral — in case of job transfer",
                    "cancelación anticipada — early termination",
                    "¿Se permiten mascotas? — Are pets allowed?",
                    "con previo aviso — with prior notice"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["contrato", "aviso", "mascotas", "trabajo", "fianza", "meses", "posible"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Con aviso previo de un mes no habría penalización. Si le interesa, podemos revisar la documentación este viernes.",
                "interlocutorTranslation": "With a one-month prior notice there would be no penalty. If you are interested, we can review the documents this Friday.",
                "learnerCue": "Acepta la propuesta, confirma qué documentos necesitas llevar y agradece la visita.",
                "vocabularyHints": [
                    "me interesa mucho — I am very interested",
                    "¿Qué documentos debo aportar? — What documents must I provide?",
                    "nómina o comprobante de ingresos — payslip or proof of income",
                    "el viernes nos vemos — see you on Friday"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["documentos", "viernes", "interesa", "nómina", "gracias", "visita"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc03-entrevista-trabajo",
        "cefrLevel": "B1",
        "title": "Entrevista de Trabajo",
        "situation": "Te presentas a una entrevista para un puesto de coordinador de proyectos en una empresa internacional en Santiago de Chile.",
        "roleplay": {
            "interlocutorRole": "Entrevistador de Recursos Humanos",
            "learnerRole": "Candidato",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can summarize work experience, discuss professional strengths, and answer interview questions",
        "targetSkills": ["professional_presentation", "career_narrative", "strengths_and_goals"],
        "unitIds": ["unit.b1.core.06", "unit.b1.core.26"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Bienvenido a nuestra empresa. Hemos revisado su currículum con interés. Para comenzar, ¿podría resumir su experiencia laboral previa?",
                "interlocutorTranslation": "Welcome to our company. We reviewed your CV with interest. To start, could you summarize your previous work experience?",
                "learnerCue": "Resume que has trabajado durante tres años coordinando proyectos y gestionando equipos multiculturales.",
                "vocabularyHints": [
                    "durante los últimos tres años — over the last three years",
                    "he trabajado como coordinador — I have worked as coordinator",
                    "gestión de equipos — team management",
                    "entornos multiculturales — multicultural environments"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["años", "experiencia", "trabajado", "proyectos", "equipos", "empresa", "gestión"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Muy interesante. Este puesto exige resolver situaciones imprevistas con rapidez. ¿Cómo suele manejar la presión en momentos de entrega crítica?",
                "interlocutorTranslation": "Very interesting. This position requires resolving unforeseen situations quickly. How do you usually handle pressure during critical deadlines?",
                "learnerCue": "Explica que priorizas las tareas esenciales, mantienes una comunicación transparente y buscas soluciones prácticas.",
                "vocabularyHints": [
                    "suelo priorizar las tareas clave — I usually prioritize key tasks",
                    "comunicación constante — constant communication",
                    "mantener la calma — to stay calm",
                    "encontrar soluciones eficientes — to find efficient solutions"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["presión", "priorizo", "tareas", "comunicación", "equipo", "soluciones", "calma"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Excelente enfoque. Por último, ¿por qué le motiva incorporarse específicamente a nuestro proyecto?",
                "interlocutorTranslation": "Excellent approach. Lastly, why does joining our project specifically motivate you?",
                "learnerCue": "Menciona que admiras el compromiso de la empresa con la innovación y que buscas crecer profesionalmente.",
                "vocabularyHints": [
                    "admiro su trayectoria en... — I admire your track record in...",
                    "innovación y sostenibilidad — innovation and sustainability",
                    "crecimiento profesional — professional growth",
                    "aportar mis competencias — contribute my skills"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["empresa", "innovación", "crecer", "motiva", "aportar", "oportunidad"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc04-reclamacion-vuelo",
        "cefrLevel": "B1",
        "title": "Reclamación por Vuelo Cancelado",
        "situation": "Tu vuelo de conexión en el aeropuerto de Barajas ha sido cancelado debido a problemas técnicos de la aerolínea.",
        "roleplay": {
            "interlocutorRole": "Agente de la Aerolínea",
            "learnerRole": "Pasajero Afectado",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can express dissatisfaction with a service disruption, demand alternatives, and claim compensation",
        "targetSkills": ["complaints_and_rights", "problem_resolution", "formal_demands"],
        "unitIds": ["unit.b1.core.08", "unit.b1.core.20"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Atención al pasajero, buenas tardes. ¿En qué le puedo asistir con su billete?",
                "interlocutorTranslation": "Passenger service, good afternoon. How can I assist you with your ticket?",
                "learnerCue": "Explica que tu vuelo a Roma fue cancelado sin aviso previo y que perdiste una conexión importante.",
                "vocabularyHints": [
                    "mi vuelo ha sido cancelado — my flight has been cancelled",
                    "sin aviso previo — without prior notice",
                    "he perdido mi conexión — I have lost my connection",
                    "exijo una solución urgente — I demand an urgent solution"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["vuelo", "cancelado", "conexión", "aviso", "roma", "urgente", "solución"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Comprendo su malestar. El próximo vuelo con asientos disponibles saldrá mañana a las ocho de la mañana.",
                "interlocutorTranslation": "I understand your distress. The next flight with available seats leaves tomorrow at eight in the morning.",
                "learnerCue": "Acepta el vuelo pero exige alojamiento en un hotel cercano y vales para cenar y desayunar.",
                "vocabularyHints": [
                    "acepto el vuelo de mañana — I accept tomorrow's flight",
                    "la aerolínea debe cubrir — the airline must cover",
                    "alojamiento en hotel — hotel accommodation",
                    "vales de comida — meal vouchers"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["mañana", "hotel", "noche", "comida", "vales", "gastos", "cubrir"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Efectivamente, le corresponde un bono de hotel con transporte y dos vales de comida. Aquí tiene sus tarjetas de embarque.",
                "interlocutorTranslation": "Indeed, you are entitled to a hotel voucher with transport and two meal vouchers. Here are your boarding passes.",
                "learnerCue": "Solicita una constancia escrita de la cancelación para solicitar indemnización según los derechos del pasajero.",
                "vocabularyHints": [
                    "necesito una constancia escrita — I need written proof",
                    "motivo de la cancelación — reason for cancellation",
                    "reclamar indemnización — claim compensation",
                    "derechos del pasajero — passenger rights"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["constancia", "documento", "indemnización", "escrito", "derechos", "gracias"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc05-debate-medioambiente",
        "cefrLevel": "B1",
        "title": "Debate sobre Hábitos y Medio Ambiente",
        "situation": "Participas en una mesa redonda universitaria sobre cómo reducir el impacto ecológico en las grandes urbes.",
        "roleplay": {
            "interlocutorRole": "Moderador / Compañero de Mesa",
            "learnerRole": "Participante",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can express opinions, provide arguments on environmental issues, and respond to counterarguments",
        "targetSkills": ["expressing_opinions", "debating", "environmental_issues"],
        "unitIds": ["unit.b1.core.16", "unit.b1.core.21"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¿Considera usted que prohibir los coches contaminantes en los centros urbanos es la medida más eficaz para frenar las emisiones?",
                "interlocutorTranslation": "Do you consider that banning polluting cars in urban centers is the most effective measure to curb emissions?",
                "learnerCue": "Opina que es una medida necesaria pero insuficiente si no se abarata y moderniza el transporte público.",
                "vocabularyHints": [
                    "en mi opinión es una medida necesaria — in my opinion it is a necessary measure",
                    "pero resulta insuficiente — but it turns out insufficient",
                    "fomentar el transporte público — encourage public transit",
                    "precios asequibles — affordable prices"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["opinión", "medida", "transporte", "público", "insuficiente", "precio", "coches"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Algunos críticos sostienen que esas restricciones perjudican económicamente a las familias de ingresos modestos. ¿Qué opina?",
                "interlocutorTranslation": "Some critics argue that those restrictions economically harm low-income families. What do you think?",
                "learnerCue": "Argumenta que el gobierno debe otorgar subsidios para vehículos limpios y alternativas gratuitas de movilidad.",
                "vocabularyHints": [
                    "entiendo ese punto de vista — I understand that viewpoint",
                    "subsidios estatales — state subsidies",
                    "evitar la desigualdad — avoid inequality",
                    "transición justa — just transition"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["familias", "ayudas", "subsidios", "gobierno", "justo", "desigualdad", "apoyo"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Para concluir, ¿qué cambio de hábito individual cree que tiene mayor repercusión en la vida cotidiana?",
                "interlocutorTranslation": "To conclude, what individual lifestyle change do you think has the biggest impact in daily life?",
                "learnerCue": "Destaca reducir el consumo de plásticos de un solo uso y elegir productos locales de temporada.",
                "vocabularyHints": [
                    "a nivel personal considero clave — on a personal level I consider key",
                    "reducir el plástico de un solo uso — reduce single-use plastic",
                    "consumir productos locales — consume local products",
                    "fomentar el consumo responsable — promote responsible consumption"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["plástico", "consumo", "locales", "reciclar", "responsable", "hábito"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc06-denuncia-policial",
        "cefrLevel": "B1",
        "title": "En la Comisaría: Denuncia por Hurto",
        "situation": "Acudes a una comisaría de policía en Ciudad de México para denunciar la sustracción de tu cartera en el metro.",
        "roleplay": {
            "interlocutorRole": "Oficial de Policía",
            "learnerRole": "Denunciante",
            "interlocutorVoice": "es-MX"
        },
        "targetCompetency": "I can narrate past events chronologically, describe suspects, and register an official report",
        "targetSkills": ["reporting_crimes", "past_narrative", "official_procedures"],
        "unitIds": ["unit.b1.core.28", "unit.b1.core.01"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenas tardes. Siéntese, por favor. ¿Qué suceso viene a denunciar?",
                "interlocutorTranslation": "Good afternoon. Please sit down. What incident are you here to report?",
                "learnerCue": "Relata que hace una hora en la estación de metro te sustrajeron la cartera del bolsillo.",
                "vocabularyHints": [
                    "vengo a interponer una denuncia — I come to file a complaint",
                    "me han robado la cartera — my wallet has been stolen",
                    "hace aproximadamente una hora — about an hour ago",
                    "en el andén del metro — on the subway platform"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["denuncia", "cartera", "metro", "robado", "bolsillo", "hora", "estación"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "¿Pudo ver a la persona o notó alguna actitud sospechosa a su alrededor?",
                "interlocutorTranslation": "Could you see the person or did you notice any suspicious behavior around you?",
                "learnerCue": "Explica que hubo un empujón al subir al vagón pero había demasiada multitud para ver quién fue.",
                "vocabularyHints": [
                    "hubo un forcejeo o empujón — there was a jostling or push",
                    "al entrar al vagón — when entering the train car",
                    "había mucha multitud — there was a huge crowd",
                    "no pude identificar al culpable — I couldn't identify the culprit"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["empujón", "multitud", "gente", "vagón", "persona", "ver", "sospechosa"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Entendido. ¿Qué documentos y tarjetas llevaba? Le generaré el acta oficial para que bloquee sus cuentas.",
                "interlocutorTranslation": "Understood. What documents and cards were inside? I will generate the official statement for you to block your accounts.",
                "learnerCue": "Detalla que llevabas el permiso de conducir, dos tarjetas de crédito y algo de efectivo, y pide una copia del acta.",
                "vocabularyHints": [
                    "llevaba mi permiso de conducir — I had my driver's license",
                    "dos tarjetas bancarias — two bank cards",
                    "sesenta euros en efectivo — sixty euros in cash",
                    "necesito una copia del acta para el seguro — I need a copy of the report for insurance"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["tarjetas", "permiso", "efectivo", "copia", "acta", "bloquear", "seguro"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc07-planificacion-viaje",
        "cefrLevel": "B1",
        "title": "Organizando un Viaje en Grupo",
        "situation": "Te reúnes con un amigo para planear un itinerario de viaje de dos semanas por Andalucía o el norte de España.",
        "roleplay": {
            "interlocutorRole": "Compañero de Viaje",
            "learnerRole": "Organizador",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can negotiate travel itineraries, weigh pros and cons of transport and accommodation, and manage budgets",
        "targetSkills": ["planning_travel", "weighing_options", "budget_negotiation"],
        "unitIds": ["unit.b1.core.08", "unit.b1.core.23"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "¿Qué prefieres: alquilar un coche para tener total libertad o movernos en tren de alta velocidad para no cansarnos conduciendo?",
                "interlocutorTranslation": "What do you prefer: renting a car to have total freedom or moving by high-speed train to avoid driving fatigue?",
                "learnerCue": "Soporta alquilar un coche porque permite visitar pueblos pequeños, aunque el tren sea más rápido.",
                "vocabularyHints": [
                    "el coche nos dará mayor flexibilidad — the car will give us more flexibility",
                    "visitar pueblos con encanto — visit charming villages",
                    "dividir los gastos de gasolina — split fuel expenses",
                    "aunque el tren sea cómodo — although the train is comfortable"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["coche", "tren", "alquilar", "libertad", "pueblos", "flexibilidad", "prefiero"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "De acuerdo con el coche. En cuanto al alojamiento, ¿reservamos hoteles céntricos o casas rurales con cocina para ahorrar?",
                "interlocutorTranslation": "Agreed on the car. As for lodging, should we book downtown hotels or countryside houses with kitchens to save money?",
                "learnerCue": "Propón combinar ambas opciones: casas rurales en el campo y un hotel sencillo en las ciudades grandes.",
                "vocabularyHints": [
                    "podríamos alternar ambas opciones — we could alternate both options",
                    "casas rurales para cocinar — country houses to cook",
                    "un hotel céntrico en la ciudad — a central hotel in the city",
                    "ahorrar dinero en comidas — save money on meals"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["hotel", "casas", "rurales", "cocina", "combinar", "ahorrar", "opciones"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Me parece un equilibrio perfecto. Yo me encargo de comparar los precios de los coches hoy mismo y tú revisas los alojamientos, ¿te parece?",
                "interlocutorTranslation": "Sounds like a perfect balance. I'll take care of comparing car prices today and you check accommodations, sounds good?",
                "learnerCue": "Acepta la división de tareas y fija una fecha límite para confirmar las reservas.",
                "vocabularyHints": [
                    "trato hecho — deal done",
                    "yo reviso los alojamientos disponibles — I'll review available lodgings",
                    "fijemos como límite el domingo — let's set Sunday as deadline",
                    "para no perder las mejores tarifas — to not miss best rates"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["acuerdo", "reviso", "alojamientos", "domingo", "reservas", "precios"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc08-cultura-cine",
        "cefrLevel": "B1",
        "title": "Intercambio Cultural: Recomendando Cine",
        "situation": "Participas en un café de idiomas y debates con un interlocutor nativo sobre películas hispanas destacadas.",
        "roleplay": {
            "interlocutorRole": "Interlocutor en Café de Idiomas",
            "learnerRole": "Aficionado al Cine",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can summarize plots, describe character motivations, and recommend artistic works enthusiastically",
        "targetSkills": ["describing_culture", "summarizing_plots", "expressing_emotions"],
        "unitIds": ["unit.b1.core.15", "unit.b1.core.30"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Estoy buscando una buena película en español para el fin de semana. ¿Hay alguna que te haya impresionado recientemente?",
                "interlocutorTranslation": "I am looking for a good movie in Spanish for the weekend. Is there one that impressed you recently?",
                "learnerCue": "Recomienda una película que te guste (como 'El laberinto del fauno' o 'Relatos Salvajes') y menciona su género.",
                "vocabularyHints": [
                    "te recomiendo sin duda — I definitely recommend",
                    "es una mezcla de fantasía y drama — it's a mix of fantasy and drama",
                    "una comedia negra brillante — a brilliant dark comedy",
                    "me impresionó la dirección — the direction impressed me"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["recomiendo", "película", "género", "drama", "historia", "obra", "gusta"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "He oído hablar de ella. ¿De qué trata la trama principal sin hacerme spoilers?",
                "interlocutorTranslation": "I've heard of it. What is the main plot about without giving me spoilers?",
                "learnerCue": "Resume el argumento principal y los dilemas morales a los que se enfrentan los personajes.",
                "vocabularyHints": [
                    "la trama se centra en... — the plot centers on...",
                    "los personajes deben afrontar — the characters must face",
                    "dilemas éticos y situaciones límite — ethical dilemmas and extreme situations",
                    "mantiene la tensión hasta el final — keeps tension until the end"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["trama", "historia", "personajes", "trata", "final", "conflicto"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Me has convencido por completo, la veré esta noche. ¿Crees que el cine hispano tiene una sensibilidad distinta al de Hollywood?",
                "interlocutorTranslation": "You've completely convinced me, I'll watch it tonight. Do you think Hispanic cinema has a different sensitivity compared to Hollywood?",
                "learnerCue": "Expresa que el cine hispano suele profundizar más en las relaciones humanas y la complejidad social.",
                "vocabularyHints": [
                    "a mi juicio profundiza más — in my judgment it delves deeper",
                    "relaciones humanas complejas — complex human relationships",
                    "un enfoque más realista y cercano — a more realistic and intimate approach",
                    "menos efectos especiales y más guion — fewer special effects and better script"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["cine", "social", "humanas", "realismo", "guion", "profundo", "sensibilidad"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc09-banco-cuenta",
        "cefrLevel": "B1",
        "title": "Apertura de Cuenta Bancaria",
        "situation": "Acudes a una sucursal bancaria en Madrid para abrir una cuenta para tu estancia de estudios o trabajo.",
        "roleplay": {
            "interlocutorRole": "Asesor Financiero",
            "learnerRole": "Cliente",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can enquire about banking conditions, fees, online services, and documentation requirements",
        "targetSkills": ["banking_transactions", "financial_terms", "official_enquiry"],
        "unitIds": ["unit.b1.core.19", "unit.b1.core.24"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Buenos días. Tome asiento. ¿Qué tipo de producto financiero o cuenta le gustaría contratar?",
                "interlocutorTranslation": "Good morning. Take a seat. What type of financial product or account would you like to open?",
                "learnerCue": "Explica que necesitas una cuenta corriente sin comisiones para domiciliar cobros y pagos cotidianos.",
                "vocabularyHints": [
                    "deseo abrir una cuenta corriente — I wish to open a checking account",
                    "sin comisiones de mantenimiento — without maintenance fees",
                    "domiciliar pagos y nómina — set up direct debits and payroll",
                    "tarjeta de débito asociada — associated debit card"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["cuenta", "corriente", "comisiones", "abrir", "pagos", "tarjeta", "nómina"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Nuestra cuenta joven para menores de 30 años no tiene comisiones e incluye banca móvil. ¿Dispone de su NIE o número de pasaporte?",
                "interlocutorTranslation": "Our young person account under 30 has no fees and includes mobile banking. Do you have your NIE or passport number?",
                "learnerCue": "Confirma que tienes tu pasaporte y comprobante de matrícula o contrato laboral.",
                "vocabularyHints": [
                    "aquí tengo mi pasaporte original — here is my original passport",
                    "mi número de identificación (NIE) — my identification number",
                    "comprobante de matrícula — proof of enrollment",
                    "contrato de trabajo — employment contract"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["pasaporte", "nie", "contrato", "matrícula", "documento", "aquí"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "La documentación es válida. En tres días hábiles recibirá su tarjeta en su domicilio. ¿Tiene alguna duda adicional sobre las transferencias?",
                "interlocutorTranslation": "The documentation is valid. In three business days you will receive your card at your address. Any additional questions about transfers?",
                "learnerCue": "Pregunta si las transferencias internacionales dentro de la Unión Europea tienen coste adicional.",
                "vocabularyHints": [
                    "¿Las transferencias internacionales tienen coste? — Do international transfers have a cost?",
                    "dentro de la zona euro — within the eurozone",
                    "límite diario en cajeros — daily ATM withdrawal limit",
                    "muchas gracias por la información — thank you very much for the information"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["transferencias", "internacionales", "coste", "comisión", "banca", "gracias"]
                }
            }
        ]
    },
    {
        "id": "es-b1-sc10-vecindario-reunion",
        "cefrLevel": "B1",
        "title": "Reunión de la Comunidad de Vecinos",
        "situation": "Participas en la reunión anual de propietarios de tu edificio para debatir reformas energéticas y normas de convivencia.",
        "roleplay": {
            "interlocutorRole": "Presidente de la Comunidad",
            "learnerRole": "Vecino Propietario",
            "interlocutorVoice": "es-ES"
        },
        "targetCompetency": "I can participate in community meetings, propose improvements, vote, and mediate disagreements",
        "targetSkills": ["civic_participation", "persuasion", "consensus_building"],
        "unitIds": ["unit.b1.core.11", "unit.b1.core.21"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "El siguiente punto del día es la propuesta de instalar paneles solares en la azotea comunitaria. ¿Cuál es su postura?",
                "interlocutorTranslation": "The next agenda item is the proposal to install solar panels on the shared rooftop. What is your position?",
                "learnerCue": "Manifiesta tu apoyo a la energía solar destacando el ahorro en la factura de la luz a medio plazo.",
                "vocabularyHints": [
                    "estoy totalmente a favor de la propuesta — I am completely in favor of the proposal",
                    "ahorro considerable en la factura eléctrica — considerable savings on electricity bill",
                    "inversión amortizable a medio plazo — investment amortized in the medium term",
                    "beneficio ecológico para el edificio — ecological benefit for the building"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["favor", "paneles", "energía", "ahorro", "factura", "medio plazo", "propuesta"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Varios vecinos temen que el coste inicial sea excesivo y requiera una cuota extraordinaria muy elevada.",
                "interlocutorTranslation": "Several neighbors fear that the initial cost may be excessive and require a very high special levy.",
                "learnerCue": "Propón solicitar subvenciones municipales para energías renovables y financiar el resto en plazos mensuales.",
                "vocabularyHints": [
                    "podríamos solicitar subvenciones públicas — we could apply for public grants",
                    "financiar el pago en plazos cómodos — finance payments in manageable installments",
                    "no representaría una carga económica — would not represent an economic burden",
                    "pedir presupuestos detallados — request detailed estimates"
                ],
                "validationCriteria": {
                    "minWords": 5,
                    "targetKeywords": ["subvenciones", "ayudas", "financiar", "plazos", "cuota", "coste", "presupuestos"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Parece una solución sensata y equilibrada. Si todos están conformes, someteremos a votación la búsqueda de presupuestos.",
                "interlocutorTranslation": "Sounds like a sensible and balanced solution. If everyone agrees, we will put the search for quotes to a vote.",
                "learnerCue": "Vota a favor y agradece que se haya escuchado tu propuesta constructiva.",
                "vocabularyHints": [
                    "voto a favor de someterlo a estudio — I vote in favor of putting it to study",
                    "gracias por considerar mi propuesta — thank you for considering my proposal",
                    "un acuerdo muy positivo para todos — a very positive agreement for all"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["voto", "favor", "acuerdo", "gracias", "propuesta", "comunidad"]
                }
            }
        ]
    }
]

HU_EXPANDED_SCENARIOS = [
    # -------------------------------------------------------------
    # HU A1 SCENARIOS (4)
    # -------------------------------------------------------------
    {
        "id": "hu-a1-sc01-kavezo",
        "cefrLevel": "A1",
        "title": "A Kávézóban",
        "titleEn": "In the Café",
        "situation": "Egy budapesti kávézóban vagy. Rendelni szeretnél egy kávét és süteményt, majd fizetni.",
        "situationEn": "You are in a café in Budapest. You would like to order a coffee and a pastry, and then pay.",
        "roleplay": {
            "interlocutorRole": "Pincér / Felszolgáló",
            "interlocutorRoleEn": "Waiter / Server",
            "learnerRole": "Vendég",
            "learnerRoleEn": "Guest / Customer",
            "interlocutorVoice": "hu-HU"
        },
        "targetCompetency": "I can order food and drink in a café and ask for the bill in Hungarian",
        "targetSkills": ["ordering_food", "polite_requests", "paying_bill"],
        "unitIds": ["unit.a1.23", "unit.a1.24"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Jó napot kívánok! Mit hozhatok Önnek?",
                "interlocutorTranslation": "Good day! What can I bring you?",
                "learnerCue": "Köszönj udvariasan, és kérj egy tejeskávét (cappuccinót) és egy croissant-t.",
                "learnerCueEn": "Greet politely, and ask for a white coffee (cappuccino) and a croissant.",
                "vocabularyHints": [
                    "egy tejeskávét — a white coffee (accusative)",
                    "egy croissant-t — a croissant (accusative)",
                    "kérek szépen — I'd like, please",
                    "jó napot kívánok — good day (formal greeting)"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["kávé", "tejeskávé", "cappuccino", "croissant", "kérek", "szépen", "jó napot"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Rendben van. Cukorral vagy cukor nélkül kéri a kávét? És hideg vagy meleg tejjel?",
                "interlocutorTranslation": "Alright. Do you take your coffee with sugar or without? And with cold or warm milk?",
                "learnerCue": "Mondd el, hogy cukor nélkül (vagy kevés cukorral) és meleg tejjel kéred.",
                "learnerCueEn": "Say that you would like it without sugar (or with a little sugar) and with warm milk.",
                "vocabularyHints": [
                    "cukor nélkül — without sugar",
                    "kevés cukorral — with a little sugar",
                    "meleg tejjel — with warm milk",
                    "kérem — please / I ask for it"
                ],
                "validationCriteria": {
                    "minWords": 2,
                    "targetKeywords": ["cukor", "nélkül", "cukorral", "meleg", "hideg", "tejjel", "kérem", "köszönöm"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Parancsoljon, itt van a tejeskávé és a sütemény. Kér még valamit?",
                "interlocutorTranslation": "Here you are, here is the white coffee and the pastry. Would you like anything else?",
                "learnerCue": "Köszönd meg, mondd, hogy nem kérsz mást, és kérd a számlát (kártyával szeretnél fizetni).",
                "learnerCueEn": "Say thank you, mention that you don't need anything else, and ask for the bill (wishing to pay by card).",
                "vocabularyHints": [
                    "köszönöm szépen — thank you very much",
                    "mást nem kérek — nothing else, thank you",
                    "a számlát kérem — the bill, please",
                    "kártyával fizetnék — I would like to pay by card"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["köszönöm", "számlát", "fizetni", "fizetnék", "kártyával", "készpénzzel", "nem"]
                }
            }
        ]
    },
    {
        "id": "hu-a1-sc02-bolt",
        "cefrLevel": "A1",
        "title": "A Boltban",
        "titleEn": "At the Grocery Store",
        "situation": "Egy élelmiszerboltban vásárolsz kenyeret és sajtot.",
        "situationEn": "You are at a grocery shop buying bread and cheese.",
        "roleplay": {
            "interlocutorRole": "Eladó",
            "interlocutorRoleEn": "Shop Assistant",
            "learnerRole": "Vásárló",
            "learnerRoleEn": "Customer",
            "interlocutorVoice": "hu-HU"
        },
        "targetCompetency": "I can buy basic food items, state quantities, and pay in Hungarian",
        "targetSkills": ["food_shopping", "numbers_and_prices", "polite_requests"],
        "unitIds": ["unit.a1.08", "unit.a1.09"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Jó napot! Miben segíthetek?",
                "interlocutorTranslation": "Good day! How can I help you?",
                "learnerCue": "Kérj egy fél kiló kenyeret és húsz deka sajtot.",
                "learnerCueEn": "Ask for half a kilo of bread and 200g of cheese.",
                "vocabularyHints": [
                    "fél kiló kenyér — half a kilo of bread",
                    "húsz deka sajt — 200g of cheese",
                    "kérek szépen — I'd like, please"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["kenyér", "kenyeret", "sajt", "sajtot", "kérek", "deka", "kiló"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Tessék, itt van. Kér még valamit esetleg?",
                "interlocutorTranslation": "Here you go. Would you like anything else perhaps?",
                "learnerCue": "Mondd, hogy nem kérsz mást, és kérdezd meg, mennyibe kerül.",
                "learnerCueEn": "Say nothing else, and ask how much it costs.",
                "vocabularyHints": [
                    "köszönöm, mást nem — thank you, nothing else",
                    "mennyibe kerül? — how much does it cost?",
                    "összesen — in total"
                ],
                "validationCriteria": {
                    "minWords": 2,
                    "targetKeywords": ["mást", "nem", "mennyibe", "kerül", "köszönöm"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Összesen ezerkétszáz forint lesz. Kártyával vagy készpénzzel fizet?",
                "interlocutorTranslation": "That will be 1,200 forints in total. Paying by card or cash?",
                "learnerCue": "Mondd, hogy készpénzzel vagy kártyával fizetsz, és köszönd meg.",
                "learnerCueEn": "State whether you are paying by cash or card, and say thank you.",
                "vocabularyHints": [
                    "készpénzzel fizetek — I pay with cash",
                    "kártyával — by card",
                    "tessék, itt van — here you go",
                    "viszontlátásra — goodbye"
                ],
                "validationCriteria": {
                    "minWords": 2,
                    "targetKeywords": ["kártya", "készpénz", "fizetek", "köszönöm", "tessék"]
                }
            }
        ]
    },

    # -------------------------------------------------------------
    # HU A2 SCENARIOS (4)
    # -------------------------------------------------------------
    {
        "id": "hu-a2-sc01-palyaudvar",
        "cefrLevel": "A2",
        "title": "A Pályaudvaron",
        "titleEn": "At the Train Station",
        "situation": "A budapesti Déli pályaudvaron vagy a jegypénztárnál, és Siófokra (Balaton) szeretnél vonatjegyet venni.",
        "situationEn": "You are at the ticket counter of Déli station in Budapest, and you want to buy a train ticket to Siófok (Lake Balaton).",
        "roleplay": {
            "interlocutorRole": "Jegypénztáros",
            "interlocutorRoleEn": "Ticket Clerk",
            "learnerRole": "Utas",
            "learnerRoleEn": "Passenger",
            "interlocutorVoice": "hu-HU"
        },
        "targetCompetency": "I can buy a train ticket, enquire about schedule and departure tracks in Hungarian",
        "targetSkills": ["travel_arrangements", "asking_timetable", "numbers_and_times"],
        "unitIds": ["unit.a2.14", "unit.a2.15"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Tessék, parancsoljon! Hova kéri a jegyet?",
                "interlocutorTranslation": "Yes please! Where would you like the ticket to?",
                "learnerCue": "Kérj egy retúr (oda-vissza) jegyet Siófokra a mai napra.",
                "learnerCueEn": "Ask for a round-trip ticket to Siófok for today.",
                "vocabularyHints": [
                    "egy oda-vissza jegyet — a round-trip ticket (accusative)",
                    "Siófokra — to Siófok",
                    "mára — for today",
                    "kérek szépen — please"
                ],
                "validationCriteria": {
                    "minWords": 4,
                    "targetKeywords": ["Siófok", "Siófokra", "jegy", "jegyet", "oda-vissza", "retúr", "kérek", "mára"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Van egy InterCity tíz óra húszkor és egy személyvonat tizenegykor. Az InterCityre helyjegy is kell. Melyikkel szeretne utazni?",
                "interlocutorTranslation": "There is an InterCity at 10:20 and a local train at 11:00. The InterCity also requires a seat reservation. Which one would you like to travel on?",
                "learnerCue": "Válaszd a tíz óra húszas járatot, és kérdezd meg, mikor érkezik Siófokra.",
                "learnerCueEn": "Choose the 10:20 train, and ask what time it arrives in Siófok.",
                "vocabularyHints": [
                    "az InterCityvel szeretnék — I would like with the InterCity",
                    "tíz óra húszkor — at 10:20",
                    "Mikor érkezik meg? — When does it arrive?",
                    "mennyi a menetidő? — how long is the travel time?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["tíz", "húsz", "InterCity", "mikor", "érkezik", "menetidő", "szeretnék"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "Pontosan tizenegy óra harminckor érkezik. Összesen háromezer-ötszáz forint lesz. Készpénz vagy bankkártya?",
                "interlocutorTranslation": "It arrives at exactly 11:30. That will be 3,500 forints in total. Cash or bank card?",
                "learnerCue": "Mondd, hogy kártyával fizetsz, és kérdezd meg, hányas vágányról indul a vonat.",
                "learnerCueEn": "Say that you will pay by card, and ask which track the train departs from.",
                "vocabularyHints": [
                    "bankkártyával fizetek — I pay by card",
                    "Hányas vágányról indul? — From which track does it depart?",
                    "köszönöm szépen — thank you very much"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["kártya", "bankkártya", "készpénz", "vágány", "vágányról", "indul", "köszönöm"]
                }
            }
        ]
    },
    {
        "id": "hu-a2-sc02-utbaigazitas",
        "cefrLevel": "A2",
        "title": "Útbaigazítás Kérése",
        "titleEn": "Asking for Directions",
        "situation": "A Deák téren vagy és keresed a Magyar Nemzeti Múzeumot.",
        "situationEn": "You are at Deák Square and looking for the Hungarian National Museum.",
        "roleplay": {
            "interlocutorRole": "Helyi járókelő",
            "interlocutorRoleEn": "Local passerby",
            "learnerRole": "Turista",
            "learnerRoleEn": "Tourist",
            "interlocutorVoice": "hu-HU"
        },
        "targetCompetency": "I can ask for and understand directional directions in Hungarian",
        "targetSkills": ["asking_directions", "spatial_orientation", "polite_enquiry"],
        "unitIds": ["unit.a2.05", "unit.a2.06"],
        "turns": [
            {
                "turnIndex": 1,
                "interlocutorPrompt": "Jó napot! Segíthetek valamiben?",
                "interlocutorTranslation": "Good day! Can I help with something?",
                "learnerCue": "Elnézést kérve kérdezd meg, merre van a Nemzeti Múzeum.",
                "learnerCueEn": "Excuse yourself and ask which way the National Museum is.",
                "vocabularyHints": [
                    "elnézést kívánok — excuse me",
                    "hol van a múzeum? — where is the museum?",
                    "merre kell menni? — which way should I go?",
                    "messze van? — is it far?"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["elnézést", "múzeum", "merre", "hol", "Nemzeti", "menni"]
                }
            },
            {
                "turnIndex": 2,
                "interlocutorPrompt": "Nincs messze, körülbelül tíz perc séta. Menjen egyenesen a Kálvin tér felé.",
                "interlocutorTranslation": "It's not far, about a ten-minute walk. Go straight towards Kálvin Square.",
                "learnerCue": "Kérdezd meg, hogy jobbra vagy balra kell-e fordulni a Kálvin téren.",
                "learnerCueEn": "Ask whether you need to turn right or left at Kálvin Square.",
                "vocabularyHints": [
                    "értem — I understand",
                    "jobbra vagy balra? — right or left?",
                    "kell fordulni — need to turn",
                    "a Kálvin téren — at Kálvin Square"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["jobbra", "balra", "fordulni", "Kálvin", "téren"]
                }
            },
            {
                "turnIndex": 3,
                "interlocutorPrompt": "A Kálvin téren menjen kissé balra a Múzeum körútra, és a bal oldalon meglátja az épületet.",
                "interlocutorTranslation": "At Kálvin Square go slightly to the left onto Múzeum Boulevard, and you will see the building on the left side.",
                "learnerCue": "Köszönd meg a segítséget és kívánj szép napot.",
                "learnerCueEn": "Thank them for the help and wish them a nice day.",
                "vocabularyHints": [
                    "nagyon köszönöm a segítséget — thank you very much for the help",
                    "szép napot kívánok — have a nice day",
                    "viszontlátásra — goodbye"
                ],
                "validationCriteria": {
                    "minWords": 3,
                    "targetKeywords": ["köszönöm", "segítséget", "szép", "napot", "viszontlátásra"]
                }
            }
        ]
    }
]

def main():
    root = Path(".")
    es_latam_path = root / "content" / "es-latam" / "conversation-scenarios.json"
    es_es_path = root / "content" / "es-es" / "conversation-scenarios.json"
    hu_path = root / "content" / "hu" / "conversation-scenarios.json"

    es_data = {
        "language": "es",
        "scenarios": ES_SCENARIOS
    }

    hu_data = {
        "language": "hu",
        "scenarios": HU_EXPANDED_SCENARIOS
    }

    print(f"Writing {len(ES_SCENARIOS)} scenarios to {es_latam_path}...")
    es_latam_path.write_text(json.dumps(es_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Writing {len(ES_SCENARIOS)} scenarios to {es_es_path}...")
    es_es_path.write_text(json.dumps(es_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Writing {len(HU_EXPANDED_SCENARIOS)} scenarios to {hu_path}...")
    hu_path.write_text(json.dumps(hu_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Done! Scenarios generated successfully.")

if __name__ == "__main__":
    main()
