####################################################################################################
# 
# @Project@ - @ProjectDescription@.
# Copyright (C) 2013 Fabrice Salvaire
# 
####################################################################################################

####################################################################################################

from PyQt4 import QtGui

####################################################################################################

from .Page import PageBase

####################################################################################################

# from .ui.BatteryPage_ui import Ui_form

####################################################################################################

class BatteryPage(PageBase):

    __page_name__ = 'battery'
    __page_title__ = 'Battery'

    ##############################################

    def __init__(self, parent=None):

        super(BatteryPage, self).__init__(parent)

        #self.form = Ui_form()
        #self.form.setupUi(self)

####################################################################################################
# 
# End
# 
####################################################################################################
