#!/usr/bin/env python3
"""Generate Spain CCSE B1 Units 31, 32, and 33 (Empleo y Seguridad Social, Vivienda y Empadronamiento, Documentación y Registro Civil)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_es_b1_ccse_unit2_3 import emit_unit_from_dict


UNIT_31 = {
    "unit_num": 67,
    "slug": "empleo",
    "title": "Mercado Laboral y Seguridad Social",
    "theme": "Derechos laborales, Estatuto de los Trabajadores, contratos, Seguridad Social y prestaciones en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "El Estatuto de los Trabajadores, los contratos y la jornada laboral",
            "objective": "Conocer el marco legal de las relaciones laborales en España (Estatuto de los Trabajadores), la edad mínima para trabajar (16 años) y los derechos básicos.",
            "grammar_title": "Construcciones concesivas y de límite legal («a partir de los dieciséis años», «como máximo»)",
            "grammar_slug": "limites-legales-estatuto-trabajadores",
            "grammar_Body": """Para describir los derechos y límites legales del trabajo en España se usan locuciones preposicionales de límite (**a partir de, como máximo, como mínimo**) y pasivas reflejas:

- *En España **se puede trabajar legalmente a partir de los dieciséis años** (con autorización de los padres o tutores entre los 16 y los 18).*
- *La jornada laboral ordinaria es de **cuarenta horas semanales como máximo** de promedio anual y las vacaciones pagadas son de **treinta días naturales como mínimo** al año.*""",
            "story_title": "Derechos y garantías en el puesto de trabajo",
            "paragraphs": [
                "El artículo 35 de la Constitución Española reconoce que todos los españoles tienen el deber de trabajar y el derecho al trabajo, a la libre elección de profesión u oficio y a una remuneración suficiente sin que en ningún caso pueda hacerse discriminación por razón de sexo. La ley fundamental que desarrolla estos principios y regula las relaciones entre empresas y empleados asalariados es el Estatuto de los Trabajadores.",
                "De acuerdo con la legislación laboral española, la edad mínima legal para trabajar en España es de dieciséis años (16 años). No obstante, los menores de dieciocho años y mayores de dieciséis necesitan la autorización expresa de sus padres o tutores legales y tienen prohibido realizar trabajos nocturnos, horas extraordinarias o actividades declaradas insalubres o peligrosas.",
                "El contrato de trabajo es el acuerdo entre el empresario y el trabajador por el que este presta sus servicios a cambio de un salario. Tras las recientes reformas laborales para combatir la precariedad, el contrato ordinario general en España es el contrato indefinido (a tiempo completo o a tiempo parcial), existiendo además contratos formativos para jóvenes y contratos de duración determinada por circunstancias de la producción o sustitución.",
                "El Estatuto de los Trabajadores garantiza un conjunto de derechos irrenunciables: una jornada máxima legal ordinaria de cuarenta horas semanales de trabajo efectivo de promedio en cómputo anual, un descanso mínimo semanal de día y medio ininterrumpido y unas vacaciones anuales retribuidas (pagadas) que en ningún caso pueden ser inferiores a treinta días naturales por año trabajado.",
                "Asimismo, el Gobierno fija anualmente, previa consulta con los sindicatos y las asociaciones empresariales más representativas, el Salario Mínimo Interprofesional (SMI), que establece la cuantía retributiva mínima que debe percibir cualquier trabajador a jornada completa en España, habitualmente distribuida en catorce pagas anuales (doce mensualidades más dos pagas extraordinarias en verano y Navidad)."
            ],
            "questions": [
                ("¿Cuál es la edad mínima legal para poder trabajar en España (con autorización de los padres o tutores si aún no se es mayor de edad)?", ["16 años", "12 años", "14 años", "21 años"], 0),
                ("¿Cómo se llama la ley principal que regula los derechos y deberes de los trabajadores asalariados y las empresas en España?", ["El Estatuto de los Trabajadores", "El Código de la Circulación", "La Ley de Propiedad Horizontal", "La Ley de Costas"], 0),
                ("¿Cuántos días naturales de vacaciones pagadas al año corresponden como mínimo por ley a un trabajador en España?", ["30 días naturales al año (o 22 días laborables)", "7 días naturales al año", "10 días naturales cada dos años", "Ninguno si tiene contrato indefinido"], 0)
            ],
            "vocab": [
                ("el Estatuto de los Trabajadores", "noun", "Workers' Statute (Spanish labor law)", "El Estatuto de los Trabajadores regula los contratos, los salarios y las vacaciones."),
                ("el contrato indefinido", "noun", "permanent employment contract", "El contrato indefinido ofrece estabilidad laboral sin fecha fija de finalización."),
                ("el Salario Mínimo Interprofesional", "noun", "National Minimum Wage (SMI)", "Ningún trabajador a jornada completa puede cobrar menos del Salario Mínimo Interprofesional."),
                ("la jornada laboral", "noun", "working hours / workday", "La jornada laboral ordinaria máxima en España es de cuarenta horas semanales de promedio."),
                ("las vacaciones retribuidas", "noun", "paid holidays / paid annual leave", "Todo empleado tiene derecho a treinta días naturales de vacaciones retribuidas al año."),
                ("la paga extraordinaria", "noun", "bonus / extra salary payment (summer and Christmas)", "Los trabajadores españoles tienen derecho a dos pagas extraordinarias al año."),
                ("el convenio colectivo", "noun", "collective bargaining agreement", "El convenio colectivo mejora las condiciones salariales y horarias de cada sector."),
                ("el trabajador por cuenta ajena", "noun", "salaried employee (working for an employer)", "El trabajador por cuenta ajena recibe una nómina mensual de su empresa.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas laborales SMI en España?", ["Salario Mínimo Interprofesional", "Servicio Médico Infantil", "Sistema Monetario Internacional", "Sindicato de Maestros Independientes"], 0),
                ("¿Cómo se llama el acuerdo negociado entre los sindicatos de trabajadores y los representantes de los empresarios para regular los sueldos y horarios de un sector concreto?", ["El convenio colectivo", "El testamento vital", "La escritura hipotecaria", "El padrón municipal"], 0)
            ],
            "ex_fb": [
                ("La edad mínima legal para trabajar en España es de ___ años.", "16", "The minimum legal age to work in Spain is 16 years old."),
                ("La ley fundamental que protege los derechos laborales en España es el ___ de los Trabajadores.", "Estatuto", "The fundamental law protecting labor rights in Spain is the Workers' Statute.")
            ],
            "ex_sb": [
                (["La", "edad", "mínima", "para", "trabajar", "en", "España", "es", "de", "dieciséis", "años."], "The minimum age to work in Spain is sixteen years.")
            ],
            "ex_dict": [
                ("El Estatuto de los Trabajadores garantiza treinta días naturales de vacaciones pagadas al año.", "The Workers' Statute guarantees thirty calendar days of paid vacation per year.")
            ]
        },
        {
            "num": "02",
            "title": "La Seguridad Social, las cotizaciones y la nómina",
            "objective": "Comprender el funcionamiento de la Seguridad Social española, el número de afiliación (NUSS), las cotizaciones y la estructura de una nómina mensual.",
            "grammar_title": "Verbos de aportación y retención financiera («cotizar a», «deducir de», «percibir el salario neto»)",
            "grammar_slug": "verbos-aportacion-retencion-nomina",
            "grammar_Body": """Para explicar la nómina y las cotizaciones sociales en España se emplean verbos con régimen preposicional específico:

- *Tanto la empresa como el trabajador **cotizan mensualmente a** la Seguridad Social.*
- *Del salario bruto **se deducen** las cotizaciones sociales y la retención del IRPF.*
- *El trabajador **percibe** en su cuenta bancaria el **salario líquido o neto**.*""",
            "story_title": "El escudo solidario que protege a los trabajadores",
            "paragraphs": [
                "El artículo 41 de la Constitución Española establece que los poderes públicos mantendrán un régimen público de Seguridad Social para todos los ciudadanos, que garantice la asistencia y prestaciones sociales suficientes ante situaciones de necesidad, especialmente en caso de desempleo, enfermedad, maternidad, incapacidad laboral o jubilación.",
                "Toda persona que va a iniciar una actividad laboral por primera vez en España —ya sea como empleado asalariado o por cuenta propia— debe disponer de un Número de la Seguridad Social (NUSS) o número de afiliación, que es único para toda la vida laboral. Cuando una empresa contrata a un trabajador, tiene la obligación legal de tramitar su «alta» en la Tesorería General de la Seguridad Social (TGSS) antes de que empiece a trabajar.",
                "El sistema contributivo de la Seguridad Social se financia mediante las «cotizaciones sociales», que son aportaciones económicas mensuales obligatorias pagadas mayoritariamente por la empresa empleadora y, en una proporción menor, por el propio trabajador.",
                "Cada mes, el trabajador recibe un recibo oficial de salarios conocido como la «nómina». En la nómina figuran los datos de la empresa y del empleado, su categoría profesional, el «salario bruto» (el total devengado antes de descuentos) y las dos grandes deducciones legales: la cotización a la Seguridad Social y la retención a cuenta del Impuesto sobre la Renta de las Personas Físicas (IRPF).",
                "La cantidad final que el trabajador recibe efectivamente en su cuenta bancaria tras restar al salario bruto las cotizaciones sociales y el IRPF se denomina «salario neto» o «líquido a percibir». En cualquier momento, el ciudadano puede consultar por internet o teléfono su «Informe de Vida Laboral», documento oficial que recoge todos los días cotizados y empresas en las que ha trabajado."
            ],
            "questions": [
                ("¿Cómo se llama el recibo mensual oficial donde se detallan el sueldo bruto, las cotizaciones a la Seguridad Social, las retenciones de IRPF y el sueldo neto de un trabajador?", ["La nómina", "La factura de la luz", "El certificado de empadronamiento", "La letra del tesoro"], 0),
                ("¿Qué es el salario neto (o líquido a percibir) de una nómina?", ["La cantidad final de dinero que recibe realmente el trabajador tras descontar impuestos (IRPF) y cotizaciones a la Seguridad Social", "El sueldo antes de aplicar ningún descuento legal", "El impuesto que paga el ayuntamiento por las basuras", "La multa por llegar tarde al trabajo"], 0),
                ("¿Qué documento oficial expedido por la Seguridad Social recoge de forma cronológica todas las empresas y el total de días en los que una persona ha trabajado y cotizado en España?", ["El Informe de Vida Laboral", "El libro de familia", "El carné por puntos", "La partida de bautismo"], 0)
            ],
            "vocab": [
                ("la Seguridad Social", "noun", "Social Security system", "Todo trabajador en España debe estar dado de alta en la Seguridad Social."),
                ("la nómina", "noun", "payslip / monthly payroll statement", "La nómina detalla el salario bruto, las deducciones y el salario neto mensual."),
                ("la cotización", "noun", "Social Security contribution", "Las cotizaciones a la Seguridad Social dan derecho a la jubilación y al paro."),
                ("el salario bruto", "noun", "gross salary (before taxes and contributions)", "El salario bruto es el sueldo total antes de restar el IRPF y la Seguridad Social."),
                ("el salario neto", "noun", "net salary / take-home pay", "El salario neto o líquido es el dinero que se ingresa finalmente en la cuenta bancaria."),
                ("la vida laboral", "noun", "official employment history report (Informe de Vida Laboral)", "El informe de vida laboral acredita cuántos años ha cotizado un trabajador."),
                ("el alta en la Seguridad Social", "noun", "registration as an active contributor in Social Security", "La empresa debe tramitar el alta del trabajador antes de su primer día de empleo."),
                ("la Tesorería General de la Seguridad Social", "noun", "General Treasury of Social Security (TGSS)", "La Tesorería General de la Seguridad Social recauda las cotizaciones de empresas y trabajadores.")
            ],
            "ex_mc": [
                ("¿Qué dos conceptos principales se descuentan del salario bruto en la nómina mensual de un trabajador en España?", ["Las cotizaciones a la Seguridad Social y la retención del IRPF (impuesto sobre la renta)", "El abono transporte y el recibo del agua", "El seguro del coche y el IBI municipal", "El pago de la hipoteca y la comunidad de vecinos"], 0),
                ("¿Quién tiene la obligación de dar de alta en la Seguridad Social a un trabajador contratado por una empresa?", ["El empresario o la empresa que lo contrata, antes del inicio del trabajo", "El vecino del piso superior", "El colegio donde estudió la Primaria", "Nadie, el alta es opcional"], 0)
            ],
            "ex_fb": [
                ("El documento mensual que recibe el trabajador con el desglose de su sueldo y descuentos se llama ___.", "nómina", "The monthly document received by the worker with the breakdown of their salary and deductions is called a payslip (nómina)."),
                ("El informe de ___ laboral recoge todos los periodos en los que un ciudadano ha cotizado a la Seguridad Social.", "vida", "The employment history report (vida laboral) records all periods in which a citizen has contributed to Social Security.")
            ],
            "ex_sb": [
                (["La", "empresa", "y", "el", "trabajador", "cotizan", "a", "la", "Seguridad", "Social."], "The company and the worker contribute to Social Security.")
            ],
            "ex_dict": [
                ("En la nómina mensual se descuentan la cotización a la Seguridad Social y la retención del IRPF.", "On the monthly payslip, the Social Security contribution and the IRPF withholding are deducted.")
            ]
        },
        {
            "num": "03",
            "title": "Trabajadores autónomos, emprendimiento y cooperativas",
            "objective": "Distinguir entre trabajador asalariado (por cuenta ajena) y trabajador autónomo (por cuenta propia) y conocer las obligaciones del régimen RETA y Hacienda.",
            "grammar_title": "Contraste léxico y preposicional («trabajar por cuenta propia» frente a «trabajar por cuenta ajena»)",
            "grammar_slug": "contraste-cuenta-propia-cuenta-ajena",
            "grammar_Body": """En la terminología laboral y fiscal del CCSE es esencial distinguir dos locuciones adverbiales opuestas:

