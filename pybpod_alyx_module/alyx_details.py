from AnyQt import QtCore
from pybpod_alyx_module.module_api import AlyxModule
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlLabel


class AlyxDetails(AlyxModule, BaseWidget):

    TITLE = 'Subject Details'

    def __init__(self, _subject):
        BaseWidget.__init__(self, self.TITLE)
        AlyxModule.__init__(self)

        self._nickname_text = ControlLabel('Nickname:')
        self._nickname = ControlLabel(_subject.name)

        self._id_text = ControlLabel('ID:')
        self._id = ControlLabel(_subject.alyx_id)

        # self._url_text = ControlLabel('URL:')
        # self._url = ControlLabel(_subject.alyx_url)

        self._responsible_user_text = ControlLabel('Responsible user:')
        self._responsible_user = ControlLabel(_subject.alyx_responsible_user)

        self._birth_text = ControlLabel('Birth date:')
        self._birth = ControlLabel(_subject.alyx_birth_date)

        self._death_text = ControlLabel('Death date:')
        self._death = ControlLabel(_subject.alyx_death_date)

        self._species_text = ControlLabel('Species:')
        self._species = ControlLabel(_subject.alyx_species)

        self._sex_text = ControlLabel('Sex:')
        self._sex = ControlLabel(_subject.alyx_species)

        self._litter_text = ControlLabel('Litter:')
        self._litter = ControlLabel(_subject.alyx_litter)

        self._strain_text = ControlLabel('Strain:')
        self._strain = ControlLabel(_subject.alyx_strain)

        self._line_text = ControlLabel('Line:')
        self._line = ControlLabel(_subject.alyx_line)

        self._description_text = ControlLabel('Description:')
        self._description = ControlLabel(_subject.alyx_description)

        self._lab_text = ControlLabel('Lab:')
        self._lab = ControlLabel(_subject.alyx_lab)

        self._genotype_text = ControlLabel('Genotype:')
        self._genotype = ControlLabel("\n".join(map(str, _subject.alyx_genotype)) if _subject.alyx_genotype else None)

        self._alive_text = ControlLabel('Alive:')
        self._alive = ControlLabel(str(_subject.alyx_alive))

        self._projects_text = ControlLabel('Projects:')
        self._projects = ControlLabel("\n".join(map(str, _subject.alyx_projects)) if _subject.alyx_projects else None)

        # {
        #     "nickname": "test_mouse0",
        #     "id": "ab627ee2-e438-4fcb-9eea-d0ab779c2de6",
        #     "url": "https://dev.alyx.internationalbrainlab.org/subjects/test_mouse0",
        #     "responsible_user": "test_user",
        #     "birth_date": "2018-11-13",
        #     "death_date": null,
        #     "species": "Laboratory mouse",
        #     "sex": "M",
        #     "litter": "Ai148.Vg_L_003",
        #     "strain": "C57BL/6J",
        #     "line": "DAT-IRES-Cre",
        #     "description": "",
        #     "lab": null,
        #     "genotype": [],
        #     "alive": true,
        #     "projects": [
        #         "ibl_mainenlab"
        #     ]
        # },

        self.set_margin(10)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        #self._nickname.enabled = False
        self.formset = [
            ('_nickname_text', '_nickname'),
            ('_id_text', '_id'),
            # ('_url_text', '_url'),
            ('_responsible_user_text', '_responsible_user'),
            ('_birth_text', '_birth'),
            ('_death_text', '_death'),
            ('_species_text', '_species'),
            ('_sex_text', '_sex'),
            ('_litter_text', '_litter'),
            ('_strain_text', '_strain'),
            ('_line_text', '_line'),
            ('_description_text', '_description'),
            ('_lab_text', '_lab'),
            ('_genotype_text', '_genotype'),
            ('_alive_text', '_alive'),
            ('_projects_text', '_projects')
        ]