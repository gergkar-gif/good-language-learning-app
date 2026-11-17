import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from u31 import U
from chal import write
items=[
("The Memorial on Szabadság tér","In a history seminar you are asked what happened on Szabadság tér in 2014.","Put the events in order, and say how the government and its critics judged the memorial.",["Say what followed the start of construction","Name the source of each view"],
 "Miután 2014 júliusában megkezdődött az építés, tiltakozások kezdődtek. A kormány szerint az emlékmű a megszállás áldozataira emlékezett, a bírálók szerint viszont elfedte a magyar hatóságok felelősségét.",
 "After construction began in July 2014, protests began. According to the government the memorial commemorated the victims of the occupation; according to the critics, however, it concealed the responsibility of the Hungarian authorities."),
("The House of Terror Museum","In a history seminar you are asked about the House of Terror Museum.","Say when the museum opened and how its defenders and its critics judged the exhibition, naming the source.",["Give the date of the opening","Name the source of each view"],
 "A Terror Háza Múzeum 2002. február 24-én nyílt meg. A múzeum védői szerint a kiállítás két diktatúra áldozatainak adott emléket, a bírálók szerint viszont a hangsúly a kommunista korszakon volt.",
 "The House of Terror Museum opened on 24 February 2002. According to the museum's defenders the exhibition commemorated the victims of two dictatorships; according to the critics, however, the emphasis was on the communist period."),
("Nagy Imre","In a history seminar you are asked about the fate of Nagy Imre.","Say when Nagy Imre was executed and when the executed prime minister was reburied.",["Give the date of the execution","Give the date of the reburial"],
 "Nagy Imre miniszterelnököt 1958. június 16-án kivégezték. A kivégzett miniszterelnököt 1989. június 16-án újratemették.",
 "Prime minister Nagy Imre was executed on 16 June 1958. The executed prime minister was reburied on 16 June 1989."),
("Horthy Miklós","In a history seminar you are asked how Horthy Miklós has been judged.","Say how Horthy's supporters and how his critics judged him, setting the two views against each other.",["Give the view of the supporters","Give the view of the critics"],
 "Horthy támogatói szerint a kormányzó a konszolidáció jelképe volt. A bírálók szerint viszont felelősséget viselt a zsidóellenes törvényekért.",
 "According to Horthy's supporters the regent was a symbol of consolidation. According to the critics, however, he bore responsibility for the anti-Jewish laws."),
("Open Questions and the Election","At the end of the seminar you are asked what was left open and how the period ended.","Name one open question of memory politics and give the result of the election of 12 April 2026.",["State one question that was disputed","Give the result of the election"],
 "Vitatott volt, hogy kell-e a két diktatúrát egy kiállításon bemutatni. 2026. április 12-én a Tisza Párt a 199 mandátumból 141-et szerzett.",
 "It was disputed whether the two dictatorships should be shown in one exhibition. On 12 April 2026 the Tisza Party won 141 of the 199 seats."),
("The Period in Summary","At the end of the seminar you are asked to sum up the period.","Sum up the period briefly, with years and sources.",["Mention the memorial on Szabadság tér","Say how it was judged","Mention the election of 2026"],
 "2014 júliusában megkezdődött a Szabadság téri emlékmű építése. A kormány szerint az emlékmű a megszállás áldozataira emlékezett, a bírálók szerint viszont elfedte a hatóságok felelősségét. 2026. április 12-én a Tisza Párt kétharmados többséget szerzett.",
 "In July 2014 the construction of the memorial on Szabadság tér began. According to the government the memorial commemorated the victims of the occupation; according to the critics, however, it concealed the responsibility of the authorities. On 12 April 2026 the Tisza Party won a two-thirds majority."),
]
write('/home/user/parlour-read-a/challenges-historical-revisionism.json','emlekezetpolitika',U,items)