- **Trabajar por cuenta ajena**: ser empleado asalariado de una empresa o administración y recibir una nómina.
- **Trabajar por cuenta propia (ser autónomo)**: ejercer una actividad económica o profesional de forma independiente, emitir facturas y pagar la cuota mensual del **RETA (Régimen Especial de Trabajadores Autónomos)**.""",
            "story_title": "Emprender y trabajar por cuenta propia en España",
            "paragraphs": [
                "El artículo 38 de la Constitución Española reconoce la libertad de empresa en el marco de la economía de mercado. En España existen más de tres millones de personas que desarrollan su actividad económica o profesional de manera independiente sin depender del contrato laboral de un jefe: son los «trabajadores autónomos» o trabajadores por cuenta propia.",
                "Son trabajadores autónomos desde el propietario de un pequeño comercio de barrio, un taxista, un fontanero o un hostelero hasta los profesionales liberales como abogados, arquitectos, diseñadores gráficos, traductores o médicos con consulta propia. Para empezar a trabajar como autónomo en España es obligatorio realizar dos trámites simultáneos y gratuitos: darse de alta en el Censo de Empresarios y Profesionales de la Agencia Tributaria (Hacienda) y darse de alta en el Régimen Especial de Trabajadores Autónomos (RETA) de la Seguridad Social.",
                "A diferencia de los asalariados, el trabajador autónomo abona mensualmente su propia cuota de cotización a la Seguridad Social —calculada en función de sus ingresos o rendimientos netos reales y con una «tarifa plana» reducida durante el primer año para nuevos emprendedores— y emite facturas a sus clientes aplicando el Impuesto sobre el Valor Añadido (IVA), que luego declara trimestralmente ante Hacienda junto con sus pagos fraccionados de IRPF.",
                "Quienes desean constituir una empresa con personalidad jurídica propia suelen optar por crear una Sociedad de Responsabilidad Limitada (S. L.) o una Sociedad Anónima (S. A.), inscribiéndola en el Registro Mercantil mediante escritura ante notario. Para agilizar estos trámites existen los Puntos de Atención al Emprendedor (PAE), que permiten constituir empresas por vía telemática en pocos días.",
                "Asimismo, España cuenta con una fuerte tradición de economía social a través de las sociedades cooperativas (industriales, agrarias o de consumo), donde los propios trabajadores son socios copropietarios y gestionan democráticamente la empresa."
            ],
            "questions": [
                ("¿Cómo se llama en España a la persona que realiza una actividad económica o profesional de forma habitual, personal y directa por cuenta propia, sin estar sujeta a un contrato de trabajo con un jefe?", ["Trabajador autónomo (o por cuenta propia)", "Funcionario interino", "Pensionista pasivo", "Trabajador por cuenta ajena"], 0),
                ("¿En qué dos organismos públicos debe darse de alta obligatoriamente una persona para empezar a trabajar como autónomo en España?", ["En la Agencia Tributaria (Hacienda) y en el Régimen Especial de Trabajadores Autónomos (RETA) de la Seguridad Social", "En el Museo del Prado y en el Senado", "En la Dirección General de Tráfico y en AENA", "Únicamente en el club deportivo de su barrio"], 0),
                ("¿Qué significan las siglas mercantiles «S. L.» que acompañan al nombre de muchas pequeñas y medianas empresas españolas?", ["Sociedad Limitada (o Sociedad de Responsabilidad Limitada)", "Sindicato Libre", "Servicio Local", "Sector Laboral"], 0)
            ],
            "vocab": [
                ("el trabajador autónomo", "noun", "self-employed worker / freelancer", "El trabajador autónomo ejerce su profesión por cuenta propia y emite facturas."),
                ("por cuenta propia", "adverb", "self-employed / on one's own account", "Más de tres millones de personas trabajan por cuenta propia en España."),
                ("el RETA", "noun", "Special Scheme for Self-Employed Workers (Social Security)", "Los autónomos cotizan mensualmente en el RETA de la Seguridad Social."),
                ("la factura", "noun", "invoice", "El profesional autónomo debe emitir una factura con IVA por cada servicio prestado."),
                ("la Sociedad Limitada", "noun", "Limited Liability Company (S.L.)", "La Sociedad Limitada es la forma jurídica más común entre las pymes españolas."),
                ("la pyme", "noun", "small and medium-sized enterprise (SME)", "Las pymes y los autónomos generan la mayor parte del empleo en España."),
                ("la cooperativa", "noun", "cooperative society", "En una cooperativa los trabajadores son al mismo tiempo socios propietarios de la empresa."),
                ("el emprendedor", "noun", "entrepreneur", "Los nuevos emprendedores disfrutan de una cuota reducida de autónomos el primer año.")
            ],
            "ex_mc": [
                ("¿Qué significan las siglas españolas «pyme», muy utilizadas en la economía y las noticias laborales?", ["Pequeña y mediana empresa", "Plan y método educativo", "Partido y movimiento electoral", "Puerto y marina española"], 0),
                ("¿Cómo declara habitualmente un trabajador autónomo el IVA de sus facturas ante la Agencia Tributaria?", ["Mediante declaraciones trimestrales y un resumen anual", "Una sola vez cada diez años", "Pagándolo en efectivo al alcalde de su pueblo", "Los autónomos nunca cobran ni declaran IVA"], 0)
            ],
            "ex_fb": [
                ("Quien trabaja de forma independiente sin jefe ni empresa empleadora es un trabajador ___ o por cuenta propia.", "autónomo", "Someone who works independently without a boss or employing company is a self-employed worker (autónomo)."),
                ("Las pequeñas y medianas empresas se conocen en España con la palabra formada por sus siglas: ___.", "pymes", "Small and medium-sized enterprises are known in Spain by the word formed from their acronym: pymes.")
            ],
            "ex_sb": [
                (["El", "trabajador", "autónomo", "realiza", "su", "actividad", "por", "cuenta", "propia."], "The self-employed worker carries out their activity on their own account.")
            ],
            "ex_dict": [
                ("Las pequeñas y medianas empresas y los autónomos crean la mayor parte del empleo en España.", "Small and medium-sized enterprises and self-employed workers create most of the jobs in Spain.")
            ]
        },
        {
            "num": "04",
            "title": "El SEPE, la prestación por desempleo (el paro) y las pensiones de jubilación",
            "objective": "Conocer el funcionamiento del Servicio Público de Empleo Estatal (SEPE), la prestación por desempleo, los permisos de nacimiento y la pensión de jubilación (INSS).",
            "grammar_title": "Condicionales de requisito contributivo («para tener derecho a..., es preciso haber cotizado...»)",
            "grammar_slug": "condicionales-requisito-contributivo-sepe",
            "grammar_Body": """Para explicar el acceso a las prestaciones económicas de la Seguridad Social se emplean **oraciones condicionales y finales de requisito**:

- ***Para tener derecho a** la prestación contributiva por desempleo («el paro»), **es preciso haber cotizado** al menos 360 días en los últimos seis años.*
- *La pensión de jubilación **es gestionada por** el Instituto Nacional de la Seguridad Social (INSS).*""",
            "story_title": "Protección ante el desempleo, la maternidad y la vejez",
            "paragraphs": [
                "Cuando un trabajador pierde su empleo de forma involuntaria (por despido o finalización de su contrato temporal), el Estado español lo protege económica y formativamente a través del Servicio Público de Empleo Estatal (SEPE) —antiguamente llamado INEM— en colaboración con los servicios públicos de empleo de las diecisiete comunidades autónomas.",
                "Si el trabajador ha cotizado a la Seguridad Social un mínimo de 360 días dentro de los seis años anteriores a la pérdida del empleo, tiene derecho a cobrar la prestación contributiva por desempleo, conocida popularmente en toda España como «el paro». Su duración depende del tiempo cotizado (desde cuatro meses hasta un máximo de dos años). Para quienes han agotado la prestación contributiva o no alcanzan el año cotizado y carecen de rentas, existen los subsidios por desempleo y el Ingreso Mínimo Vital (IMV).",
                "Por su parte, el Instituto Nacional de la Seguridad Social (INSS) reconoce y abona las prestaciones económicas por incapacidad temporal (baja médica por enfermedad o accidente), incapacidad permanente, viudedad, orfandad y nacimiento y cuidado de menor.",
                "En España, tras la equiparación total entre hombres y mujeres para fomentar la corresponsabilidad familiar, el permiso por nacimiento y cuidado de menor (antiguas bajas de maternidad y paternidad) tiene una duración igual e intransferible de dieciséis semanas (16 semanas) remuneradas al cien por cien de la base reguladora para cada uno de los dos progenitores.",
                "Al final de la vida activa, el trabajador accede a la pensión pública de jubilación. En España, la edad ordinaria de jubilación se sitúa entre los sesenta y cinco años (65 años, para quienes cuentan con largas carreras de cotización de más de 38 años) y los sesenta y siete años (67 años), requiriéndose un mínimo de quince años cotizados para acceder a la pensión contributiva."
            ],
            "questions": [
                ("¿Qué organismo público gestiona en España las prestaciones por desempleo (el «paro») y la orientación laboral a nivel estatal?", ["El Servicio Público de Empleo Estatal (SEPE)", "La Dirección General de Tráfico (DGT)", "El Instituto Geográfico Nacional (IGN)", "La Agencia Estatal de Meteorología (AEMET)"], 0),
                ("¿Cuántas semanas de permiso retribuido al cien por cien corresponden por ley en España a cada progenitor (tanto a la madre como al otro progenitor) por el nacimiento o adopción de un hijo?", ["16 semanas para cada progenitor", "2 semanas para el padre y 8 para la madre", "1 sola semana sin sueldo", "52 semanas solo para el abuelo"], 0),
                ("¿En torno a qué edades se sitúa la edad legal ordinaria de jubilación en España según los años cotizados?", ["Entre los 65 y los 67 años", "A los 50 años exactamente", "A los 45 años para todos los sectores", "A los 80 años obligatoriamente"], 0)
            ],
            "vocab": [
                ("el SEPE", "noun", "Public State Employment Service (Servicio Público de Empleo Estatal)", "El SEPE tramita las prestaciones por desempleo y ofrece cursos gratuitos de formación."),
                ("el paro", "noun", "unemployment / unemployment benefit (colloquial and standard)", "Cobrar el paro requiere haber cotizado al menos trescientos sesenta días."),
                ("la prestación por desempleo", "noun", "unemployment benefit", "La prestación por desempleo protege a quien pierde su trabajo de manera involuntaria."),
                ("la pensión de jubilación", "noun", "retirement pension", "El Instituto Nacional de la Seguridad Social abona mensualmente las pensiones de jubilación."),
                ("la baja médica", "noun", "sick leave (incapacidad temporal)", "El médico de cabecera del centro de salud expide el parte oficial de baja médica."),
                ("el permiso por nacimiento", "noun", "maternity / paternity parental leave (16 weeks each)", "El permiso por nacimiento de hijo es de dieciséis semanas pagadas para cada progenitor."),
                ("el Ingreso Mínimo Vital", "noun", "Minimum Vital Income (IMV anti-poverty benefit)", "El Ingreso Mínimo Vital previene el riesgo de pobreza y exclusión social de los hogares."),
                ("el INSS", "noun", "National Institute of Social Security", "El INSS gestiona las pensiones de jubilación, viudedad e incapacidad en toda España.")
            ],
            "ex_mc": [
                ("¿Cómo se conoce popularmente en España tanto a la situación de desempleo como a la prestación económica que recibe quien pierde su trabajo?", ["El paro", "El censo", "El vado", "El fuero"], 0),
                ("¿Qué profesional es el único autorizado para firmar el parte oficial de «baja médica» por enfermedad común de un trabajador?", ["Un médico del servicio público de salud (médico de cabecera)", "El director del banco del trabajador", "El presidente de la comunidad de vecinos", "El propio trabajador mediante una nota escrita a mano"], 0)
            ],
            "ex_fb": [
                ("El organismo estatal encargado de pagar la prestación por desempleo es el ___ (Servicio Público de Empleo Estatal).", "SEPE", "The state agency in charge of paying unemployment benefits is SEPE (Public State Employment Service)."),
                ("En España, la edad ordinaria de ___ se sitúa entre los 65 y los 67 años.", "jubilación", "In Spain, the ordinary retirement age is between 65 and 67 years old.")
            ],
            "ex_sb": [
                (["El", "SEPE", "gestiona", "las", "prestaciones", "por", "desempleo", "en", "España."], "SEPE manages unemployment benefits in Spain.")
            ],
            "ex_dict": [
                ("El permiso por nacimiento y cuidado de menor es de dieciséis semanas para cada progenitor.", "Parental leave for birth and childcare is sixteen weeks for each parent.")
            ]
        },
        {
            "num": "05",
            "title": "Prevención de riesgos laborales, representación sindical e Inspección de Trabajo",
            "objective": "Conocer la Ley de Prevención de Riesgos Laborales, los representantes de los trabajadores (comités de empresa) y la función de la Inspección de Trabajo.",
            "grammar_title": "Oraciones sustantivas de obligación empresarial («velar por que + subjuntivo», «proporcionar equipos de protección»)",
            "grammar_slug": "obligacion-empresarial-prevencion-riesgos",
            "grammar_Body": """Para expresar las obligaciones legales de seguridad e higiene en el trabajo se utiliza **tener la obligación de + infinitivo** o **velar por que + presente de subjuntivo**:

