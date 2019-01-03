import pyforms
from AnyQt import QtGui, QtCore
from AnyQt.QtWidgets import QLineEdit
from confapp import conf
from pybpod_alyx_module.models.subject.alyx_subject import AlyxSubject
from pybpod_alyx_module.module_api import AlyxModule
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText, ControlButton, ControlLabel


class AlyxModuleGUI(AlyxModule, BaseWidget):

    TITLE = 'Alyx connection'

    def __init__(self, _project=None):
        BaseWidget.__init__(self, self.TITLE, parent_win=_project)
        AlyxModule.__init__(self)

        self.project = _project
        
        self._addressbox = ControlText('Address')
        self._username = ControlText('User:')
        self._password = ControlText('Password:')
        self._username = ControlText('User:',default = conf.ALYX_PLUGIN_USERNAME)
        self._password = ControlText('Password:', default = conf.ALYX_PLUGIN_PASSWORD)
        self._connect_btn = ControlButton('Connect',default = self._connect)
        self._status_lbl = ControlLabel('Status: Not Connected')
        self._getsubjects_btn = ControlButton('Get Subjects', default = self._get_subjects)
        self._getsubjects_btn.enabled = False
        self.set_margin(10)

        self._addressbox.value = conf.ALYX_PLUGIN_ADDRESS
        self._addressbox.changed_event = self.setaddr

        if self.project.loggeduser is not None:
            self._username.value = self.project.loggeduser.name
        
        self._password.form.lineEdit.setEchoMode(QLineEdit.Password)

        self.formset = [
            '_addressbox',
            '_username',
            '_password',
            '_connect_btn',
            '_status_lbl',
            '_getsubjects_btn'
        ]

    def setaddr(self):
        self.api.setaddr(self._addressbox.value)

    def _connect(self):
        if self._connect_to_alyx(self._username.value,self._password.value):
            usersearch = self.project.find_user(self._username.value)
            if usersearch is None: # create this user on the project
                newuser = self.project.create_user()
                newuser.name = self._username.value
                newuser.node_double_clicked_event()
            else:
                usersearch.node_double_clicked_event()
            self.project.loggeduser.connection = 'ALYX'
            self._status_lbl.value = 'Status: CONNECTED'
            self.project.loggeduser = self.project.loggeduser
            self._getsubjects_btn.enabled = True

    def _get_subjects(self):
        result = self.get_alyx_subjects(self._username.value)
        replace_all = False
        ignore_all = False
        for subj in result:
            subjname = subj['nickname']
            existing = False
            for s in self.project.subjects:
                if s.name == subjname:
                    existing = True
                    if replace_all:
                        subj_info = self.get_alyx_subject_info(subjname)
                        s.add_alyx_info(subj_info)
                        continue
                    reply = self.question("Subject '{name}' already exists locally. Replace local details?".format(name=s.name), 'Update Subject', buttons=['no', 'yes', 'no_all', 'yes_all'])
                    if reply == 'yes':
                        subj_info = self.get_alyx_subject_info(subjname)
                        s.add_alyx_info(subj_info)
                    if reply == 'yes_all':
                        subj_info = self.get_alyx_subject_info(subjname)
                        s.add_alyx_info(subj_info)
                        replace_all = True
                    if reply == 'no_all':
                        ignore_all = True
                        break
            if ignore_all:
                break
            if not existing:
                subj_info = self.get_alyx_subject_info(subjname)
                # SubjectBase constructor adds Subject automatically to self.project so there's no need to add it here
                newsubject = AlyxSubject(self.project)
                newsubject.add_alyx_info(subj_info)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    pyforms.start_app(AlyxModuleGUI, geometry=(0, 0, 300, 300))
