import sys
sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
from u27 import U
def mk(title,scenario,prompt,cues,target,english,canDo):
    return {"tier":"tier1","level":"C1","title":"Communicative Challenge: "+title,"scenario":scenario,"prompt":prompt,"cues":cues,"target":target,"english":english,"canDo":canDo}
g=lambda i:U['lessons'][i]['goals'][0]
C={}
C['c1-egeszsegugy-01']=mk("Doctors' Pay","In a history seminar you are asked how the Medical Chamber saw doctors' pay.","Say how the chamber compared Hungarian and Austrian pay, with képest.",['Name what the chamber compared','Say what it found'],
 'A kamara szerint az osztrák fizetésekhez képest alacsonyak voltak a magyar orvosi fizetések.',"According to the chamber, Hungarian doctors' pay was low compared with Austrian pay.",g(0))
C['c1-egeszsegugy-02']=mk('Hospital Debts in 2013','In a history seminar you are asked what happened in June 2013 between the hospitals and their suppliers.','Say what the hospitals did not do and what the suppliers did, with emiatt.',['Say what the hospitals owed','Say how the suppliers reacted'],
 'A kórházak nem fizették ki a számlákat, és emiatt harmincöt fő beszállító 2013 júniusában jelezte, hogy nem hajlandó tovább tűrni.','The hospitals did not pay the invoices, and because of this thirty-five main suppliers signalled in June 2013 that they were not willing to tolerate it any longer.',g(1))
C['c1-egeszsegugy-03']=mk('Nurses in 2021','In a history seminar you are asked what a survey showed about nurses in 2021.','Say what the survey showed, with során.',['Name the survey and its year','Say how many nurses were considering working abroad'],
 'A 2021-es felmérés során kiderült, hogy több mint ezer ápoló fontolgatta a külföldi munkavállalást.','The survey of 2021 showed that more than a thousand nurses were considering working abroad.',g(2))
C['c1-egeszsegugy-04']=mk('The Chamber Law of 2023','In a history seminar you are asked what was disputed about the law on the Medical Chamber.','Say what was disputed, with an indirect question.',['Say that the matter was disputed','Name the two views on the law'],
 'Vitatott volt, hogy a törvény az orvosokat védte-e, vagy a kamarát gyengítette.','It was disputed whether the law protected the doctors or weakened the chamber.',g(3))
C['c1-egeszsegugy-05']=mk('The Healthy Budapest Programme','In a history seminar you are asked how the government judged the Healthy Budapest Programme.','Give the government\'s view in spite of the delay, with ellenére.',['Mention the delay','Give the government\'s view'],
 'A késés ellenére a kormány szerint a program a fővárosi ellátás korszerűsítését szolgálta.','In spite of the delay, according to the government the programme served the modernisation of care in the capital.',g(4))
C['c1-egeszsegugy-consolidation']=mk('The Period in Summary','At the end of the seminar you are asked to sum up healthcare in Hungary from 2020 to 2026.','Sum up briefly, with years and sources.',['Mention the pay agreement','Mention the chamber law','Mention the election of 2026'],
 '2020 őszén a kormány és a kamara megállapodott az orvosok béremeléséről. 2023-ban az Országgyűlés megszüntette a kötelező kamarai tagságot. 2026. április 12-én a Tisza Párt kétharmados többséget szerzett.','In autumn 2020 the government and the chamber agreed on a pay rise for doctors. In 2023 the National Assembly abolished compulsory chamber membership. On 12 April 2026 the Tisza Party won a two-thirds majority.',U['lessons'][5]['goals'][0])
dump('/home/user/parlour-read-a/challenges-healthcare-crisis.json',C)
