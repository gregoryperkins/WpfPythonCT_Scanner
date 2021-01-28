import wpf
import clr
import System
from System.Windows import Application, Window
from System.Collections.ObjectModel import *
from System.ComponentModel import INotifyPropertyChanged, PropertyChangedEventArgs
import os
import xml.etree.ElementTree as et
#import time
#from exceptions import ValueError
import pyevent
import clrtype


# in case you do not want to use the search path option in VS, then, use
#import sys
#sys.path.append(r'C:\Users\dguzun\Source\Repos\WpfPyXact\misc')

#============== Code snippets that may be used ==================
    #"""
    #    use setter getter.
    #    IronPython 2.6 or later.
    #"""
    #@property
    #def PartName(self):
    #    return self._PartName

    #@PartName.setter
    #def PartName(self, value):
    #    self._PartName = value
    #    self.OnPropertyChanged("PartName")



            #self._partDescriptions = ObservableCollection[PartDescription]()
            #for entry in self._partList:
            #    en = PartDescription()
            #    item = ComboBoxItem()
            #    item.Content = en
            #    en.PartName = entry
            #    self._partDescriptions.Add(en)

            #combo = ComboBox()
            #for partname in self._partList:
            #    item = ComboBoxItem()
            #    item.Content = partname
            #    item.FontSize = 8
            #    combo.Items.Add(item)

    #@property
    #def PartListCombo(self):
    #    return self._partDescriptions

    #@PartListCombo.setter
    #def PartListCombo(self, value):
    #    self._partDescriptions = value
   
    
#================================================================

from varian import *
from automation import *
from editor import *
from sleep import *
from demosource import *
from hasealed1 import *
from motorizeddoorio import *



#====== Global variables ==========================

WorkDir="D:/Temp/RX-Solutions/Tomo"
#WorkDir="C:/autoTESTING"

CalMacroName="calibrations.macro"
TomoMacroName="tomography.macro"
ReconstructionXml="unireconstruction.xml"

Part1 = {"name" : "Part1", "macro" : WorkDir + "/Part1/" + CalMacroName, "unireconstruction" :  WorkDir + "/Part1/unireconstruction.xml", "tomo_macro" : WorkDir + "/Part1/" +TomoMacroName}
Part2 = {"name" : "Part2", "macro" : WorkDir + "/Part2/" + CalMacroName, "unireconstruction" :  WorkDir + "/Part2/unireconstruction.xml", "tomo_macro" : WorkDir + "/Part2/" +TomoMacroName}
Part3 = {"name" : "Part3", "macro" : WorkDir + "/Part3/" + CalMacroName, "unireconstruction" :  WorkDir + "/Part3/unireconstruction.xml", "tomo_macro" : WorkDir + "/Part3/" +TomoMacroName}
Part4 = {"name" : "Part3", "macro" : WorkDir + "/Part4/" + CalMacroName, "unireconstruction" :  WorkDir + "/Part4/unireconstruction.xml", "tomo_macro" : WorkDir + "/Part4/" +TomoMacroName}


partDB = [Part1, Part2, Part3, Part4]

simulation=False

#===================================================
# Watch out for the order of class definitions since one is dependnet on the other. Order matters in Python

class MacroXmlParser:
    def __init__(self):
        self.path = ""

    def LoadMacro(self, path):
        self.path = path
        # use the parse() function to load and parse an XML file
        self.xmltree = et.parse(path)
        return self.xmltree

class notify_property(property):
    def __init__(self, getter):
        def newgetter(slf):
            try:
                return getter(slf)
            except AttributeError:
                return None
        super(notify_property, self).__init__(newgetter)
    def setter(self, setter):
        def newsetter(slf, newvalue):
            oldvalue = self.fget(slf)
            if oldvalue != newvalue:
                setter(slf, newvalue)
                slf.OnPropertyChanged(setter.__name__)
        return property(
            fget=self.fget,
            fset=newsetter,
            fdel=self.fdel,
            doc=self.__doc__)

