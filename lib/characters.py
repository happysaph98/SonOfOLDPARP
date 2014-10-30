# -*- coding: utf-8 -*-

CHARACTER_GROUPS = [
    'Special/Other',
    'Humans',
    'Post-scratch Trolls',
    'Pre-scratch Trolls',
    'Guardians',
    'Sprites',
    'Ancestors',
    'Midnight Crew',
]

CHARACTERS = {
    'Special/Other': [
        'Anonymous/Other',
        'Original Character',
        'Trickster',
        'Doc Scratch',
        'AR/Hal',
        'Calliope',
        'Caliborn',
        'Lord English',
        'Other (canon)',
    ],
    'Humans': [
        'John',
        'Rose',
        'Dave',
        'Jade',
        'Jane',
        'Roxy',
        'Dirk',
        'Jake',
    ],
    'Post-scratch Trolls': [
        'Aradia (dead)',
        'Aradia',
        'Aradiabot',
        'Tavros',
        'Sollux',
        'Sollux (blind)',
        'Karkat',
        'Nepeta',
        'Kanaya',
        'Terezi',
        'Vriska',
        'Equius',
        'Gamzee',
        'Gamzee (sober)',
        'Eridan',
        'Feferi',
    ],
    'Pre-scratch Trolls': [
        'Damara',
        'Rufioh',
        'Mituna',
        'Kankri',
        'Meulin',
        'Porrim',
        'Latula',
        'Aranea',
        'Horuss',
        'Kurloz',
        'Cronus',
        'Meenah',
    ],
    'Guardians': [
        'Dad',
        'Nanna',
        'Mom',
        'Bro',
        'Grandpa',
        'Poppop',
        'Alpha Mom',
        'Alpha Bro',
        'Grandma',
    ],
    'Sprites': [
        'Nannasprite',
        'Jaspersprite',
        'Davesprite',
        'Jadesprite',
        'Aradiasprite',
        'Tavrisprite',
        'Fefetasprite',
        'Erisolsprite',
        'ARquiusprite',
    ],
    'Ancestors': [
        'The Handmaid',
        'The Summoner',
        'The Psiioniic',
        'The Helmsman',
        'The Signless',
        'The Disciple',
        'The Dolorosa',
        'Redglare',
        'Mindfang',
        'Darkleer',
        'Grand Highblood',
        'Dualscar',
        'The Condesce',
    ],
    'Midnight Crew': [
        'Spades Slick',
        'Clubs Deuce',
        'Diamonds Droog',
        'Hearts Boxcars',
    ],
}

# XXX THIS IS JUST A DUPLICATE OF CHARACTERS.JS
# XXX also fix the goddamn indentation

