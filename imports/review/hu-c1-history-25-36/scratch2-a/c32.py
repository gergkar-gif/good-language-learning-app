import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from u32 import U
from chal import write
items=[
("Retirement Age of Judges","In a history seminar you are asked what the new judicial laws required from judges.","Say what the rule required from judges from 2012 and how the government and its critics judged it.",["Say what judges were obliged to do","Name the source of each view"],
 "A hatvankettedik életévüket betöltött bírák kötelesek voltak nyugdíjba vonulni. A kormány indoklása szerint a korhatár a közszolgálat általános korhatárához igazodott, a bírálók szerint viszont sértette a bírák elmozdíthatatlanságának elvét.",
 "Judges who had reached the age of sixty-two were obliged to retire. According to the government's reasoning the age limit followed the general age limit of the civil service; according to the critics, however, it violated the principle of the irremovability of judges."),
("The National Judicial Office","In a history seminar you are asked about the powers of the president of the National Judicial Office.","Say who made the proposal for the appointment of judges and what the Constitutional Court did in July 2012.",["Say who made the proposal for appointments","Say what the Constitutional Court did in July 2012"],
 "A bírák kinevezésére az OBH elnöke tett javaslatot. 2012 júliusában az Alkotmánybíróság megsemmisítette az elnök ügyáthelyezési jogkörét.",
 "The president of the Office made the proposal for the appointment of judges. In July 2012 the Constitutional Court annulled the president's power to transfer cases."),
("Applications for Court Leadership","In a history seminar you are asked about the applications for leading posts in the courts.","Say what the president did although the judicial bodies had ranked the applicants, and what the National Judicial Council found in 2018.",["Set the president's decision against the ranking","Say what the Council found in 2018"],
 "Annak ellenére, hogy a bírói testületek rangsorolták a pályázókat, az elnök több pályázatot eredménytelennek nyilvánított. 2018-ban az OBT több határozatában megállapította, hogy az OBH elnöke megsértette a szabályokat.",
 "Although the judicial bodies had ranked the applicants, the president declared several applications unsuccessful. In 2018 the Council found in several resolutions that the president of the Office had broken the rules."),
("The Procedures of the Union","In a history seminar you are asked about the European procedures on the rule of law.","Say what the European Parliament decided on 12 September 2018 and what the Council decided during the conditionality procedure.",["Give the date and the decision of the Parliament","Say what the Council decided in December 2022"],
 "2018. szeptember 12-én az Európai Parlament határozatot fogadott el a hetedik cikk szerinti eljárásról. A feltételességi eljárás során a Tanács 2022 decemberében a források egy részének felfüggesztéséről döntött.",
 "On 12 September 2018 the European Parliament adopted a resolution on the procedure under Article 7. During the conditionality procedure the Council decided in December 2022 to suspend part of the funds."),
("The Amendments of 2023","In a history seminar you are asked what was stated about the amendments of 2023.","Report what the government stated about the amendments and what the Commission found in December 2023.",["Report the statement of the government","Report the finding of the Commission"],
 "A kormány azt közölte, hogy a módosítások az uniós feltételek teljesítését szolgálták. A Bizottság 2023 decemberében azt állapította meg, hogy a bírói függetlenséggel kapcsolatos feltételek teljesültek.",
 "The government stated that the amendments served the fulfilment of the Union's conditions. In December 2023 the Commission found that the conditions concerning judicial independence had been fulfilled."),
("The Period in Summary","At the end of the seminar you are asked to sum up the period.","Sum up the period briefly, with years and sources.",["Mention the judicial laws of 2011","Mention the ruling of the European Union's Court of Justice","Mention the election of 2026"],
 "2011-ben az Országgyűlés új törvényeket fogadott el a bíróságokról. Az Európai Unió Bírósága 2012 novemberében megállapította, hogy a korhatár csökkentése sértette az uniós szabályokat. 2026. május 9-én az Országgyűlés Magyar Pétert választotta miniszterelnökké.",
 "In 2011 the National Assembly adopted new laws on the courts. In November 2012 the Court of Justice of the European Union found that the lowering of the age limit violated the Union's rules. On 9 May 2026 the National Assembly elected Magyar Péter prime minister."),
]
write('/home/user/parlour-read-a/challenges-judicial-independence.json','biroifuggetlenseg',U,items)