class PartListEntry:
    def __init__(self, name):
        self._partName = name

    @notify_property
    def PartName(self):
        return self._partName

    @PartName.setter
    def PartName(self, value):
        self._partName = value
        self.OnPropertyChanged("PartName")    

class NotifyPropertyChangedBase(INotifyPropertyChanged):
    PropertyChanged = None

    def __init__(self):
        self.PropertyChanged, self._propertyChangedCaller = pyevent.make_event()

    def add_PropertyChanged(self, value):
        self.PropertyChanged += value

    def remove_PropertyChanged(self, value):
        self.PropertyChanged -= value

    def OnPropertyChanged(self, propertyName):
        if self.PropertyChanged is not None:
            self._propertyChangedCaller(self, PropertyChangedEventArgs(propertyName))

    def init_view(self, view):
        xaml = view
        self.view = XamlLoader(xaml).Root
        self.view.DataContext = self

    def declareNotifiable(self, *symbols):
        for symbol in symbols:
            self.defineNotifiableProperty(symbol)

    def defineNotifiableProperty(self, symbol):
        dnp = """
import sys
sys.path.append(__file__)
from NotifyProperty import *
@notify_property
def {0}(self):
    return self._{0}   

@{0}.setter
def {0}(self, value):
    self._{0} = value
""".format(symbol)
        d = globals()
        exec dnp.strip() in d
        setattr(self.__class__, symbol, d[symbol])
        exec("self.{0} = ''".format(symbol))
            
class PartDescriptionEntry(NotifyPropertyChangedBase):
    def __init__(self, name):
        super(PartDescriptionEntry, self).__init__()
        #self.defineNotifiableProperty("PartName")
        self._partName = name

    @notify_property
    def PartName(self):
        return self._partName

    @PartName.setter
    def PartName(self, value):
        self._partName = value
        self.OnPropertyChanged("PartName")

class ViewModel(NotifyPropertyChangedBase):

    def __init__(self, model):
        try:
            super(ViewModel, self).__init__()
            self._model = model

            # Templates/Parts available locally
            self._partDescriptions = model._partDescriptions

            # Selected template index
            self._partDescriptionSelected = 0

            # restorepoints for current/selected template
            self._restorePoints = ObservableCollection[System.String]()

            # Current plugin run status
            self.pluginStarted = False

            # Currently active plugin
            self.plugin=None
        except Exception as e:
            print(e)

    def LoadTemplate(self):
        self.loadMacroToUI()

    def loadMacroToUI(self):
        xmlObj = MacroXmlParser()

        xmlTree = xmlObj.LoadMacro(partDB[self._partDescriptionSelected]["macro"])     
        root = xmlTree.getroot()

        # load only the calibrations.macro to Xact's macro editor
        try:
            if simulation != True:
                self._model.macroeditor.cmdClear()
                self._model.macroeditor.cmdLoad(partDB[self._partDescriptionSelected]["macro"])
        except Exception as e:
            print(e)
            #return
        
        self._restorePoints.Clear()

        # extract macro point names and populate UI
        for subelm_child in list(root.iter("point")):
            print(subelm_child.tag, " ", subelm_child.attrib)
            #self.gCmdList.insert('end', subelm_child.attrib['name'])  
            self._restorePoints.Add(subelm_child.attrib['name'])

        # add tomography.macro info into UI as well (not into Xact macro editor)
        xmlTree2 = xmlObj.LoadMacro(partDB[self._partDescriptionSelected]["tomo_macro"])
        root = xmlTree2.getroot()
        for subelm_child in list(root.iter("point")):
            print(subelm_child.tag, " ", subelm_child.attrib)
            #self.gCmdList.insert('end', subelm_child.attrib['name'])
            self._restorePoints.Add(subelm_child.attrib['name'])
            xmlTree.getroot().append(subelm_child)

        self.xmlTree = xmlTree

    @notify_property
    def PartDescriptions(self):
        return self._partDescriptions

    @PartDescriptions.setter
    def PartDescriptions(self, value):
        self._partDescriptions = value
        self.OnPropertyChanged("PartDescriptions")

    @notify_property
    def SelectedPartDescription(self):
        return self._partDescriptionSelected

    @SelectedPartDescription.setter
    def SelectedPartDescription(self, value):
        self._partDescriptionSelected = value
        self.OnPropertyChanged("SelectedPartDescription")

    @notify_property
    def RestorePoints(self):
        return self._restorePoints

    @RestorePoints.setter
    def RestorePoints(self, value):
        self._restorePoints = value
        self.OnPropertyChanged("RestorePoints")

