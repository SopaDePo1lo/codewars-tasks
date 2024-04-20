class Passport:


    _id: int
    nation: str
    name: str
    date_of_birth: str
    _sex: str
    _iss: str
    _exp_date: str

    def __init__(self, _buf) -> None:
        _buf = _buf.split('\n')
        _dict = {_i.split(':')[0] : _i.split(': ')[1] for _i in _buf}
        match _dict.keys:
            case 'ID#':
                self._id = _dict['ID#']
            case 'NATION':
                self.nation = _dict['NATION']
            case 'NAME':
                self.name = _dict['NAME']
            case 'DOB':
                self.date_of_birth = _dict['DOB']
            case 'SEX':
                self._sex = _dict['SEX']
            case 'IIS':
                self._iss = _dict['ISS']
            case 'EXP':
                self._exp_date = _dict['EXP']


# josef = {
    # "passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
# }

class Inspector:

    countries = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation']
    allow_citizens = []
    deny_citizens = []
    wanted = []
    rules = {}

    def get_rules(self):
        for rule in self.rules.keys():
            print(f'{rule} {self.rules[rule]}')
        print(f'Allow citizens of {self.allow_citizens}\nDeny citizens of {self.deny_citizens}')


    def receive_bulletin(self, bulletin: str):
        bulletin_buf = bulletin.split('\n')
        for issue in bulletin_buf:
            self.parse_bulletin(issue)


    def inspect(self, data):
        _passport = Passport(data['passport'])
        pass


    def parse_bulletin(self, _buf):
        if 'require' in _buf:
            _buf = _buf.split(' require ')
            self.rules[_buf[0]] = _buf[1] 
        elif 'Wanted by the State' in _buf:
            _buf = _buf.split('Wanted by the State: ')
            self.wanted = _buf[1:]
        else:
            _buf = _buf.split(' citizens of ')
            match _buf[0]:
                case 'Allow':
                    self.allow_citizens = _buf[1:]
                case 'Deny':
                    self.deny_citizens = _buf[1:]


inspector = Inspector()
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan
Citizens of Arstotzka require ID card
Citizens of Antegria, Republia, Obristan require polio vaccination"""

inspector.receive_bulletin(bulletin)
inspector.get_rules()

entrant1 = {
    "passport": """ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15"""
}

inspector.inspect(entrant1)