CHARACTER_DETAILS = {
    'anonymous/other': {
        'acronym': '??',
        'name': 'anonymous',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': r'[]'
    },
    'original character': {
        'acronym': '**',
        'name': 'Original Character',
        'color': 'FF00FF',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
    },
    'trickster': {
        'acronym': '??',
        'name': 'Trickster',
        'color': 'FFAC9F',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
    },
    'doc scratch': {
        'acronym': '',
        'name': 'Doc Scratch',
        'color': 'FFFFFF',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'ar/hal': {
        'acronym': 'TT',
        'name': 'Lil Hal',
        'color': 'E00707',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'calliope': {
        'acronym': 'UU',
        'name': 'uranianUmbra',
        'color': '929292',
        'quirk_prefix': '',
        'case': 'lower',
        'replacements': '[]'
	},
    'caliborn': {
        'acronym': 'uu',
        'name': 'undyingUmbrage',
        'color': '323232',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
		},
    'lord english': {
        'acronym': 'LE',
        'name': 'Lord English',
        'color': '2ED73A',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'other (canon)': {
        'acronym': '??',
        'name': 'Other (canon)',
        'color': 'ff83fb',
        'quirk_prefix': '',
        'case': 'normal',
		'replacements': '[]'
	},
    'john': {
        'acronym': 'EB',
        'name': 'ectoBiologist',
        'color': '0715CD',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'rose': {
        'acronym': 'TT',
        'name': 'tentacleTherapist',
        'color': 'B536DA',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'dave': {
        'acronym': 'TG',
        'name': 'turntechGodhead',
        'color': 'E00707',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'	
	},
    'jade': {
        'acronym': 'GG',
        'name': 'gardenGnostic',
        'color': '4AC925',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'jane': {
        'acronym': 'GG',
        'name': 'gutsyGumshoe',
        'color': '00D5F2',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'roxy': {
        'acronym': 'TG',
        'name': 'tipsyGnostalgic',
        'color': 'FF6FF2',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'dirk': {
        'acronym': 'TT',
        'name': 'timaeusTestified',
        'color': 'F2A400',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'jake': {
        'acronym': 'GT',
        'name': 'golgothasTerror',
        'color': '1F9400',
        'quirk_prefix': '',
        'case': 'normal',
       'replacements': '[]'
	},
    'aradia (dead)': {
        'acronym': 'AA',
        'name': 'apocalypseArisen',
        'color': 'A10000',
        'quirk_prefix': '',
        'case': 'lower',
        'replacements': '[]'
	},
    'aradia': {
        'acronym': 'AA',
        'name': 'apocalypseArisen',
        'color': 'A10000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'aradiabot': {
        'acronym': 'AA',
        'name': 'apocalypseArisen',
        'color': '000056',
        'quirk_prefix': '',
        'case': 'lower',
        'replacements': '[]'
	},
    'tavros': {
        'acronym': 'AT',
        'name': 'adiosToreador',
        'color': 'A15000',
        'quirk_prefix': '',
        'case': 'inverted',
        'replacements': '[]'
	},
    'sollux': {
        'acronym': 'TA',
        'name': 'twinArmageddons',
        'color': 'A1A100',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'sollux (blind)': {
        'acronym': 'TA',
        'name': 'twinArmageddons',
        'color': 'A1A100',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'karkat': {
        'acronym': 'CG',
        'name': 'carcinoGeneticist',
        'color': '626262',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'nepeta': {
        'acronym': 'AC',
        'name': 'arsenicCatnip',
        'color': '416600',
        'quirk_prefix': ':33 <',
        'case': 'normal',
        'replacements': '[]'
	},
    'kanaya': {
        'acronym': 'GA',
        'name': 'grimAuxiliatrix',
        'color': '008141',
        'quirk_prefix': '',
        'case': 'title',
        'replacements': '[]'
	},
    'terezi': {
        'acronym': 'GC',
        'name': 'gallowsCalibrator',
        'color': '008282',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'vriska': {
        'acronym': 'AG',
        'name': 'arachnidsGrip',
        'color': '005682',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'equius': {
        'acronym': 'CT',
        'name': 'centaursTesticle',
        'color': '000056',
        'quirk_prefix': 'D -->',
        'case': 'normal',
        'replacements': '[]'
	},
    'gamzee': {
        'acronym': 'TC',
        'name': 'terminallyCapricious',
        'color': '2B0057',
        'quirk_prefix': '',
        'case': 'alternating',
        'replacements': '[]'
	},
    'gamzee (sober)': {
        'acronym': 'TC',
        'name': 'terminallyCapricious',
        'color': '2B0057',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
    },
    'eridan': {
        'acronym': 'CA',
        'name': 'caligulasAquarium',
        'color': '6A006A',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'feferi': {
        'acronym': 'CC',
        'name': 'cuttlefishCuller',
        'color': '77003C',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'damara': {
        'acronym': 'DAMARA',
        'name': 'Damara',
        'color': 'A10000',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'rufioh': {
        'acronym': 'RUFIOH',
        'name': 'Rufioh',
        'color': 'A15000',
        'quirk_prefix': '',
        'case': 'lower',
        'replacements': '[]'
	},
    'mituna':{
        'acronym': 'MITUNA',
        'name': 'Mituna',
        'color': 'A1A100',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'kankri':{
        'acronym': 'KANKRI',
        'name': 'Kankri',
        'color': 'FF0000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'meulin': {
        'acronym': 'MEULIN',
        'name': 'Meulin',
        'color': '416600',
        'quirk_prefix': '(^･ω･^) <',
        'case': 'upper',
        'replacements': '[]'
	},
    'porrim':{
        'acronym':'PORRIM',
        'name':'Porrim',
        'color':'008141',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'latula': {
        'acronym': 'LATULA',
        'name': 'Latula',
        'color': '008282',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'aranea': {
        'acronym': 'ARANEA',
        'name': 'Aranea',
        'color': '005682',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'horuss': {
        'acronym': 'HORUSS',
        'name': 'Horuss',
        'color': '000056',
        'quirk_prefix': '8=D <',
        'case': 'normal',
        'replacements': '[]'
	},
    'kurloz': {
        'acronym': 'KURLOZ',
        'name': 'Kurloz',
        'color': '2B0057',
        'quirk_prefix': 'SIGNS: <',
        'case': 'upper',
        'replacements': '[]'
	},
    'cronus': {
        'acronym': 'CRONUS',
        'name': 'Cronus',
        'color': '6A006A',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'meenah': {
        'acronym': 'MEENAH',
        'name': 'Meenah',
        'color': '77003C',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'dad': {
        'acronym': 'pipefan413',
        'name': 'Dad',
        'color': '4B4B4B',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'nanna': {
        'acronym': 'NANNA',
        'name': 'Nanna',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'mom': {
        'acronym': 'MOM',
        'name': 'Mom',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'bro': {
        'acronym': 'BRO',
        'name': 'Bro',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'grandpa': {
        'acronym': 'GRANDPA',
        'name': 'Grandpa',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'poppop': {
        'acronym': 'POPPOP',
        'name': 'Poppop',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'alpha mom': {
        'acronym': 'MOM',
        'name': 'Mom',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'alpha bro': {
        'acronym': 'BRO',
        'name': 'Bro',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'grandma': {
        'acronym': 'GRANDMA',
        'name': 'Grandma',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'nannasprite': {
        'acronym': 'NANNASPRITE',
        'name': 'Nannasprite',
        'color': '00D5F2',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'jaspersprite': {
        'acronym': 'JASPERSPRITE',
        'name': 'Jaspersprite',
        'color': 'F141EF',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
	# XXX GOTTA REMOVE THIS AT SOME POINT
    'calsprite': {
        'acronym': 'CALSPRITE',
        'name': 'Calsprite',
        'color': 'F2A400',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
	# XXX END STUFF THAT NEEDS REMOVING
    'davesprite': {
        'acronym': 'DAVESPRITE',
        'name': 'Davesprite',
        'color': 'F2A400',
        'quirk_prefix': '',
        'case': 'normal',
		'replacements': '[]'
	},
    'jadesprite': {
        'acronym': 'JADESPRITE',
        'name': 'Jadesprite',
        'color': '1F9400',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'aradiasprite': {
        'acronym': 'ARADIASPRITE',
        'name': 'Aradiasprite',
        'color': 'A10000',
        'quirk_prefix': '',
        'case': 'lower',
       'replacements': '[]'
	},
    'tavrisprite': {
        'acronym': 'TAVRISPRITE',
        'name': 'Tavrisprite',
        'color': '0715CD',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'fefetasprite': {
        'acronym': 'FEFETASPRITE',
        'name': 'Fefetasprite',
        'color': 'B536DA',
        'quirk_prefix': '3833 <',
        'case': 'normal',
        'replacements': '[]'
	},
    'erisolsprite': {
        'acronym': 'ERISOLSPRITE',
        'name': 'Erisolsprite',
        'color': '4AC925',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'arquiusprite': {
        'acronym': 'ARQUIUSPRITE',
        'name': 'ARquiusprite',
        'color': 'e00707',
        'quirk_prefix': '◥▶◀◤ —>',
        'case': 'normal',
        'replacements': '[]'
	},
    'the handmaid': {
        'acronym': '♈',
        'name': 'The Handmaid',
        'color': 'A10000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the summoner': {
        'acronym': '♉',
        'name': 'The Summoner',
        'color': 'A15000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the psiioniic':{
        'acronym': '♊',
        'name': 'The Ψiioniic',
        'color': 'A1A100',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the helmsman': {
        'acronym': '♊',
        'name': 'The Helmsman',
        'color': 'A1A100',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'the signless': {
        'acronym': '♋',
        'name': 'The Signless',
        'color': '626262',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the disciple': {
        'acronym': '♌',
        'name': 'The Disciple',
        'color': '416600',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the dolorosa': {
        'acronym': '♍',
        'name': 'The Dolorosa',
        'color': '008141',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'redglare': {
        'acronym': '♎',
        'name': 'Neophyte Redglare',
        'color': '008282',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'mindfang': {
        'acronym': '♏',
        'name': 'Marquise Spinneret Mindfang',
        'color': '005682',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'darkleer': {
        'acronym': '♐',
        'name': 'E%ecutor Darkleer',
        'color': '000056',
        'quirk_prefix': '-+->',
        'case': 'normal',
        'replacements': '[]'
	},
    'grand highblood': {
        'acronym': '♑',
        'name': 'The Grand Highblood',
        'color': '2B0057',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'dualscar': {
        'acronym': '♒',
        'name': 'Orphaner Dualscar',
        'color': '6A006A',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'the condesce': {
        'acronym': '♓',
        'name': 'Her Imperious Condescension',
        'color': '77003C',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'spades slick': {
        'acronym': '♠',
        'name': 'Spades Slick',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'lower',
        'replacements': '[]'
	},
    'clubs deuce': {
        'acronym': '♣',
        'name': 'Clubs Deuce',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	},
    'diamonds droog': {
        'acronym': '♦',
        'name': 'Diamonds Droog',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'normal',
        'replacements': '[]'
	},
    'hearts boxcars': {
        'acronym': '♥',
        'name': 'Hearts Boxcars',
        'color': '000000',
        'quirk_prefix': '',
        'case': 'upper',
        'replacements': '[]'
	}
}