- *Las empresas **tienen la obligación de garantizar** la seguridad y la salud de sus empleados.*
- *La Inspección de Trabajo **vela por que se cumpla** la legislación laboral y de Seguridad Social.*""",
            "story_title": "Salud en el trabajo y diálogo social",
            "paragraphs": [
                "El artículo 40.2 de la Constitución Española ordena a los poderes públicos velar por la seguridad e higiene en el trabajo. Este mandato se desarrolla en la Ley de Prevención de Riesgos Laborales de 1995, que establece que todo empresario tiene el deber legal de proteger la salud física y mental de sus trabajadores frente a los riesgos derivados de su actividad.",
                "En virtud de esta ley, la empresa está obligada a evaluar los riesgos de cada puesto, impartir formación preventiva gratuita dentro de la jornada laboral, ofrecer reconocimientos médicos periódicos y suministrar sin coste alguno para el empleado los Equipos de Protección Individual (EPI) necesarios, como cascos, guantes, calzado de seguridad, arneses o gafas protectoras.",
                "Dentro de las empresas, los trabajadores participan democráticamente en la defensa de sus derechos laborales y salariales mediante sus representantes elegidos cada cuatro años en las elecciones sindicales: en los centros de entre 6 y 49 trabajadores eligen a los «delegados de personal», y en las empresas de 50 o más trabajadores eligen un órgano colegiado llamado «Comité de Empresa».",
                "A nivel nacional, el diálogo social tripartito reúne al Gobierno de España, a los sindicatos más representativos —como Comisiones Obreras (CC. OO.) y la Unión General de Trabajadores (UGT)— y a las organizaciones empresariales —la Confederación Española de Organizaciones Empresariales (CEOE) y la Confederación Española de la Pequeña y Mediana Empresa (CEPYME)— para acordar subidas salariales, reformas de pensiones y planes de empleo.",
                "Finalmente, para vigilar el cumplimiento estricto de las leyes laborales, perseguir el empleo sumergido o sin contrato y sancionar los abusos o accidentes por falta de medidas de seguridad, existe un cuerpo público especializado dependiente del Ministerio de Trabajo y Economía Social: la Inspección de Trabajo y Seguridad Social, ante la cual cualquier ciudadano puede presentar una denuncia confidencial."
            ],
            "questions": [
                ("¿Quién tiene la obligación legal de proporcionar gratuitamente a los trabajadores los Equipos de Protección Individual (casco, guantes, botas de seguridad) necesarios para su trabajo?", ["La empresa o el empresario que los contrata", "El propio trabajador pagándolo de su sueldo neto", "El ayuntamiento de la localidad", "La Cruz Roja Española"], 0),
                ("¿Cómo se llama el órgano representativo elegido por los trabajadores en las empresas españolas que tienen 50 o más empleados?", ["El Comité de Empresa", "El Senado Provincial", "La Junta de Propietarios", "El Consejo Escolar"], 0),
                ("¿Qué organismo público vigila que las empresas cumplan las leyes laborales, den de alta a sus empleados en la Seguridad Social y respeten la seguridad en el trabajo?", ["La Inspección de Trabajo y Seguridad Social", "El Instituto Cervantes", "Patrimonio Nacional", "La Sociedad Estatal de Loterías"], 0)
            ],
            "vocab": [
                ("la prevención de riesgos laborales", "noun", "occupational risk prevention / workplace health and safety", "La empresa debe impartir un curso de prevención de riesgos laborales a cada empleado."),
                ("el Equipo de Protección Individual", "noun", "Personal Protective Equipment (PPE / EPI)", "El casco y las botas reforzadas son Equipos de Protección Individual obligatorios en la obra."),
                ("el Comité de Empresa", "noun", "Works Council (in companies with 50+ employees)", "El Comité de Empresa representa a la plantilla ante la dirección de la compañía."),
                ("el delegado de personal", "noun", "staff representative (in companies with 6–49 employees)", "En las pequeñas empresas los trabajadores eligen delegados de personal."),
                ("la Inspección de Trabajo", "noun", "Labor and Social Security Inspectorate", "La Inspección de Trabajo sanciona a las empresas que tienen empleados sin contrato."),
                ("el diálogo social", "noun", "social dialogue (government, unions, employers)", "El diálogo social entre Gobierno, sindicatos y patronal fortalece la paz laboral."),
                ("la patronal", "noun", "employers' association (CEOE / CEPYME)", "La CEOE y la CEPYME son las principales organizaciones de la patronal española."),
                ("el accidente laboral", "noun", "workplace / occupational accident", "Las medidas de seguridad reducen drásticamente el riesgo de sufrir un accidente laboral.")
            ],
            "ex_mc": [
                ("¿Qué son la CEOE y la CEPYME en el ámbito económico y laboral español?", ["Las principales organizaciones empresariales (la patronal) que representan a las empresas y pymes", "Dos sindicatos de estudiantes de Bachillerato", "Dos cuerpos de policía autonómica", "Dos impuestos municipales sobre vehículos"], 0),
                ("¿Cuáles son los dos sindicatos de trabajadores más representativos a nivel estatal en España?", ["Comisiones Obreras (CC. OO.) y la Unión General de Trabajadores (UGT)", "RENFE y ADIF", "AENA y Puertos del Estado", "ONCE y Cruz Roja"], 0)
            ],
            "ex_fb": [
                ("En las empresas de 50 o más trabajadores, el órgano que representa a los empleados se llama ___ de Empresa.", "Comité", "In companies with 50 or more workers, the body that represents employees is called the Works Council (Comité de Empresa)."),
                ("La ___ de Trabajo y Seguridad Social vigila que las empresas cumplan las normas laborales.", "Inspección", "The Labor and Social Security Inspectorate ensures that companies comply with labor rules.")
            ],
            "ex_sb": [
                (["Las", "empresas", "deben", "garantizar", "la", "seguridad", "y", "salud", "de", "los", "trabajadores."], "Companies must guarantee the safety and health of workers.")
            ],
            "ex_dict": [
                ("El Comité de Empresa y los delegados de personal representan a los trabajadores en las empresas.", "The Works Council and staff representatives represent workers in companies.")
            ]
        }
    ]
}


UNIT_32 = {
    "unit_num": 68,
    "slug": "vivienda",
    "title": "Vivienda, Registro y Empadronamiento",
    "theme": "Derecho a la vivienda, compraventa, hipoteca, alquiler (LAU), comunidad de vecinos y Padrón Municipal en España (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "Compra de vivienda, escritura pública, hipoteca y Registro de la Propiedad",
            "objective": "Conocer los trámites para comprar una vivienda en España: el notario, la escritura pública, el préstamo hipotecario y el Registro de la Propiedad.",
            "grammar_title": "Secuencias procedimentales administrativas («firmar ante notario», «inscribir en el Registro»)",
            "grammar_slug": "secuencias-procedimentales-compraventa-vivienda",
            "grammar_Body": """Para explicar el proceso jurídico de adquisición de un inmueble en España se usan verbos de formalización legal seguidos de las preposiciones **ante** (autoridad) y **en** (registro público):

- *La compraventa de un piso **se formaliza en escritura pública ante notario**.*
- *Posteriormente, la propiedad **se inscribe en el Registro de la Propiedad** para garantizar la seguridad jurídica.*""",
            "story_title": "Seguridad jurídica al comprar un hogar en España",
            "paragraphs": [
                "El artículo 47 de la Constitución Española reconoce que todos los españoles tienen derecho a disfrutar de una vivienda digna y adecuada. En España, donde más del setenta y cinco por ciento de las familias son propietarias de su vivienda habitual, la compra de un piso o de una casa sigue un procedimiento dotado de una gran seguridad jurídica.",
                "Antes de firmar la compra, el comprador suele solicitar al Registro de la Propiedad un documento informativo barato y rápido llamado «Nota Simple». La Nota Simple acredita quién es el verdadero propietario legal de la vivienda y certifica si el inmueble está libre de cargas o si, por el contrario, arrastra deudas, embargos o hipotecas pendientes.",
                "El contrato definitivo de compraventa y, en su caso, el préstamo hipotecario concedido por una entidad bancaria para financiar la compra (la «hipoteca») se firman mediante «escritura pública» ante un Notario, que es un funcionario público del Estado experto en Derecho que da fe de la identidad de las partes, de la legalidad del contrato y de que el comprador comprende todas las cláusulas financieras.",
                "Una vez firmada la escritura ante notario y abonados los impuestos correspondientes a la comunidad autónoma (el IVA si la vivienda es nueva de primera mano, o el Impuesto de Transmisiones Patrimoniales, ITP, si es de segunda mano), la escritura se inscribe en el Registro de la Propiedad para proteger plenamente los derechos del nuevo dueño frente a terceros.",
                "Además, todo inmueble urbano o rústico en España figura descrito físicamente en el Catastro Inmobiliario (dependiente del Ministerio de Hacienda), cuyo valor catastral sirve de base para que el ayuntamiento cobre anualmente a cada propietario el Impuesto sobre Bienes Inmuebles (IBI)."
            ],
            "questions": [
                ("¿Ante qué funcionario público del Estado se firma la escritura pública de compraventa de una vivienda y de un préstamo hipotecario en España?", ["Ante un notario", "Ante un médico de cabecera", "Ante un inspector de tráfico", "Ante un director de instituto"], 0),
                ("¿En qué institución pública se inscriben las escrituras de compra de una vivienda para acreditar legalmente quién es su propietario y si tiene cargas o hipotecas?", ["En el Registro de la Propiedad", "En el Registro Civil de nacimientos", "En el Padrón de vehículos", "En el Boletín Oficial del Estado"], 0),
                ("¿Qué impuesto municipal anual debe pagar todo propietario de un piso o una casa al ayuntamiento donde se ubica el inmueble?", ["El Impuesto sobre Bienes Inmuebles (IBI)", "El impuesto de matriculación de barcos", "La tasa de pasaporte", "El recargo de selectividad"], 0)
            ],
            "vocab": [
                ("la escritura pública", "noun", "public deed (signed before a notary)", "La compraventa de la vivienda se formaliza mediante escritura pública ante notario."),
                ("el notario", "noun", "notary public", "El notario comprueba la legalidad del contrato y la identidad de comprador y vendedor."),
                ("la hipoteca", "noun", "mortgage / mortgage loan", "La mayoría de las familias solicita una hipoteca al banco para comprar su vivienda."),
                ("el Registro de la Propiedad", "noun", "Land Registry (Property Register)", "Inscribir el piso en el Registro de la Propiedad protege legalmente al comprador."),
                ("la nota simple", "noun", "Land Registry summary extract (showing ownership and liens)", "Antes de comprar un piso conviene pedir una nota simple al Registro de la Propiedad."),
                ("el Catastro", "noun", "Cadastre (official geographic and tax inventory of real estate)", "El Catastro asigna una referencia catastral y un valor fiscal a cada inmueble."),
                ("el IBI", "noun", "Municipal Property Tax (Impuesto sobre Bienes Inmuebles)", "El propietario de una vivienda paga cada año el recibo del IBI a su ayuntamiento."),
                ("el contrato de arras", "noun", "earnest-money deposit agreement prior to purchase", "Al reservar la vivienda, comprador y vendedor suelen firmar un contrato privado de arras.")
            ],
            "ex_mc": [
                ("¿Cómo se llama el préstamo bancario a largo plazo en el que la propia vivienda sirve como garantía de pago para poder comprarla?", ["Préstamo hipotecario (o hipoteca)", "Beca de comedor", "Subsidio de desempleo", "Fianza de alquiler"], 0),
                ("¿Qué documento del Registro de la Propiedad solicita un comprador para comprobar si una vivienda tiene deudas o embargos antes de comprarla?", ["Una nota simple", "Un volante de empadronamiento", "Una receta electrónica", "Un informe de vida laboral"], 0)
            ],
            "ex_fb": [
                ("La escritura pública de compraventa de una casa se firma ante un ___.", "notario", "The public deed of sale for a house is signed before a notary."),
                ("Para proteger los derechos del nuevo dueño, la escritura de la vivienda se inscribe en el ___ de la Propiedad.", "Registro", "To protect the rights of the new owner, the deed of the home is registered in the Land Registry.")
            ],
            "ex_sb": [
                (["La", "escritura", "de", "la", "vivienda", "se", "firma", "ante", "notario."], "The deed of the home is signed before a notary.")
            ],
            "ex_dict": [
                ("El propietario de una vivienda debe pagar anualmente el Impuesto sobre Bienes Inmuebles al ayuntamiento.", "The owner of a home must pay the Property Tax annually to the city council.")
            ]
        },
        {
            "num": "02",
            "title": "El alquiler de vivienda (LAU), el contrato de arrendamiento y la fianza",
            "objective": "Conocer los derechos y deberes del casero (arrendador) y del inquilino (arrendatario) según la Ley de Arrendamientos Urbanos (LAU) y la fianza obligatoria.",
            "grammar_title": "Parejas léxicas recíprocas («el arrendador / casero» y «el arrendatario / inquilino»)",
            "grammar_slug": "parejas-lexicas-arrendador-arrendatario",
            "grammar_Body": """En los contratos de alquiler de vivienda regulados por la Ley de Arrendamientos Urbanos (LAU) intervienen dos figuras jurídicas complementarias:

- **El arrendador** (llamado cotidianamente **el casero** o propietario): cede el uso de la vivienda.
- **El arrendatario** (llamado cotidianamente **el inquilino**): habita la vivienda y paga la renta mensual y una **fianza legal de un mes**.""",
            "story_title": "Inquilinos y caseros: reglas claras para vivir de alquiler",
            "paragraphs": [
                "El alquiler o arrendamiento de viviendas para uso habitual en España está regulado por la Ley de Arrendamientos Urbanos (LAU) y por la Ley por el Derecho a la Vivienda. En todo contrato de alquiler intervienen dos partes: el «arrendador» (conocido popularmente como el «casero», que es el propietario del piso) y el «arrendatario» (conocido como el «inquilino», que vive en él a cambio de pagar una renta mensual).",
                "De acuerdo con la Ley de Arrendamientos Urbanos vigente, aunque el contrato se firme inicialmente por un año, el inquilino que utiliza el piso como vivienda habitual tiene derecho a que el contrato se prorrogue obligatoriamente cada año hasta alcanzar una duración mínima de cinco años (5 años) si el propietario es una persona física, o de siete años (7 años) si el propietario es una empresa o persona jurídica.",
                "En el momento de la firma del contrato, es obligatorio por ley que el inquilino entregue en metálico una «fianza» equivalente a una mensualidad de renta (1 mes de alquiler) en los arrendamientos de vivienda habitual, o de dos meses cuando se alquila un local para uso distinto del de vivienda (por ejemplo, una oficina o tienda).",
                "El casero no puede quedarse ese dinero en su bolsillo particular, sino que tiene la obligación de depositar la fianza en el organismo público de vivienda de su comunidad autónoma (como el IVIMA en Madrid o el INCASÒL en Cataluña). Al finalizar el contrato de alquiler, si el inquilino devuelve el piso en buen estado y sin recibos pendientes, el propietario debe devolverle íntegramente el importe de la fianza en el plazo máximo de un mes.",
                "Durante la vigencia del alquiler, el propietario está obligado a realizar sin subir la renta todas las reparaciones necesarias para conservar la vivienda en condiciones de habitabilidad (como arreglar una avería estructural de la caldera), mientras que las pequeñas reparaciones derivadas del desgaste por el uso diario corren a cargo del inquilino."
            ],
            "questions": [
                ("¿Cómo se llama comúnmente en España a la persona que alquila una vivienda para vivir en ella pagando una renta mensual (el arrendatario)?", ["El inquilino", "El notario", "El registrador", "El conserje"], 0),
                ("¿A cuántas mensualidades de renta equivale la fianza legal obligatoria que debe entregarse al firmar un contrato de alquiler de vivienda habitual en España?", ["A una mensualidad de renta (1 mes)", "A doce mensualidades de renta (1 año entero)", "A diez años de sueldo", "En España está prohibido pedir fianza"], 0),
                ("¿Qué sucede con la fianza cuando termina el contrato de alquiler y el inquilino entrega las llaves dejando la vivienda en buen estado y al corriente de pagos?", ["Se le devuelve íntegramente al inquilino", "Pasa a ser propiedad definitiva del alcalde", "Se entrega al presidente de la escalera", "Nunca se devuelve en ningún caso"], 0)
            ],
            "vocab": [
                ("el alquiler", "noun", "rent / rental", "El precio del alquiler se abona habitualmente durante los primeros siete días de cada mes."),
                ("el inquilino", "noun", "tenant / lessee (arrendatario)", "El inquilino tiene derecho a permanecer hasta cinco años en su vivienda habitual."),
                ("el casero", "noun", "landlord / property owner (arrendador)", "El casero debe depositar la fianza en el organismo de su comunidad autónoma."),
                ("la fianza", "noun", "security deposit (1 month's rent for residential leases)", "Al terminar el contrato sin desperfectos, el propietario devuelve la fianza al inquilino."),
                ("la Ley de Arrendamientos Urbanos", "noun", "Urban Leases Act (LAU)", "La Ley de Arrendamientos Urbanos regula los contratos de alquiler de vivienda en España."),
                ("la renta mensual", "noun", "monthly rent payment", "La renta mensual se actualiza anualmente según los límites fijados por la ley."),
                ("la habitabilidad", "noun", "habitability / livable condition", "El propietario debe mantener la vivienda en condiciones adecuadas de habitabilidad."),
                ("el desahucio", "noun", "eviction", "La ley establece mecanismos de mediación y protección para familias vulnerables ante un desahucio.")
            ],
            "ex_mc": [
                ("¿Cómo se llama en el lenguaje jurídico del contrato de alquiler al propietario («el casero») y al inquilino?", ["Arrendador (el propietario) y arrendatario (el inquilino)", "Demandante y demandado", "Senador y diputado", "Emisor y cartero"], 0),
                ("Si el propietario de un piso en alquiler es una persona física, ¿hasta cuántos años tiene derecho el inquilino a prorrogar anualmente su contrato de vivienda habitual según la LAU?", ["Hasta 5 años (y hasta 7 años si el propietario es una empresa)", "Solo 15 días", "Exactamente 50 años obligatorios", "Solo 3 meses en verano"], 0)
            ],
            "ex_fb": [
                ("En un contrato de alquiler de vivienda habitual, la ___ obligatoria equivale a un mes de renta.", "fianza", "In a residential lease contract, the mandatory security deposit equals one month's rent."),
                ("La persona que vive de alquiler en un piso pagando una renta mensual al casero se llama ___ o arrendatario.", "inquilino", "The person who lives renting an apartment paying a monthly rent to the landlord is called a tenant (inquilino) or lessee.")
            ],
            "ex_sb": [
                (["La", "fianza", "se", "devuelve", "al", "inquilino", "al", "finalizar", "el", "contrato."], "The security deposit is returned to the tenant at the end of the contract.")
            ],
            "ex_dict": [
                ("En el alquiler de vivienda habitual la fianza legal obligatoria es de un mes de renta.", "In residential rentals the mandatory legal security deposit is one month's rent.")
            ]
        },
        {
            "num": "03",
            "title": "La comunidad de propietarios, los gastos comunes y las normas de convivencia",
            "objective": "Comprender el funcionamiento de las comunidades de vecinos en España según la Ley de Propiedad Horizontal: junta de propietarios, presidente y normas municipales de ruido.",
            "grammar_title": "Expresiones de copropiedad y convivencia vecinal («elementos comunes», «turno rotatorio»)",
            "grammar_slug": "copropiedad-convivencia-vecinal-horizontal",
            "grammar_Body": """Para explicar la organización de los edificios de pisos en España se distingue entre **elementos privativos** (el interior de cada piso) y **elementos comunes** (portal, escalera, ascensor, tejado, fachada):

- *Todos los dueños de un edificio forman parte de la **Comunidad de Propietarios** y contribuyen a los **gastos comunes** según su cuota de participación.*
- *El cargo de **Presidente de la comunidad** se ejerce habitualmente por sorteo o **turno rotatorio** entre los vecinos.*""",
            "story_title": "La democracia cotidiana en la escalera de vecinos",
            "paragraphs": [
                "España es uno de los países de Europa donde mayor porcentaje de la población vive en edificios de viviendas colectivas o bloques de pisos. La convivencia y el mantenimiento de estos edificios están regulados por la Ley de Propiedad Horizontal (LPH), que combina la propiedad exclusiva de cada vecino sobre su piso o local con la copropiedad compartida sobre los elementos comunes del inmueble: el portal, las escaleras, los ascensores, los patios, la fachada, el tejado y los jardines o piscinas.",
                "El conjunto de todos los dueños de pisos y locales de un edificio constituye la «Comunidad de Propietarios» (conocida popularmente como la «comunidad de vecinos»). Su órgano supremo de decisión es la Junta de Propietarios, que se reúne de forma ordinaria al menos una vez al año para aprobar las cuentas, el presupuesto anual y las obras del edificio, y de forma extraordinaria cuando surge un asunto urgente.",
                "Al frente de la comunidad se encuentra el Presidente, que debe ser obligatoriamente uno de los propietarios de viviendas o locales del edificio. El cargo se elige mediante votación o, muy frecuentemente, por turno rotatorio o sorteo anual entre todos los vecinos, y es legalmente obligatorio aceptarlo salvo que un juez autorice la dispensa por edad avanzada o enfermedad. Muchas comunidades contratan además a un profesional colegiado llamado «Administrador de Fincas» para llevar la contabilidad y contratar reparaciones.",
                "Cada propietario debe abonar mensualmente la «cuota de comunidad» para sufragar los gastos ordinarios de limpieza, luz de la escalera, mantenimiento del ascensor y seguro del edificio. Cuando la Junta aprueba una obra costosa no cubierta por el fondo de reserva —como instalar un ascensor para eliminar barreras arquitectónicas o rehabilitar la fachada—, los vecinos abonan una cuota extraordinaria llamada «derrama».",
                "Asimismo, los estatutos de la comunidad y las ordenanzas municipales de convivencia prohíben realizar ruidos molestos, fiestas ruidosas, obras o mudanzas durante las horas de descanso nocturno (habitualmente desde las 21:00 o 22:00 h hasta las 08:00 h de la mañana)."
            ],
            "questions": [
                ("¿Quién puede ser elegido Presidente de una Comunidad de Propietarios en un edificio de viviendas en España?", ["Únicamente uno de los propietarios de pisos o locales del propio edificio", "Cualquier vecino que viva de alquiler sin ser propietario", "El cartero del barrio", "Un funcionario designado por el Ministerio del Interior"], 0),
                ("¿Cómo se llama la cuota extraordinaria que aprueban los vecinos de una comunidad de propietarios para pagar una obra importante en el edificio, como arreglar el tejado o instalar un ascensor?", ["Una derrama", "Una beca", "Una hipoteca", "Una propina"], 0),
                ("¿Cuántas veces al año como mínimo debe reunirse la Junta de Propietarios de un edificio para aprobar los presupuestos y las cuentas?", ["Al menos una vez al año", "Una vez cada diez años", "Todos los lunes por la mañana", "Nunca es necesario reunirse"], 0)
            ],
            "vocab": [
                ("la comunidad de propietarios", "noun", "homeowners' association / building residents' association", "La comunidad de propietarios gestiona el mantenimiento del portal, el tejado y el ascensor."),
                ("la Junta de Propietarios", "noun", "general meeting of property owners", "La Junta de Propietarios se reúne al menos una vez al año para aprobar las cuentas."),
                ("el presidente de la comunidad", "noun", "president of the homeowners' association", "El presidente de la comunidad representa legalmente a todos los vecinos del inmueble."),
                ("el administrador de fincas", "noun", "property manager (licensed professional)", "El administrador de fincas elabora el presupuesto y gestiona los recibos de la comunidad."),
                ("la derrama", "noun", "special assessment / extraordinary community levy for building works", "Los vecinos aprobaron una derrama para renovar la fachada y el ascensor del edificio."),
                ("los elementos comunes", "noun", "common areas of a building (lobby, stairs, roof, elevator)", "El ascensor, la escalera y la azotea son elementos comunes de todos los propietarios."),
                ("la Ley de Propiedad Horizontal", "noun", "Horizontal Property Act (condominium law)", "La Ley de Propiedad Horizontal regula las comunidades de vecinos en España."),
                ("el descanso nocturno", "noun", "nighttime quiet hours (typically 22:00 to 08:00)", "Las ordenanzas municipales prohíben hacer obras o ruidos durante el horario de descanso nocturno.")
            ],
            "ex_mc": [
                ("¿Qué ley española regula los derechos y obligaciones de los vecinos en un bloque de pisos?", ["La Ley de Propiedad Horizontal", "El Estatuto de los Trabajadores", "La Ley General de Sanidad", "La Ley Electoral"], 0),
                ("Si en un edificio vive una persona mayor de setenta años o con discapacidad que necesita instalar un ascensor para salir a la calle, ¿es obligatorio para la comunidad de propietarios realizar las obras de accesibilidad?", ["Sí, las obras de accesibilidad para mayores de 70 años o personas con discapacidad son obligatorias por ley", "No, está prohibido instalar ascensores en edificios antiguos", "Solo si lo aprueba el Rey por Real Decreto", "Solo en edificios de más de cuarenta plantas"], 0)
            ],
            "ex_fb": [
                ("El presidente de una comunidad de vecinos debe ser obligatoriamente uno de los ___ del edificio.", "propietarios", "The president of a residents' association must mandatorily be one of the owners in the building."),
                ("La cuota extraordinaria que pagan los vecinos para financiar una obra importante en las zonas comunes se llama ___.", "derrama", "The special assessment paid by neighbors to finance major works in common areas is called a derrama.")
            ],
            "ex_sb": [
                (["La", "Junta", "de", "Propietarios", "se", "reúne", "al", "menos", "una", "vez", "al", "año."], "The Homeowners' Board meets at least once a year.")
            ],
            "ex_dict": [
                ("Todos los propietarios del edificio deben contribuir a los gastos de mantenimiento de las zonas comunes.", "All owners in the building must contribute to the maintenance costs of the common areas.")
            ]
        },
        {
            "num": "04",
            "title": "Suministros domésticos, eficiencia energética y reciclaje urbano",
            "objective": "Conocer la gestión de los suministros domésticos (luz, agua, gas, internet), el bono social eléctrico y los colores de los contenedores de reciclaje en España.",
            "grammar_title": "Clasificación por atributos y colores («el contenedor amarillo para envases», «el azul para papel»)",
            "grammar_slug": "clasificacion-colores-reciclaje-suministros",
            "grammar_Body": """En las preguntas prácticas de vida cotidiana del examen CCSE aparecen con frecuencia los **colores de los contenedores municipales de recogida selectiva de residuos**:

