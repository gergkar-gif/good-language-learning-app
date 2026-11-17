import sys
sys.path.insert(0,'/home/user/parlour-read-a/.scratch')
from lib import *
from u26 import U
def mk(title,scenario,prompt,cues,target,english,canDo):
    return {"tier":"tier1","level":"C1","title":"Communicative Challenge: "+title,"scenario":scenario,"prompt":prompt,"cues":cues,"target":target,"english":english,"canDo":canDo}
g=lambda i:U['lessons'][i]['goals'][0]
C={}
C['c1-mediaszabadsag-01']=mk('Népszabadság in 2016','In a history seminar you are asked why Népszabadság stopped appearing in 2016.','Say what the publisher stated and what the critics said.',['Give the publisher\'s statement','Give the critics\' view'],
 'A kiadó azt közölte, hogy a lap veszteséges volt, a bírálók viszont azt mondták, hogy politikai ok állt a háttérben.','The publisher stated that the paper was making a loss, but the critics said that there was a political reason behind it.',g(0))
C['c1-mediaszabadsag-02']=mk('Klubrádió in 2021','In a history seminar you are asked what happened to Klubrádió in February 2021.','Say what happened to the radio and what it did afterwards, with annak ellenére, hogy.',['Say that the radio ceased on the traditional airwaves','Say that it continued on the internet'],
 'Annak ellenére, hogy a Klubrádió 2021-ben megszűnt a hagyományos rádióhullámokon, az interneten folytatta a műsorszolgáltatást.','Although Klubrádió ceased on the traditional airwaves in 2021, it continued broadcasting on the internet.',g(1))
C['c1-mediaszabadsag-03']=mk('State Advertising','In a history seminar you are asked what the European Parliament thought of state advertising in 2018.','Say what the European Parliament called a cause for concern and what the critics said about the award.',['Name the object of the concern with a verbal noun','Give the critics\' view about the award'],
 'Az Európai Parlament 2018-as jelentése aggályosnak nevezte az állami hirdetések elosztását. A bírálók szerint az odaítélés nem volt átlátható.','The European Parliament\'s report of 2018 called the distribution of state advertisements a cause for concern. According to the critics, the award was not transparent.',g(2))
C['c1-mediaszabadsag-04']=mk('The Index in 2020','In a history seminar you are asked what happened to the Index editor-in-chief and where he went.','Say who was dismissed in 2020 and where he worked from 2021, with a past participle.',['Say who was dismissed','Say where he joined'],
 'Az elbocsátott főszerkesztő, Dull Szabolcs 2021 januárjában a Telexhez csatlakozott.','The dismissed editor-in-chief, Szabolcs Dull, joined the Telex in January 2021.',g(3))
C['c1-mediaszabadsag-05']=mk('The Sovereignty Protection Office','In a history seminar you are asked how the Sovereignty Protection Office was judged.','Set the government\'s view against the critics\' view, with ugyanakkor.',['Give the government\'s view','Add the critics\' contrasting view'],
 'A kormány szerint a hivatal a külföldi befolyásolás elleni védelmet szolgálta, a bírálók szerint ugyanakkor a független sajtó ellen is felhasználható volt.','According to the government the office served protection against foreign influence; at the same time, according to the critics it could also be used against the independent press.',g(4))
C['c1-mediaszabadsag-consolidation']=mk('The Period in Summary','At the end of the seminar you are asked to sum up the media events from 2016 to 2026.','Sum up the period briefly, with years and sources.',['Mention KESMA','Mention the Telex','Mention the election of 2026'],
 '2018-ban több mint négyszáz lap, rádió és televízió a KESMA-hoz került, a kormánypárti oldal szerint ez kiegyensúlyozta a médiapiacot, a bírálók szerint viszont veszélyeztette a sokszínűséget. 2020-ban megjelent a Telex. 2026. április 12-én a Tisza Párt kétharmados többséget szerzett.','In 2018 more than four hundred papers, radios and television channels went to KESMA; according to the pro-government side this balanced the media market, but according to the critics it endangered diversity. In 2020 the Telex appeared. On 12 April 2026 the Tisza Party won a two-thirds majority.',U['lessons'][5]['goals'][0])
dump('/home/user/parlour-read-a/challenges-media-capture.json',C)
