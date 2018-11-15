from AnyQt import QtCore, QtGui
from pybpod_alyx_module.module_api import AlyxModule
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlLabel


class AlyxDetails(AlyxModule, BaseWidget):

    TITLE = 'Subject Details'

    def __init__(self, _subject=None):
        BaseWidget.__init__(self, self.TITLE, parent_win=_subject.project)
        AlyxModule.__init__(self)

        self._nickname_text = ControlLabel('Nickname:')
        self._nickname = ControlLabel(_subject.name)
        self._nickname.selectable = True

        self._id_text = ControlLabel('ID:')
        self._id = ControlLabel(_subject.alyx_id)
        self._id.selectable = True

        # self._url_text = ControlLabel('URL:')
        # self._url = ControlLabel(_subject.alyx_url)
        # self._url.selectable = True

        self._responsible_user_text = ControlLabel('Responsible user:')
        self._responsible_user = ControlLabel(_subject.alyx_responsible_user)
        self._responsible_user.selectable = True

        self._birth_text = ControlLabel('Birth date:')
        self._birth = ControlLabel(_subject.alyx_birth_date)
        self._birth.selectable = True

        self._death_text = ControlLabel('Death date:')
        self._death = ControlLabel(_subject.alyx_death_date)
        self._death.selectable = True

        self._species_text = ControlLabel('Species:')
        self._species = ControlLabel(_subject.alyx_species)
        self._species.selectable = True

        self._sex_text = ControlLabel('Sex:')
        self._sex = ControlLabel(_subject.alyx_species)
        self._sex.selectable = True

        self._litter_text = ControlLabel('Litter:')
        self._litter = ControlLabel(_subject.alyx_litter)
        self._litter.selectable = True

        self._strain_text = ControlLabel('Strain:')
        self._strain = ControlLabel(_subject.alyx_strain)
        self._strain.selectable = True

        self._line_text = ControlLabel('Line:')
        self._line = ControlLabel(_subject.alyx_line)
        self._line.selectable = True

        self._description_text = ControlLabel('Description:')
        self._description = ControlLabel(_subject.alyx_description)
        self._description.selectable = True

        self._lab_text = ControlLabel('Lab:')
        self._lab = ControlLabel(_subject.alyx_lab)
        self._lab.selectable = True

        self._genotype_text = ControlLabel('Genotype:')
        self._genotype = ControlLabel(", ".join(map(str, _subject.alyx_genotype)) if _subject.alyx_genotype else None)
        self._genotype.selectable = True

        self._alive_text = ControlLabel('Alive:')
        self._alive = ControlLabel(str(_subject.alyx_alive))
        self._alive.selectable = True

        self._projects_text = ControlLabel('Projects:')
        self._projects = ControlLabel(", ".join(map(str, _subject.alyx_projects)) if _subject.alyx_projects else None)
        self._projects.selectable = True

        self.set_margin(10)

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

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