- **Contenedor amarillo**: envases de plástico, latas metálicas y briks.
- **Contenedor azul**: papel y cartón.
- **Contenedor verde (iglú)**: envases de vidrio (botellas, tarros, frascos).
- **Contenedor marrón**: biorresiduos o materia orgánica.
- **Punto Limpio**: electrodomésticos, muebles viejos, pilas, aceite usado y escombros.""",
            "story_title": "Servicios del hogar y compromiso con el medio ambiente",
            "paragraphs": [
                "Al instalarse en una vivienda en España —ya sea en propiedad o en alquiler—, el residente debe gestionar el alta o el cambio de titularidad de los suministros básicos del hogar: la electricidad (cuya potencia contratada se mide en kilovatios y cuyo consumo se factura en kilovatios hora), el gas natural o butano, el agua potable (gestionada por empresas municipales o mancomunadas) y la conexión de fibra óptica y telefonía móvil.",
                "Para proteger a las familias con bajos ingresos, familias numerosas y pensionistas con pensiones mínimas, el Gobierno de España regula el «Bono Social Eléctrico» y el «Bono Social Térmico», que aplican descuentos importantes en la factura de la luz y la calefacción a través de las compañías comercializadoras de referencia (tarifa regulada PVPC). Además, para vender o alquilar cualquier vivienda en España es obligatorio disponer del Certificado de Eficiencia Energética, que califica el consumo del inmueble con una escala de letras desde la A (la más eficiente) hasta la G.",
                "En la vida diaria de los barrios españoles, los ayuntamientos gestionan el servicio público de recogida de basuras mediante contenedores diferenciados por colores que fomentan el reciclaje y la economía circular.",
                "Así, en el contenedor amarillo se depositan los envases de plástico, las latas de conserva o refresco y los envases tipo brik; en el contenedor azul se tiran exclusivamente el papel y las cajas de cartón plegadas; en el contenedor verde con forma de iglú se introducen las botellas, tarros y frascos de vidrio (sin tapones y sin mezclar con cristal de ventanas o vajilla de cerámica); y en el contenedor marrón se depositan los restos orgánicos de comida.",
                "Cuando un ciudadano necesita deshacerse de residuos especiales o voluminosos que no pueden tirarse a los contenedores de la calle —como muebles viejos, colchones, ordenadores, electrodomésticos averiados, pinturas, baterías o aceite de cocina usado—, debe llevarlos gratuitamente al «Punto Limpio» municipal de su localidad."
            ],
            "questions": [
                ("¿En qué contenedor de reciclaje de color específico deben depositarse en España las botellas de plástico, las latas metálicas y los envases tipo brik?", ["En el contenedor amarillo", "En el contenedor azul", "En el iglú verde", "En el buzón de Correos"], 0),
                ("¿Qué se deposita exclusivamente en el contenedor de reciclaje de color azul en las calles españolas?", ["El papel y el cartón", "Las botellas de vidrio", "Las pilas y baterías de coche", "Los medicamentos caducados"], 0),
                ("¿A qué instalación municipal gratuita deben llevarse los electrodomésticos viejos, muebles rotos, pinturas o aceites usados que no pueden tirarse en los contenedores normales de la calle?", ["Al Punto Limpio municipal", "Al centro de salud", "Al juzgado de guardia", "A la estación de tren"], 0)
            ],
            "vocab": [
                ("el contenedor amarillo", "noun", "yellow recycling bin (plastic packaging, cans, cartons)", "Las botellas de plástico, las latas y los briks van al contenedor amarillo."),
                ("el contenedor azul", "noun", "blue recycling bin (paper and cardboard)", "Los periódicos viejos y las cajas de cartón se depositan en el contenedor azul."),
                ("el contenedor verde", "noun", "green igloo recycling bin (glass bottles and jars)", "Las botellas y frascos de vidrio se reciclan en el contenedor verde."),
                ("el Punto Limpio", "noun", "municipal waste recycling center (for bulky or hazardous items)", "Los electrodomésticos y muebles viejos deben llevarse al Punto Limpio del ayuntamiento."),
                ("el Bono Social Eléctrico", "noun", "Social Electricity Bonus (discount for vulnerable households)", "El Bono Social Eléctrico reduce la factura de la luz a las familias vulnerables y numerosas."),
                ("el Certificado de Eficiencia Energética", "noun", "Energy Performance Certificate (rated A to G)", "Para vender o alquilar un piso en España es obligatorio tener el Certificado de Eficiencia Energética."),
                ("los suministros del hogar", "noun", "household utilities (water, electricity, gas, internet)", "El inquilino suele abonar mensualmente el consumo de los suministros del hogar."),
                ("la recogida selectiva", "noun", "separate waste collection / recycling", "La recogida selectiva de residuos protege el medio ambiente en los municipios españoles.")
            ],
            "ex_mc": [
                ("¿En qué contenedor se reciclan en España las botellas y los tarros de vidrio?", ["En el contenedor verde (iglú)", "En el contenedor amarillo", "En el contenedor azul", "En el Punto SIGRE de las librerías"], 0),
                ("¿Qué letra identifica a las viviendas con menor consumo energético y mayor respeto medioambiental en el Certificado de Eficiencia Energética?", ["La letra A", "La letra G", "La letra Z", "La letra Ñ"], 0)
            ],
            "ex_fb": [
                ("En España, el papel y el cartón se depositan para su reciclaje en el contenedor de color ___.", "azul", "In Spain, paper and cardboard are placed for recycling in the blue bin."),
                ("Los muebles viejos, electrodomésticos y aceites usados deben llevarse al ___ Limpio municipal.", "Punto", "Old furniture, appliances, and used oils must be taken to the municipal Recycling Center (Punto Limpio).")
            ],
            "ex_sb": [
                (["El", "papel", "y", "el", "cartón", "se", "depositan", "en", "el", "contenedor", "azul."], "Paper and cardboard are placed in the blue bin.")
            ],
            "ex_dict": [
                ("Los envases de plástico, las latas y los briks se reciclan en el contenedor amarillo.", "Plastic containers, cans, and cartons are recycled in the yellow bin.")
            ]
        },
        {
            "num": "05",
            "title": "El Padrón Municipal de Habitantes y el certificado de empadronamiento",
            "objective": "Comprender la importancia fundamental del Padrón Municipal en los ayuntamientos españoles y la diferencia entre volante y certificado de empadronamiento.",
            "grammar_title": "Construcciones de obligación universal y finalidad administrativa («toda persona que viva en España está obligada a inscribirse en el Padrón»)",
            "grammar_slug": "obligacion-inscripcion-padron-municipal",
            "grammar_Body": """El trámite del empadronamiento se formula en el examen CCSE con verbos pronominales y preposiciones de lugar (**empadronarse en el ayuntamiento**, **inscribirse en el Padrón Municipal**):

