import logging
import os
import pybpodgui_api
from pybpod_alyx_module.alyx_details import AlyxDetails
from pybpodgui_plugin.models.subject.subject_uibusy import SubjectUIBusy
from sca.formats import json

logger = logging.getLogger(__name__)


class AlyxSubject(SubjectUIBusy):

    def __init__(self, project):
        super(AlyxSubject, self).__init__(project)

    def add_alyx_info(self, jsondata):
        print(json.dumps(jsondata))
        # print(self.uuid4)
        self.name = jsondata['nickname']
        self.alyx_nickname = jsondata['nickname']
        self.alyx_id = jsondata['id']
        self.alyx_url = jsondata['url']
        self.alyx_responsible_user = jsondata['responsible_user']
        self.alyx_birth_date = jsondata['birth_date']
        self.alyx_death_date = jsondata['death_date']
        self.alyx_species = jsondata['species']
        self.alyx_sex = jsondata['sex']
        self.alyx_litter = jsondata['litter']
        self.alyx_strain = jsondata['strain']
        self.alyx_line = jsondata['line']
        self.alyx_description = jsondata['description']
        self.alyx_lab = jsondata['lab']
        self.alyx_genotype = jsondata['genotype']
        self.alyx_alive = jsondata['alive']
        self.alyx_projects = jsondata['projects']

        # print(self.uuid4)
        self._tree.add_popup_menu_option('Alyx Details', self.showdetails, item=self.node)
        

    def save(self):
        """
        Save subject data on filesystem.

        :ivar str project_path: Project path.  
        :return: Dictionary containing the setup info to save.  
        :rtype: dict
        """
        if not hasattr(self, 'alyx_id'):
            super().save()
            return

        if not self.name:
            logger.warning("Skipping subject without name")
            return None
        else:  
            if not os.path.exists(self.path): os.makedirs(self.path)

            if self.data:
                data = self.data
            else:
                data = json.scadict(
                    uuid4_id=self.uuid4,
                    software='PyBpod GUI API v'+str(pybpodgui_api.__version__),
                    def_url ='http://pybpod.readthedocs.org',
                    def_text='This file contains information about a subject used on PyBpod GUI.',
                )
            data['nickname'] = self.alyx_nickname
            data['alyx_id'] = self.alyx_id
            data['url'] = self.alyx_url
            data['responsible_user'] = self.alyx_responsible_user
            data['birth_date'] = self.alyx_birth_date
            data['death_date'] = self.alyx_death_date
            data['species'] = self.alyx_species
            data['sex'] = self.alyx_sex
            data['litter'] = self.alyx_litter
            data['strain'] = self.alyx_strain
            data['line'] = self.alyx_line
            data['description'] = self.alyx_description
            data['lab'] = self.alyx_lab
            data['genotype'] = self.alyx_genotype
            data['alive'] = self.alyx_alive
            data['projects'] = self.alyx_projects

            config_path = os.path.join(self.path, self.name+'.json')
            with open(config_path, 'w') as fstream: json.dump(data, fstream)

    def toJSON(self):
        if not hasattr(self, 'alyx_id'):
            return super().toJSON()

        data = json.scadict(
                    uuid4_id=self.uuid4,
                    software='PyBpod GUI API v'+str(pybpodgui_api.__version__),
                    def_url ='http://pybpod.readthedocs.org',
                    def_text='This file contains information about a subject used on PyBpod GUI.',
                )
        data['name'] = self.name
        data['uuid4'] = self.uuid4
        data['nickname'] = self.alyx_nickname
        data['alyx_id'] = self.alyx_id
        data['url'] = self.alyx_url
        data['responsible_user'] = self.alyx_responsible_user
        data['birth_date'] = self.alyx_birth_date
        data['death_date'] = self.alyx_death_date
        data['species'] = self.alyx_species
        data['sex'] = self.alyx_sex
        data['litter'] = self.alyx_litter
        data['strain'] = self.alyx_strain
        data['line'] = self.alyx_line
        data['description'] = self.alyx_description
        data['lab'] = self.alyx_lab
        data['genotype'] = self.alyx_genotype
        data['alive'] = self.alyx_alive
        data['projects'] = self.alyx_projects

        return json.dumps(data)

    def load(self, path):
        """
        Load subject data from filesystem

        :ivar str subject_path: Path of the subject
        :ivar dict data: data object that contains all subject info
        """
        print('LOADING SUBJECT ALYX')
        self.name  = os.path.basename(path)

        try:
            with open( os.path.join(self.path, self.name+'.json'), 'r' ) as stream:
                self.data = data = json.load(stream)

            if data.get('alyx_id', None) is None:
                super().load(path)
                return

            #self.name = data.get('name', None)
            self.uuid4 = data.uuid4 if data.uuid4 else self.uuid4
            self.alyx_nickname = data.get('nickname', None)
            self.alyx_id = data.get('alyx_id', None)
            self.alyx_url = data.get('url', None)
            self.alyx_responsible_user = data.get('responsible_user', None)
            self.alyx_birth_date = data.get('birth_date', None)
            self.alyx_death_date = data.get('death_date', None)
            self.alyx_species = data.get('species', None)
            self.alyx_sex = data.get('sex', None)
            self.alyx_litter = data.get('litter', None)
            self.alyx_strain = data.get('strain', None)
            self.alyx_line = data.get('line', None)
            self.alyx_description = data.get('description', None)
            self.alyx_lab = data.get('lab', None)
            self.alyx_genotype = data.get('genotype', None)
            self.alyx_alive = data.get('alive', None)
            self.alyx_projects = data.get('projects', None)

            self._tree.add_popup_menu_option('Alyx Details', self.showdetails, item=self.node)

        except:
            raise Exception(f'There was an error loading the configuration file for the subject [{self.name}]. File not found.')

    def create_treenode(self, tree):
        """
        Creates node for this board under the parent "Boards" node.

        This methods is called when the board is first created.

        The following actions get assigned to node:
            * *Remove*: :meth:`BoardTreeNode.remove`.

        Sets key events:
            * :meth:`BoardTreeNode.node_key_pressed_event`


        :param tree: the project tree
        :type tree: pyforms.controls.ControlTree
        :return: new created node
        :return type: QTreeWidgetItem
        """
        super().create_treenode(tree)

        # save the tree so we can add the pop-up on load and add_alyx_info for those subjects that require it
        self._tree = tree

        return self.node

    def showdetails(self):
        if not hasattr(self, 'detailswindow'):
            self.detailswindow = AlyxDetails(self)
        self.detailswindow.show()
        return self.detailswindow

'''
test_subject = {
    "nickname": "test_subject_posted",
    "responsible_user": "test_user",  # Required
    "birth_date": None,
    "death_date": None,
    "species": None,
    "sex": 'U',  # Required
    "litter": None,
    "strain": None,
    "line": None,
    "description": "Some description",
    "genotype": []  # Required?
}
'''

'''
{
    'species': 'mouse', 
    'genotype': [], 
    'litter': None, 
    'alive': True, 
    'url': 'http://alyx.champalimaud.pt:8000/subjects/4577', 
    'line': None, 
    'birth_date': '2017-04-11', 
    'responsible_user': 'ines', 
    'sex': 'F', 
    'death_date': None, 
    'description': '', 
    'nickname': '4577', 
    'strain': 'VGlut-2-ChR2-het', 
    'id': '27705345-f49a-4483-aec8-313fc01d2c1f'
} 


'''     