class Model():
    def __init__(self):
        try:
            # get part list (populate global partDB and listview control container self._partlist)
            self._partDescriptions = ObservableCollection[System.String]()
            for entry in self.getPartList():
                self._partDescriptions.Add(entry)

            # Imager
            self.imager=Varian('Imager')

            # Source
            if(simulation==True):
                self.xray=Demosource('Xray150')
            else:
                self.xray=Hasealed1("Xray150")

            # Automation
            self.automation=Automation('Automation')

            # MacroEditor
            self.macroeditor=Editor('MacroEditor')
        except Exception as e:
            print(e)

    def getPartList(self):
        list_subfolders_with_paths = [os.path.join(WorkDir, f) for f in os.listdir(WorkDir) if os.path.isdir(os.path.join(WorkDir, f))]
        found_cal_files = list()
        found_tomo_files = list()
        for f in list_subfolders_with_paths:
            list_files = self.getListOfFiles(f)
            for fi in list_files:
                if "calibrations.macro" in fi:
                    found_cal_files.append(fi)
                if "tomography.macro" in fi:
                    found_tomo_files.append(fi)

        listOfCalFiles = list()
        listOfTomoFiles = list()
        listOfParts = list()
        for (dirpath, dirnames, filenames) in os.walk(WorkDir):
            listOfCalFiles = [os.path.join(dirpath, file) for file in filenames if "calibrations.macro" in file]
            listOfTomoFiles = [os.path.join(dirpath, file) for file in filenames if "tomography.macro" in file]
            if(len(listOfCalFiles) == 1 and len(listOfTomoFiles) == 1):
                listOfParts += [os.path.basename(os.path.dirname(listOfCalFiles[0]))]

        listOfPartsOut = list()
        # partDB is a global
        if len(listOfParts) > 0:
            #partDB.clear()
            partDB = []
            for part in listOfParts:
                listOfPartsOut.append(part)
                partDB.append(
                    {"name" : part, 
                        "macro" : WorkDir + "/" + part +"/" + CalMacroName, 
                        "unireconstruction" :  WorkDir + "/" + part +"/" + ReconstructionXml, 
                        "tomo_macro" : WorkDir + "/" + part +"/" +TomoMacroName})
        else:
            # this happens if no parts avail. Then, use some "simulated" list define in the Global section
            for part in partDB:
                listOfPartsOut.append(part["name"])
        return listOfPartsOut

    def getListOfFiles(self, dirName):
        # create a list of file and sub directories 
        # names in the given directory 
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory 
            if os.path.isdir(fullPath):
                #allFiles = allFiles + getListOfFiles(fullPath)
                print("")
            else:
                allFiles.append(fullPath)                
        return allFiles




class MyWindow(Window):
    def __init__(self):
        try:
            ui = wpf.LoadComponent(self, 'WpfPyXact.xaml')
            model = Model()
            viewModel = ViewModel(model)
            self.DataContext = viewModel

            ui.LoadTemplateBtn.Click += self.LoadTemplateBtn_Click
        except Exception as e:
            print(e)

    def LoadTemplateBtn_Click(self, sender, e):
        try:
            self.DataContext.LoadTemplate()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        Application().Run(MyWindow())
    except Exception as e:
        print(e)