- *Toda persona que resida en España **tiene el derecho y el deber de inscribirse en el Padrón Municipal** del ayuntamiento donde vive.*
- *El **certificado de empadronamiento** acredita la residencia y el domicilio habitual para solicitar la tarjeta sanitaria, escolarizar a los hijos o tramitar la nacionalidad.*""",
            "story_title": "El primer trámite al llegar a un municipio español",
            "paragraphs": [
                "Uno de los trámites administrativos más importantes de la vida cotidiana en España es el «empadronamiento». El Padrón Municipal de Habitantes es el registro administrativo gestionado por cada uno de los más de ocho mil cien ayuntamientos españoles donde constan todos los vecinos que viven habitualmente en ese municipio.",
                "De acuerdo con la Ley de Bases del Régimen Local, toda persona que viva en España —ya sea ciudadano español, ciudadano de la Unión Europea o extranjero de cualquier nacionalidad— está obligada a inscribirse en el Padrón del municipio en el que resida habitualmente. Quien viva en varios municipios a lo largo del año debe inscribirse únicamente en aquel en el que habite durante más tiempo al año.",
                "Para empadronarse en el ayuntamiento (de forma presencial en las Oficinas de Atención a la Ciudadanía o por internet con certificado digital), el ciudadano solo necesita presentar su documento de identidad (DNI, NIE o pasaporte en vigor) y un documento que acredite el uso de la vivienda donde reside: la escritura de propiedad, el contrato de alquiler vigente, una factura reciente de suministros o la autorización firmada por la persona que ya figura empadronada en ese domicilio.",
                "Estar empadronado es un requisito imprescindible para acceder a los servicios públicos esenciales cerca de casa: permite obtener la Tarjeta Sanitaria Individual y tener médico de familia en el centro de salud del barrio, solicitar plaza escolar para los hijos en los colegios públicos y concertados del municipio, acceder a ayudas sociales municipales, renovar el DNI o el TIE y ejercer el derecho al voto formando parte del Censo Electoral.",
                "Cuando una administración pide demostrar dónde vive un ciudadano, el ayuntamiento expide gratuitamente o con una tasa simbólica dos tipos de documentos: el «volante de empadronamiento» (documento informativo rápido para trámites sencillos como la tarjeta sanitaria o el abono transporte) y el «certificado de empadronamiento» (documento oficial firmado por el Secretario del Ayuntamiento que hace prueba plena del domicilio ante los tribunales, el Registro Civil o el expediente de nacionalidad española por residencia)."
            ],
            "questions": [
                ("¿Cómo se llama el registro administrativo del ayuntamiento donde deben inscribirse todas las personas que viven habitualmente en un municipio español?", ["El Padrón Municipal de Habitantes", "El Registro Mercantil Central", "El Catálogo de Bienes Culturales", "El Boletín de Tráfico"], 0),
                ("¿En qué institución pública se realiza el trámite del empadronamiento cuando una persona llega a vivir a una ciudad o cambia de domicilio?", ["En el Ayuntamiento del municipio donde reside", "En el Congreso de los Diputados", "En el Museo Nacional del Prado", "En las oficinas de RENFE"], 0),
                ("¿Para cuál de los siguientes trámites cotidianos es imprescindible presentar el volante o certificado de empadronamiento?", ["Para obtener la Tarjeta Sanitaria en el centro de salud, escolarizar a los hijos o tramitar la nacionalidad por residencia", "Para comprar un billete de autobús urbano sencillo", "Para tomar un café en un bar", "Para entrar en una playa pública"], 0)
            ],
            "vocab": [
                ("el Padrón Municipal", "noun", "Municipal Register of Inhabitants", "Toda persona que reside en España debe inscribirse en el Padrón Municipal de su ayuntamiento."),
                ("empadronarse", "verb", "to register one's address at the local town hall", "Al mudarse de piso o de ciudad es obligatorio empadronarse en el nuevo domicilio."),
                ("el certificado de empadronamiento", "noun", "official certificate of municipal residence", "El certificado de empadronamiento es necesario para el expediente de nacionalidad española."),
                ("el volante de empadronamiento", "noun", "informational proof-of-address slip", "El volante de empadronamiento sirve para pedir la tarjeta sanitaria en el centro de salud."),
                ("el domicilio habitual", "noun", "habitual residence / home address", "Si una persona tiene dos viviendas, debe empadronarse donde resida más tiempo al año."),
                ("el vecino", "noun", "registered municipal resident / neighbor", "Quien se inscribe en el Padrón Municipal adquiere legalmente la condición de vecino del municipio."),
                ("la Oficina de Atención a la Ciudadanía", "noun", "Citizen Service Office (at the town hall)", "El empadronamiento se tramita en la Oficina de Atención a la Ciudadanía del ayuntamiento."),
                ("el Censo Electoral", "noun", "Electoral Roll (based on the Municipal Register)", "La Oficina del Censo Electoral elabora las listas de votantes a partir del Padrón Municipal.")
            ],
            "ex_mc": [
                ("Si un ciudadano vive seis meses al año en Madrid y cuatro meses en una casa de vacaciones en Alicante, ¿en qué municipio debe estar empadronado según la ley?", ["En el municipio en el que habite durante más tiempo al año (en este caso, Madrid)", "En los dos ayuntamientos simultáneamente", "En ninguno de los dos", "En Bruselas"], 0),
                ("¿Qué diferencia existe entre el volante y el certificado de empadronamiento?", ["El volante tiene carácter informativo para gestiones cotidianas y el certificado acredita fehacientemente la residencia ante tribunales y trámites de nacionalidad", "El volante solo sirve para conducir coches y el certificado para pilotar aviones", "El volante lo da el médico y el certificado lo da el banco", "No existe el certificado de empadronamiento en España"], 0)
            ],
            "ex_fb": [
                ("El trámite de inscribirse como vecino en el registro del ayuntamiento donde uno vive se llama ___.", "empadronamiento", "The procedure of registering as a resident in the town hall register where one lives is called empadronamiento."),
                ("El ___ Municipal de Habitantes es gestionado por cada uno de los ayuntamientos de España.", "Padrón", "The Municipal Register of Inhabitants (Padrón) is managed by each of Spain's town halls.")
            ],
            "ex_sb": [
                (["Toda", "persona", "que", "vive", "en", "España", "debe", "empadronarse", "en", "su", "ayuntamiento."], "Every person living in Spain must register their address at their town hall.")
            ],
            "ex_dict": [
                ("El certificado de empadronamiento acredita el domicilio habitual de un ciudadano en su municipio.", "The certificate of registration certifies the habitual address of a citizen in their municipality.")
            ]
        }
    ]
}


UNIT_33 = {
    "unit_num": 69,
    "slug": "documentacion",
    "title": "Documentación: DNI, NIE y Registro Civil",
    "theme": "Documentos oficiales de identidad (DNI, Pasaporte, NIE, TIE), Registro Civil y adquisición de la nacionalidad española (Tarea 5 CCSE)",
    "lessons": [
        {
            "num": "01",
            "title": "El Documento Nacional de Identidad (DNI) y el Pasaporte español",
            "objective": "Conocer las características del DNI electrónico y del Pasaporte español, la edad a partir de la cual el DNI es obligatorio (14 años) y el cuerpo que los expide (Policía Nacional).",
            "grammar_title": "Expresiones de obligatoriedad por edad («obligatorio a partir de los catorce años», «expedido por la Policía Nacional»)",
            "grammar_slug": "obligatoriedad-edad-dni-policia",
            "grammar_Body": """Para responder con precisión a las preguntas del CCSE sobre documentos de identidad españoles es fundamental dominar las preposiciones **a partir de** (edad de obligatoriedad) y **por** (órgano emisor):

- *El Documento Nacional de Identidad (DNI) **es obligatorio para todos los españoles a partir de los 14 años** de edad.*
- *Tanto el DNI como el pasaporte español **son expedidos exclusivamente por el Cuerpo Nacional de Policía** (Ministerio del Interior).*""",
            "story_title": "El documento que acredita la identidad y la nacionalidad española",
            "paragraphs": [
                "El Documento Nacional de Identidad (DNI) es el documento público, personal e intransferible que acredita oficialmente desde hace más de setenta años la identidad, los datos personales y la nacionalidad española de su titular. Cada DNI consta de un número único e invariable de ocho cifras acompañado de una letra de control al final (que coincide con su Número de Identificación Fiscal, NIF).",
                "De acuerdo con la legislación española sobre seguridad ciudadana, obtener el DNI es obligatorio para todos los ciudadanos de nacionalidad española que residan en España a partir de los catorce años (14 años) de edad. No obstante, también puede solicitarse de manera voluntaria para los niños menores de catorce años —incluso desde bebés—, lo cual resulta muy habitual cuando las familias van a viajar en avión o por países de la Unión Europea.",
                "La competencia exclusiva para la expedición y renovación tanto del DNI como del Pasaporte español corresponde a la Dirección General de la Policía (Cuerpo Nacional de Policía), dependiente del Ministerio del Interior. Para obtenerlo por primera vez es necesario pedir cita previa y acudir a una comisaría de Policía Nacional presentando una fotografía reciente en color, el volante de empadronamiento del ayuntamiento y el certificado literal de nacimiento expedido a tal efecto por el Registro Civil.",
                "En la actualidad, el DNI español es un documento electrónico de alta seguridad (DNIe / DNI 4.0) que incorpora un chip criptográfico. Este chip permite a los ciudadanos mayores de edad identificarse de forma segura por internet ante las administraciones públicas (Agencia Tributaria, Seguridad Social, DGT o ayuntamientos) y realizar firmas electrónicas con la misma validez jurídica que la firma manuscrita.",
                "Por su parte, el Pasaporte ordinario español es el documento público de viaje que acredita en el extranjero la identidad y la nacionalidad de los ciudadanos españoles fuera de las fronteras de la Unión Europea y del espacio Schengen."
            ],
            "questions": [
                ("¿A partir de qué edad es obligatorio tener el Documento Nacional de Identidad (DNI) para todos los ciudadanos españoles residentes en España?", ["A partir de los 14 años", "A partir de los 18 años", "A partir de los 6 años", "A partir de los 21 años"], 0),
                ("¿Qué cuerpo de seguridad del Estado expide el DNI y el Pasaporte en España?", ["La Policía Nacional (dependiente del Ministerio del Interior)", "La Guardia Urbana municipal", "El Ejército del Aire", "Los agentes forestales"], 0),
                ("¿Qué certificado oficial del Registro Civil debe presentarse obligatoriamente cuando se solicita el DNI español por primera vez?", ["El certificado literal de nacimiento expedido para la obtención del DNI", "El certificado de notas del colegio", "El contrato de la compañía eléctrica", "El recibo del impuesto del coche"], 0)
            ],
            "vocab": [
                ("el Documento Nacional de Identidad", "noun", "National Identity Document (DNI, mandatory from age 14)", "El Documento Nacional de Identidad acredita la nacionalidad española y es obligatorio a los catorce años."),
                ("el pasaporte", "noun", "passport", "El pasaporte español permite viajar a países situados fuera de la Unión Europea."),
                ("la Policía Nacional", "noun", "National Police Corps", "El DNI y el pasaporte se tramitan con cita previa en las comisarías de la Policía Nacional."),
                ("el DNI electrónico", "noun", "electronic ID card (DNIe with cryptographic chip)", "El chip del DNI electrónico permite firmar documentos y hacer trámites por internet."),
                ("la firma electrónica", "noun", "electronic / digital signature", "La firma electrónica tiene la misma validez legal que la firma manuscrita en papel."),
                ("la renovación", "noun", "renewal (of an official document)", "La validez del DNI es de cinco años para menores de treinta años y de diez años hasta los setenta."),
                ("el certificado literal de nacimiento", "noun", "full literal birth certificate", "Para sacar el DNI por primera vez hay que aportar el certificado literal de nacimiento del Registro Civil."),
                ("intransferible", "adjective", "non-transferable (strictly personal)", "El DNI es un documento público, personal e intransferible.")
            ],
            "ex_mc": [
                ("¿Pueden los españoles menores de 14 años obtener el DNI aunque aún no sea obligatorio para ellos?", ["Sí, pueden obtenerlo de forma voluntaria (acompañados por sus padres o tutores)", "No, está totalmente prohibido antes de cumplir los 14 años", "Solo si tienen carné de conducir", "Solo si viven fuera de Europa"], 0),
                ("¿De cuántos números y cuántas letras consta el código identificador del DNI español (por ejemplo, 12345678Z)?", ["De ocho números y una letra final de control", "De tres letras y dos números", "De veinte números sin ninguna letra", "De cinco letras únicamente"], 0)
            ],
            "ex_fb": [
                ("El Documento Nacional de Identidad (DNI) es obligatorio para todos los españoles a partir de los ___ años.", "14", "The National Identity Document (DNI) is mandatory for all Spaniards from 14 years of age."),
                ("En España, el DNI y el pasaporte son expedidos por el Cuerpo Nacional de ___.", "Policía", "In Spain, the DNI and passport are issued by the National Police Corps.")
            ],
            "ex_sb": [
                (["El", "DNI", "es", "obligatorio", "en", "España", "a", "partir", "de", "los", "catorce", "años."], "The DNI is mandatory in Spain from the age of fourteen.")
            ],
            "ex_dict": [
                ("La Policía Nacional expide el Documento Nacional de Identidad y el pasaporte español.", "The National Police issues the National Identity Document and the Spanish passport.")
            ]
        },
        {
            "num": "02",
            "title": "Documentación de residentes extranjeros: NIE, TIE y certificado de registro de la UE",
            "objective": "Distinguir el Número de Identidad de Extranjero (NIE), la Tarjeta de Identidad de Extranjero (TIE) para extracomunitarios y el Certificado de Registro de Ciudadano de la Unión Europea.",
            "grammar_title": "Distinción conceptual y funcional («el número NIE» frente a «la tarjeta física TIE»)",
            "grammar_slug": "distincion-conceptual-nie-tie-extranjeria",
            "grammar_Body": """Para evitar errores habituales en la vida administrativa y en el examen CCSE es clave distinguir tres documentos de extranjería:

