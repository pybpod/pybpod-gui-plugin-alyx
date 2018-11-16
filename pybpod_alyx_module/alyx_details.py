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

        # self._url_text = ControlLabel('URL:')
        # self._url = ControlLabel(_subject.alyx_url)
        # self._url.selectable = True

        self._id_text = ControlLabel('ID:')
        self._id = ControlLabel(_subject.alyx_id)
        self._id.selectable = True

        self._responsible_user_text = ControlLabel('Responsible user:')
        self._responsible_user = ControlLabel(_subject.alyx_responsible_user)
        self._responsible_user.selectable = True

        self._birth_text = ControlLabel('Birth date:')
        self._birth = ControlLabel(_subject.alyx_birth_date)
        self._birth.selectable = True

        self._age_weeks_text = ControlLabel('Age (weeks):')
        self._age_weeks = ControlLabel(str(_subject.alyx_age_weeks))
        self._age_weeks.selectable = True

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

        self._source_text = ControlLabel('Source:')
        self._source = ControlLabel(_subject.alyx_source)
        self._source.selectable = True

        self._line_text = ControlLabel('Line:')
        self._line = ControlLabel(_subject.alyx_line)
        self._line.selectable = True

        self._projects_text = ControlLabel('Projects:')
        self._projects = ControlLabel(", ".join(map(str, _subject.alyx_projects)) if _subject.alyx_projects else None)
        self._projects.selectable = True

        self._lab_text = ControlLabel('Lab:')
        self._lab = ControlLabel(_subject.alyx_lab)
        self._lab.selectable = True

        self._genotype_text = ControlLabel('Genotype:')
        self._genotype = ControlLabel(", ".join(map(str, _subject.alyx_genotype)) if _subject.alyx_genotype else None)
        self._genotype.selectable = True

        self._description_text = ControlLabel('Description:')
        self._description = ControlLabel(_subject.alyx_description)
        self._description.selectable = True

        self._weighings_text = ControlLabel('Weighings:')
        self._weighings = ControlLabel(", ".join(map(str, _subject.alyx_weighings)) if _subject.alyx_weighings else None)
        self._weighings.selectable = True

        self._reference_weight_text = ControlLabel('Reference weight:')
        self._reference_weight = ControlLabel(_subject.alyx_reference_weight)
        self._reference_weight.selectable = True

        self._water_administrations_text = ControlLabel('Water admninistrations:')
        self._water_administrations = ControlLabel( ", ".join(map(str, _subject.alyx_water_administrations)) if _subject.alyx_water_administrations else None)
        self._water_administrations.selectable = True

        self._last_water_restriction_text = ControlLabel('Last water restriction:')
        self._last_water_restriction = ControlLabel(_subject.alyx_last_water_restriction)
        self._last_water_restriction.selectable = True

        self._expected_water_text = ControlLabel('Expected water:')
        self._expected_water = ControlLabel(str(_subject.alyx_expected_water))
        self._expected_water.selectable = True

        self._remaining_water_text = ControlLabel('Remaining water:')
        self._remaining_water = ControlLabel(str(_subject.alyx_remaining_water))
        self._remaining_water.selectable = True

        self.set_margin(10)

        self.formset = [
            ('_nickname_text', '_nickname'),
            # ('_url_text', '_url'),
            ('_id_text', '_id'),
            ('_responsible_user_text', '_responsible_user'),
            ('_birth_text', '_birth'),
            ('_age_weeks_text', '_age_weeks'),
            ('_death_text', '_death'),
            ('_species_text', '_species'),
            ('_sex_text', '_sex'),
            ('_litter_text', '_litter'),
            ('_strain_text', '_strain'),
            ('_source_text', '_source'),
            ('_line_text', '_line'),
            ('_projects_text', '_projects'),
            ('_lab_text', '_lab'),
            ('_genotype_text', '_genotype'),
            ('_description_text', '_description'),
            ('_weighings_text', '_weighings'),
            ('_reference_weight_text', '_reference_weight'),
            ('_water_administrations_text', '_water_administrations'),
            ('_last_water_restriction_text', '_last_water_restriction'),
            ('_expected_water_text', '_expected_water'),
            ('_remaining_water_text', '_remaining_water'),
        ]

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
