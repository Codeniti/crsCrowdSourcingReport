#oggpnosn
#hkhr

class Task(object):
  def __init__(self,problemStatement, fund, contributor,  comment,status=False):
    self.problemStatement=problemStatement
    self.fund=fund
    self.contributor=contributor
    self.status=status
    self.comment=comment

class Manager(object):
  def __init__(self,name, organization, projectList=[]):
    self.name=name
    self.organization=organization
    self.projectList=projectList

class Organization(object):    
  def __init__(self, managerList=[], projectList=[] ):
    self.managerList=managerList
    self.projectList=projectList

class Project(object):
  def __linit__(seld,taskList,manager):
    self.taskList=taskList
    self.projectManager=manager

class Investor(object):
  def __init__(self, projectList):
    self.projectList=projectList


  