- **El NIE (Número de Identidad de Extranjero)**: es el código alfanumérico personal, único e invariable (empieza por X, Y o Z, seguido de 7 dígitos y una letra) a efectos de identificación y Hacienda.
- **La TIE (Tarjeta de Identidad de Extranjero)**: es el documento físico con fotografía y huella que acredita la residencia legal en España de los ciudadanos **no pertenecientes a la Unión Europea**.
- **El Certificado de Registro de Ciudadano de la Unión**: documento verde sin foto para residentes nacionales de otro Estado miembro de la UE/EEE.""",
            "story_title": "Vivir y trabajar legalmente en España como residente extranjero",
            "paragraphs": [
                "España es un país abierto y acogedor en el que residen legalmente más de seis millones de ciudadanos procedentes tanto de otros Estados de la Unión Europea como de Iberoamérica y del resto del mundo. A toda persona extranjera que se relaciona con las administraciones españolas por motivos económicos, profesionales o de residencia se le asigna un código personal, único y exclusivo: el Número de Identidad de Extranjero (NIE).",
                "El NIE está compuesto por una letra inicial (X, Y o Z), siete números y una letra final de verificación, y sirve como número de identificación fiscal en todos los contratos de trabajo, nóminas, cuentas bancarias, compra de viviendas, pago de impuestos e inscripción en el examen CCSE del Instituto Cervantes.",
                "Sin embargo, el régimen de documentación física varía según la nacionalidad del residente. Los ciudadanos nacionales de otro Estado miembro de la Unión Europea (o de Noruega, Islandia, Liechtenstein y Suiza) tienen derecho a la libre circulación y residencia: si van a vivir en España por un periodo superior a tres meses, deben solicitar su inscripción en el Registro Central de Extranjeros de la Policía Nacional, donde se les entrega el «Certificado de Registro de Ciudadano de la Unión» (conocido popularmente como el «NIE verde»), que usan acompañado de su pasaporte o documento de identidad nacional.",
                "Por su parte, los ciudadanos procedentes de países no pertenecientes a la Unión Europea (extracomunitarios) que han obtenido un visado o una autorización para residir en España por un periodo superior a seis meses tienen la obligación de solicitar personalmente la «Tarjeta de Identidad de Extranjero» (TIE) en el plazo de un mes desde su entrada o concesión.",
                "La TIE es una tarjeta plástica biométrica con fotografía, huella dactilar y chip expedida por las Oficinas de Extranjería y la Policía Nacional que acredita la permanencia legal en España y especifica el tipo de autorización (residencia y trabajo, estudios, reagrupación familiar o residencia de larga duración tras cinco años de residencia continuada)."
            ],
            "questions": [
                ("¿Qué significan las siglas NIE en la documentación oficial española?", ["Número de Identidad de Extranjero", "Normativa Interna de Educación", "Núcleo Industrial Español", "Notificación de Impuestos Especiales"], 0),
                ("¿Cómo se llama la tarjeta física con fotografía y huella dactilar que acredita la residencia legal en España de los extranjeros no comunitarios por más de seis meses?", ["La Tarjeta de Identidad de Extranjero (TIE)", "El Documento Nacional de Identidad (DNI)", "El carné de familia numerosa", "El pasaporte diplomático"], 0),
                ("¿Qué trámite deben realizar los ciudadanos de otro país de la Unión Europea si van a residir en España durante más de tres meses?", ["Inscribirse en el Registro Central de Extranjeros y obtener el Certificado de Registro de Ciudadano de la Unión", "Pedir un visado turístico de quince días en la frontera", "Solicitar asilo político obligatorio", "Renunciar a su nacionalidad europea"], 0)
            ],
            "vocab": [
                ("el NIE", "noun", "Foreigner Identity Number (Número de Identidad de Extranjero)", "El NIE es un número único e invariable que identifica al residente extranjero ante Hacienda."),
                ("la TIE", "noun", "Foreigner Identity Card (Tarjeta de Identidad de Extranjero)", "La TIE es la tarjeta física biométrica con foto para residentes de fuera de la Unión Europea."),
                ("la Oficina de Extranjería", "noun", "Immigration Office (Subdelegación del Gobierno)", "Las autorizaciones de residencia y trabajo se tramitan en la Oficina de Extranjería."),
                ("el ciudadano de la Unión Europea", "noun", "European Union citizen", "Los ciudadanos de la Unión Europea gozan de libre circulación y residencia en España."),
                ("la residencia de larga duración", "noun", "long-term residence permit (after 5 years of legal residence)", "Tras cinco años de residencia legal y continuada se puede obtener la residencia de larga duración."),
                ("la reagrupación familiar", "noun", "family reunification", "La ley de extranjería regula el derecho a la reagrupación familiar de cónyuges e hijos."),
                ("la huella dactilar", "noun", "fingerprint", "Para expedir la tarjeta TIE es necesario acudir a la toma de huellas dactilares en la Policía."),
                ("el visado", "noun", "visa", "Los consulados de España en el exterior expiden los visados de estudios, trabajo o residencia.")
            ],
            "ex_mc": [
                ("Cuando un residente extranjero adquiere finalmente la nacionalidad española, ¿qué documento de identidad pasa a tener en lugar de su TIE?", ["El Documento Nacional de Identidad (DNI) y el Pasaporte español", "El carné de turista internacional", "Un segundo NIE con la letra W", "Ningún documento de identidad"], 0),
                ("¿Cambia el número de NIE de un residente extranjero cada vez que renueva su tarjeta TIE o cambia de domicilio en España?", ["No, el número de NIE es personal, único e invariable hasta que se adquiere la nacionalidad española", "Sí, cambia todos los meses de enero", "Sí, cambia cada vez que se muda de barrio", "Sí, cambia al cambiar de empresa"], 0)
            ],
            "ex_fb": [
                ("El código alfanumérico personal que identifica a los residentes extranjeros en España es el ___ (Número de Identidad de Extranjero).", "NIE", "The personal alphanumeric code that identifies foreign residents in Spain is the NIE (Foreigner Identity Number)."),
                ("La tarjeta física con fotografía que acredita la residencia legal de ciudadanos extracomunitarios es la ___ (Tarjeta de Identidad de Extranjero).", "TIE", "The physical card with a photograph that certifies the legal residence of non-EU citizens is the TIE (Foreigner Identity Card).")
            ],
            "ex_sb": [
                (["El", "NIE", "es", "el", "Número", "de", "Identidad", "de", "Extranjero", "en", "España."], "The NIE is the Foreigner Identity Number in Spain.")
            ],
            "ex_dict": [
                ("La Tarjeta de Identidad de Extranjero acredita la residencia legal en España de ciudadanos extracomunitarios.", "The Foreigner Identity Card certifies the legal residence in Spain of non-EU citizens.")
            ]
        },
        {
            "num": "03",
            "title": "El Registro Civil: nacimientos, matrimonios, defunciones y Libro de Familia digital",
            "objective": "Conocer las funciones del Registro Civil en España (dependiente del Ministerio de Justicia) y la gratuidad de la inscripción de nacimientos, matrimonios, defunciones y nacionalidad.",
            "grammar_title": "Verbos de inscripción registral y estado civil («inscribir el nacimiento», «contraer matrimonio»)",
            "grammar_slug": "inscripcion-registral-estado-civil",
            "grammar_Body": """Para expresar los actos jurídicos que afectan al estado civil de las personas en España se utilizan colocaciones formales con el **Registro Civil**:

- *El nacimiento de un hijo **se inscribe en el Registro Civil** (actualmente también desde el propio hospital) en un plazo de **24 horas a 8 días** (ampliable a 30 días).*
- *El Registro Civil **depende del Ministerio de Justicia** y todos sus trámites y certificados **son gratuitos**.*""",
            "story_title": "El archivo público de la biografía legal de los ciudadanos",
            "paragraphs": [
                "El Registro Civil es un servicio público esencial dependiente del Ministerio de Justicia encargado de dejar constancia oficial de los hechos y actos que conciernen al estado civil de todas las personas: el nacimiento y el nombre y apellidos, la filiación, el matrimonio, el régimen económico matrimonial, el divorcio, la tutela, la adquisición de la nacionalidad española y la defunción.",
                "En España existen Oficinas del Registro Civil en todos los municipios y partidos judiciales, así como Registros Civiles Consulares en las embajadas y consulados de España en el extranjero y un Registro Civil Central en Madrid. Todos los trámites, inscripciones y expediciones de certificados (como las partidas o certificados literales de nacimiento, matrimonio o defunción) realizados ante el Registro Civil son totalmente gratuitos.",
                "Cuando nace un bebé en España, es obligatorio inscribir su nacimiento en el Registro Civil entre las veinticuatro horas (24 horas) y los ocho días (8 días) siguientes al parto (plazo que puede ampliarse hasta treinta días cuando exista causa justificada). Hoy en día, gracias a la digitalización, los padres pueden realizar la comunicación del nacimiento directamente desde el propio hospital público o privado dentro de las primeras 72 horas sin necesidad de desplazarse al juzgado.",
                "En cuanto al nombre y los apellidos, la ley española establece que toda persona tiene dos apellidos —correspondientes al primero de cada uno de sus dos progenitores—, pudiendo los padres elegir de común acuerdo el orden de transmisión de los apellidos antes de la inscripción del primer hijo (orden que se mantendrá después para todos los hermanos).",
                "Con la entrada en vigor de la nueva Ley del Registro Civil (sistema DICIREG), el tradicional «Libro de Familia» físico de tapas azules o rojas ha sido sustituido por un registro individual electrónico único para cada ciudadano, del cual se pueden descargar en el acto certificaciones digitales con código seguro de verificación."
            ],
            "questions": [
                ("¿De qué ministerio del Gobierno de España depende el Registro Civil?", ["Del Ministerio de Justicia", "Del Ministerio de Agricultura, Pesca y Alimentación", "Del Ministerio de Industria y Turismo", "Del Ministerio de Vivienda"], 0),
                ("¿En qué institución pública deben inscribirse obligatoriamente los nacimientos, los matrimonios, las adquisiciones de nacionalidad y las defunciones en España?", ["En el Registro Civil", "En el Registro de la Propiedad Inmobiliaria", "En el Catastro Municipal", "En el Banco de España"], 0),
                ("¿Cuántos apellidos tienen legalmente los ciudadanos españoles inscritos en el Registro Civil?", ["Dos apellidos (el primero de cada uno de los dos progenitores, en el orden elegido por estos)", "Un solo apellido obligatorio del abuelo", "Cuatro apellidos en un solo bloque", "Ningún apellido hasta cumplir los 18 años"], 0)
            ],
            "vocab": [
                ("el Registro Civil", "noun", "Civil Registry (births, marriages, deaths, nationality)", "El Registro Civil depende del Ministerio de Justicia y todos sus certificados son gratuitos."),
                ("el estado civil", "noun", "marital / civil status (soltero, casado, divorciado, viudo)", "El Registro Civil da fe de los actos relativos al estado civil de las personas."),
                ("la inscripción de nacimiento", "noun", "birth registration", "Hoy en día la inscripción de nacimiento del bebé puede tramitarse desde el propio hospital."),
                ("el matrimonio civil", "noun", "civil marriage", "En España el matrimonio civil puede celebrarse en el Registro Civil, el ayuntamiento o ante notario."),
                ("la defunción", "noun", "death (formal / legal)", "El certificado de defunción es necesario para tramitar pensiones de viudedad y herencias."),
                ("la filiación", "noun", "legal parentage / filiation", "La filiación determina los apellidos y la patria potestad de los progenitores sobre sus hijos."),
                ("el Registro Civil Consular", "noun", "Consular Civil Registry (at Spanish embassies/consulates abroad)", "Los españoles residentes en el extranjero inscriben a sus hijos en el Registro Civil Consular."),
                ("los apellidos", "noun", "surnames (two surnames in Spain)", "En España cada persona lleva dos apellidos: uno de cada progenitor.")
            ],
            "ex_mc": [
                ("¿Cuál es el coste de solicitar un certificado literal de nacimiento o de matrimonio en el Registro Civil español?", ["Es totalmente gratuito", "Cuesta 150 euros", "Cuesta el 10 % del sueldo mensual", "Solo es gratuito los años bisiestos"], 0),
                ("¿Ante qué autoridades puede contraerse matrimonio civil con plenos efectos legales en España?", ["Ante el encargado del Registro Civil, el alcalde o concejal del ayuntamiento, o ante notario", "Únicamente ante el director de un banco", "Ante el presidente de la comunidad de vecinos", "Ante el médico de familia del centro de salud"], 0)
            ],
            "ex_fb": [
                ("Los nacimientos, matrimonios, defunciones y la nacionalidad española se inscriben en el ___ Civil.", "Registro", "Births, marriages, deaths, and Spanish nationality are registered in the Civil Registry."),
                ("El Registro Civil depende del Ministerio de ___ y todos sus certificados son gratuitos.", "Justicia", "The Civil Registry reports to the Ministry of Justice and all its certificates are free.")
            ],
            "ex_sb": [
                (["Los", "nacimientos", "y", "los", "matrimonios", "se", "inscriben", "en", "el", "Registro", "Civil."], "Births and marriages are registered in the Civil Registry.")
            ],
            "ex_dict": [
                ("En España todas las personas tienen dos apellidos, uno de cada progenitor.", "In Spain everyone has two surnames, one from each parent.")
            ]
        },
        {
            "num": "04",
            "title": "Adquisición de la nacionalidad española: plazos de residencia, CCSE, DELE y jura",
            "objective": "Conocer los requisitos y plazos legales para adquirir la nacionalidad española por residencia (10, 5, 2 y 1 año), las pruebas del Instituto Cervantes (CCSE y DELE A2) y el acto de jura o promesa.",
            "grammar_title": "Condicionales y plazos legales diferenciados («diez años con carácter general», «dos años para iberoamericanos»)",
            "grammar_slug": "plazos-legales-nacionalidad-residencia",
            "grammar_Body": """El artículo 22 del Código Civil establece distintos plazos de residencia legal, continuada e inmediatamente anterior a la petición para adquirir la **nacionalidad española por residencia**:

