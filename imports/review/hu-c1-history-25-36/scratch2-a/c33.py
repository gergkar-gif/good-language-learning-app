import sys; sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from u33 import U
from chal import write
items=[
("The National Core Curriculum","In a literature seminar you are asked about the National Core Curriculum of 2020.","Say when the new curriculum appeared and how its critics and the government judged it, naming the source.",["Give the date of the publication","Name the source of each view"],
 "2020. január 31-én megjelent az új Nemzeti alaptanterv. Írók, tanárok és tanári szervezetek szerint a kortárs szerzők háttérbe szorultak, a kormány szerint viszont a tanterv a magyar irodalmi örökség átadását szolgálta.",
 "On 31 January 2020 the new National Core Curriculum appeared. According to writers, teachers and teachers' organisations contemporary authors were pushed into the background; according to the government, however, the curriculum served the transmission of the Hungarian literary heritage."),
("The Textbook System","In a literature seminar you are asked how the supply of textbooks changed after 2011.","Say what the critics said compared with the earlier system and what the government said the aim was.",["Compare with the earlier system","Give the aim stated by the government"],
 "A bírálók szerint a korábbi rendszerhez képest szűkült a tanárok és az iskolák választási lehetősége. A kormány szerint a változás célja az volt, hogy a diákok ingyenesen jussanak tankönyvhöz.",
 "According to the critics, compared with the earlier system the freedom of choice of teachers and schools narrowed. According to the government, the aim of the change was that pupils should get textbooks free of charge."),
("Literary Institutions","In a literature seminar you are asked about the Petőfi Literary Museum.","Say who was appointed director-general in 2019 and what the critics said about the appointed leaders and the supported authors.",["Say who was appointed and when","Give the view of the critics"],
 "A Petőfi Irodalmi Múzeum főigazgatójává 2019-ben Demeter Szilárdot nevezték ki. A bírálók szerint a kinevezett vezetők és a támogatott szerzők köre a kormányhoz közel állókra szűkült.",
 "In 2019 Demeter Szilárd was appointed director-general of the Petőfi Literary Museum. According to the critics, the circle of the appointed leaders and the supported authors narrowed to those close to the government."),
("State and Independent Institutions","In a literature seminar you are asked how state and independent literary institutions differed.","Compare the Hungarian Academy of Arts with the Writers' Society within one sentence.",["Name what kind of body the Academy was","Name what kind of association the Writers' Society was"],
 "Míg a Magyar Művészeti Akadémia köztestület volt, a Szépírók Társasága önkéntes tagságú íróegyesületként működött. A Szépírók Társasága 1989-ben alakult.",
 "While the Hungarian Academy of Arts was a public body, the Writers' Society worked as a voluntary association of writers. The Writers' Society was founded in 1989."),
("Open Questions and Recent Events","At the end of the seminar you are asked what was left open and what happened in 2025.","Name one open question of the canon debate and say who received the Nobel Prize in Literature in 2025.",["State one question that was disputed","Say who received the Nobel Prize and when"],
 "Vitatott volt, hogy kell-e kötelező szerzők listáját előírni. 2025 októberében Krasznahorkai László kapta az irodalmi Nobel-díjat.",
 "It was disputed whether a list of compulsory authors should be prescribed. In October 2025 Krasznahorkai László received the Nobel Prize in Literature."),
("The Period in Summary","At the end of the seminar you are asked to sum up the period.","Sum up the period briefly, with years.",["Mention the curriculum of 2012","Mention the curriculum of 2020","Mention the election of 2026"],
 "2012-ben a kormány új Nemzeti alaptantervet fogadott el. 2020. január 31-én megjelent az új tanterv. 2026. április 12-én a Tisza Párt kétharmados többséget szerzett.",
 "In 2012 the government adopted a new National Core Curriculum. On 31 January 2020 the new curriculum appeared. On 12 April 2026 the Tisza Party won a two-thirds majority."),
]
write('/home/user/parlour-read-a/challenges-literary-canon.json','irodalmielet',U,items)