- **10 años**: plazo general.
- **5 años**: personas que hayan obtenido la condición de **refugiado**.
- **2 años**: nacionales de origen de **países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes**.
- **1 año**: nacido en territorio español, o **casado desde hace un año con un español/a** (sin estar separado), o viudo/a de español/a, o nacido fuera de España de padre/madre o abuelo/a originariamente españoles.""",
            "story_title": "El camino hacia la plena ciudadanía española",
            "paragraphs": [
                "De acuerdo con el artículo 11 de la Constitución y con el Código Civil español, la nacionalidad española se adquiere de origen (por ejemplo, los nacidos de padre o madre españoles) o de forma derivativa, siendo la vía más frecuente la adquisición de la «nacionalidad española por residencia», cuya concesión corresponde al Ministerio de Justicia.",
                "Para solicitar la nacionalidad por residencia es necesario haber residido en España de forma legal, continuada e inmediatamente anterior a la solicitud durante los plazos fijados por la ley: diez años (10 años) como regla general; cinco años (5 años) para quienes hayan obtenido el estatuto de refugiado; dos años (2 años) para los nacionales de origen de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o personas de origen sefardí; y tan solo un año (1 año) para quien haya nacido en territorio español o lleve un año casado legalmente con un ciudadano o ciudadana español.",
                "Además de acreditar buena conducta cívica (mediante los certificados de antecedentes penales de España y del país de origen), los solicitantes mayores de dieciocho años deben superar las dos pruebas oficiales administradas por el Instituto Cervantes para demostrar su suficiente grado de integración en la sociedad española: la prueba de Conocimientos Constitucionales y Socioculturales de España (CCSE) y, si su lengua oficial materna no es el español, el examen de idioma DELE de nivel A2 o superior (estando exentos del DELE los nacionales de países hispanohablantes y quienes hayan obtenido el título de la ESO o superior en España).",
                "Una vez que el Ministerio de Justicia dicta la resolución favorable de concesión de la nacionalidad española, el solicitante dispone de un plazo de ciento ochenta días (180 días) para realizar el solemne acto de «jura o promesa» ante el Registro Civil o ante un notario.",
                "En ese acto final, el nuevo ciudadano jura o promete fidelidad al Rey y obediencia a la Constitución Española y a las leyes, se inscribe su nacimiento como español en el Registro Civil (manteniendo su doble nacionalidad si procede de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o Francia) y con ese certificado acude a la Policía Nacional a obtener su DNI y su Pasaporte español."
            ],
            "questions": [
                ("¿Cuál es el plazo general de residencia legal y continuada en España exigido para solicitar la nacionalidad española, y a cuántos años se reduce para los ciudadanos de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes?", ["10 años con carácter general, y se reduce a 2 años para iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes", "20 años general y 15 años para iberoamericanos", "6 meses general y 1 mes para iberoamericanos", "50 años para todos sin excepción"], 0),
                ("¿Cuántos años de residencia legal y continuada necesita una persona extranjera que lleva un año casada con un ciudadano o ciudadana español (y no está separada) para poder solicitar la nacionalidad española?", ["1 año de residencia legal", "10 años de residencia legal", "5 años de residencia legal", "8 años de residencia legal"], 0),
                ("¿Qué se jura o promete obligatoriamente ante el Registro Civil o el notario en el acto final para adquirir la nacionalidad española por residencia?", ["Fidelidad al Rey y obediencia a la Constitución y a las leyes", "No viajar nunca fuera de España", "Aprender de memoria todas las carreteras nacionales", "Comprar una vivienda en Madrid"], 0)
            ],
            "vocab": [
                ("la nacionalidad por residencia", "noun", "Spanish nationality by residence", "El Ministerio de Justicia resuelve los expedientes de nacionalidad por residencia."),
                ("la prueba CCSE", "noun", "Constitutional and Sociocultural Knowledge of Spain test", "Superar la prueba CCSE del Instituto Cervantes acredita la integración en la sociedad española."),
                ("la buena conducta cívica", "noun", "good civic conduct (no criminal record)", "Para obtener la nacionalidad española es requisito acreditar buena conducta cívica."),
                ("la jura de nacionalidad", "noun", "oath or affirmation of allegiance for nationality", "La jura o promesa de nacionalidad puede realizarse en el Registro Civil o ante notario."),
                ("la doble nacionalidad", "noun", "dual nationality / dual citizenship", "Los ciudadanos iberoamericanos conservan su nacionalidad de origen al adquirir la española."),
                ("sefardí", "adjective", "Sephardic (descendant of Spanish Jews)", "Las personas de origen sefardí pueden solicitar la nacionalidad tras dos años de residencia."),
                ("el estatuto de refugiado", "noun", "refugee status", "Quienes tienen reconocido el estatuto de refugiado pueden pedir la nacionalidad a los cinco años."),
                ("la obediencia a la Constitución", "noun", "obedience to the Constitution and the laws", "El nuevo ciudadano jura o promete fidelidad al Rey y obediencia a la Constitución y a las leyes.")
            ],
            "ex_mc": [
                ("¿Qué ministerio del Gobierno de España es el encargado de conceder la nacionalidad española por residencia?", ["El Ministerio de Justicia", "El Ministerio de Transportes", "El Ministerio de Cultura", "El Ministerio de Sanidad"], 0),
                ("¿Están obligados los ciudadanos nacionales de países hispanohablantes de Iberoamérica a realizar el examen de idioma DELE A2 para solicitar la nacionalidad española?", ["No, están exentos del examen DELE por tener el español como lengua oficial (solo deben realizar la prueba CCSE)", "Sí, deben hacer el examen DELE C2 obligatorio", "Sí, y además un examen de francés", "No necesitan hacer ni DELE ni CCSE ni ningún trámite"], 0)
            ],
            "ex_fb": [
                ("Los ciudadanos de origen de países iberoamericanos, Portugal, Filipinas o Andorra pueden solicitar la nacionalidad española tras ___ años de residencia legal.", "2", "Citizens of origin from Ibero-American countries, Portugal, the Philippines, or Andorra can apply for Spanish nationality after 2 years of legal residence."),
                ("Para adquirir la nacionalidad española es obligatorio jurar o prometer fidelidad al Rey y obediencia a la ___ y a las leyes.", "Constitución", "To acquire Spanish nationality it is mandatory to swear or affirm allegiance to the King and obedience to the Constitution and the laws.")
            ],
            "ex_sb": [
                (["El", "Ministerio", "de", "Justicia", "concede", "la", "nacionalidad", "española", "por", "residencia."], "The Ministry of Justice grants Spanish nationality by residence.")
            ],
            "ex_dict": [
                ("Al adquirir la nacionalidad se jura o promete fidelidad al Rey y obediencia a la Constitución.", "Upon acquiring nationality, one swears or affirms allegiance to the King and obedience to the Constitution.")
            ]
        },
        {
            "num": "05",
            "title": "El carné de conducir (DGT), la Apostilla de La Haya y los certificados electrónicos",
            "objective": "Conocer el funcionamiento del permiso de conducir por puntos (DGT), el canje de permisos extranjeros, la Apostilla de La Haya y la administración electrónica (Cl@ve).",
            "grammar_title": "Estructuras de equivalencia y validación internacional («el canje del permiso», «legalizar mediante la Apostilla»)",
            "grammar_slug": "equivalencia-canje-apostilla-administracion",
            "grammar_Body": """Para explicar la validez de documentos extranjeros y la administración electrónica española se emplean sustantivos técnicos precisos:

- **El canje del permiso de conducir**: cambio de un carné extranjero por el permiso español equivalente ante la **Dirección General de Tráfico (DGT)** cuando existe convenio bilateral.
- **La Apostilla de La Haya**: sello internacional que certifica la autenticidad de los documentos públicos extranjeros (como partidas de nacimiento o antecedentes penales).
- **El sistema Cl@ve y el Certificado Digital (FNMT)**: permiten realizar trámites en la **Sede Electrónica** las 24 horas.""",
            "story_title": "Conducir con seguridad y gestionar trámites desde casa",
            "paragraphs": [
                "Otro documento oficial de gran importancia en la vida diaria es el permiso o carné de conducir, expedido en toda España por la Dirección General de Tráfico (DGT), organismo autónomo dependiente del Ministerio del Interior. Para obtener el permiso de la clase B (automóviles turismos) es necesario tener al menos dieciocho años (18 años), superar un reconocimiento psicotécnico médico y aprobar en la Jefatura Provincial de Tráfico un examen teórico sobre seguridad vial y un examen práctico de circulación.",
                "En España funciona el sistema del «permiso por puntos»: un conductor novel comienza con 8 puntos y, si no comete infracciones, pasa a tener 12 puntos y hasta un máximo de 15 puntos. Cometer infracciones graves —como conducir superando los límites de velocidad, utilizar el teléfono móvil con la mano al volante, no llevar puesto el cinturón de seguridad o superar la tasa de alcoholemia— conlleva multas económicas y la pérdida de puntos.",
                "Además, todo vehículo que circula por España debe tener contratado obligatoriamente un seguro de responsabilidad civil, abonar el impuesto municipal de circulación y superar periódicamente la Inspección Técnica de Vehículos (ITV). Los residentes extranjeros procedentes de la Unión Europea o de los más de veinte países de Iberoamérica y del mundo que tienen convenio con España pueden solicitar ante la DGT el «canje» de su permiso de conducir nacional por el permiso español.",
                "Cuando un ciudadano presenta documentos públicos extranjeros en un expediente español (como su certificado de nacimiento o de antecedentes penales para la nacionalidad), estos documentos deben estar debidamente legalizados o llevar el sello de la «Apostilla de La Haya» y, si no están redactados en español, ir acompañados de una traducción oficial firmada por un Traductor-Intérprete Jurado nombrado por el Ministerio de Asuntos Exteriores.",
                "Por último, España cuenta con una administración pública altamente digitalizada: mediante el Certificado Digital de la Fábrica Nacional de Moneda y Timbre (FNMT), el DNI electrónico o el sistema «Cl@ve» en el teléfono móvil, cualquier ciudadano puede presentar su solicitud de nacionalidad, pedir certificados del Registro Civil o consultar sus puntos de la DGT desde casa las veinticuatro horas del día."
            ],
            "questions": [
                ("¿Qué organismo dependiente del Ministerio del Interior expide los permisos de conducir y regula la seguridad vial en España?", ["La Dirección General de Tráfico (DGT)", "La Sociedad Estatal de Correos", "El Instituto Nacional de Estadística (INE)", "El Museo Reina Sofía"], 0),
                ("¿Cuál es la edad mínima legal en España para obtener el permiso de conducir de coches turismos (permiso de la clase B)?", ["18 años", "14 años", "16 años sin examen", "21 años"], 0),
                ("¿Cómo se llama la revisión técnica obligatoria que deben pasar periódicamente los automóviles en España para comprobar que sus frenos, luces y emisiones son seguros para circular?", ["La Inspección Técnica de Vehículos (ITV)", "La Prueba de Acceso a la Universidad (PAU)", "La Declaración de la Renta (IRPF)", "El Censo Electoral"], 0)
            ],
            "vocab": [
                ("la Dirección General de Tráfico", "noun", "Directorate-General for Traffic (DGT)", "La Dirección General de Tráfico gestiona los exámenes de conducir y el carné por puntos."),
                ("el permiso por puntos", "noun", "points-based driving license", "Usar el teléfono móvil mientras se conduce supone la pérdida de puntos del carné."),
                ("la ITV", "noun", "Technical Vehicle Inspection / MOT (Inspección Técnica de Vehículos)", "Los coches de más de cuatro años deben pasar periódicamente la revisión de la ITV."),
                ("el canje del permiso de conducir", "noun", "exchange of a foreign driving license for a Spanish one", "España tiene convenios de canje del permiso de conducir con numerosos países iberoamericanos."),
                ("la Apostilla de La Haya", "noun", "Hague Apostille (international document authentication stamp)", "Los documentos extranjeros para el trámite de nacionalidad deben llevar la Apostilla de La Haya."),
                ("el traductor jurado", "noun", "sworn / certified translator", "Los documentos redactados en otro idioma deben ser traducidos por un traductor jurado oficial."),
                ("el sistema Cl@ve", "noun", "Cl@ve electronic identification system for public administration", "El sistema Cl@ve y el certificado digital permiten realizar trámites por internet sin hacer cola."),
                ("los antecedentes penales", "noun", "criminal record certificate", "Para solicitar la nacionalidad española se exige carecer de antecedentes penales.")
            ],
            "ex_mc": [
                ("¿Con cuántos puntos iniciales comienza un conductor novel al obtener su primer carné de conducir en España y hasta qué máximo puede llegar si no comete infracciones?", ["Comienza con 8 puntos (pasa luego a 12) y puede llegar hasta un máximo de 15 puntos", "Comienza con 100 puntos y llega a 500", "Comienza con 1 punto y nunca sube", "El carné de conducir español no tiene puntos"], 0),
                ("¿Qué seguro es obligatorio por ley para que cualquier coche o motocicleta pueda circular por las calles y carreteras de España?", ["El seguro obligatorio de responsabilidad civil del vehículo", "Un seguro privado de viajes aéreos", "Un seguro de incendios forestales", "Ningún seguro es obligatorio"], 0)
            ],
            "ex_fb": [
                ("El organismo público encargado de expedir el carné de conducir en España es la Dirección General de ___ (DGT).", "Tráfico", "The public body responsible for issuing driving licenses in Spain is the Directorate-General for Traffic (DGT)."),
                ("La revisión obligatoria del estado mecánico y de seguridad de los automóviles se conoce por las siglas ___ (Inspección Técnica de Vehículos).", "ITV", "The mandatory inspection of the mechanical and safety condition of cars is known by the acronym ITV (Technical Vehicle Inspection).")
            ],
            "ex_sb": [
                (["La", "Dirección", "General", "de", "Tráfico", "expide", "el", "permiso", "de", "conducir."], "The Directorate-General for Traffic issues the driving license.")
            ],
            "ex_dict": [
                ("Para conducir un automóvil en España es obligatorio tener dieciocho años y el permiso de conducir.", "To drive a car in Spain it is mandatory to be eighteen years old and hold a driving license.")
            ]
        }
    ]
}


if __name__ == "__main__":
    for u in (UNIT_31, UNIT_32, UNIT_33):
        emit_unit_from_dict(u)
    print("Units 31, 32, and 33 generated successfully.")
