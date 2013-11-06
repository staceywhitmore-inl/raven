'''
Created on Mar 8, 2013

@author: crisr
'''
from __future__ import division, print_function, unicode_literals, absolute_import
import warnings
warnings.simplefilter('default',DeprecationWarning)

import time
from BaseType import BaseType


class Test(BaseType):
  ''' 
  a genral class containing the distributions
  '''
  def __init__(self):
    BaseType.__init__(self)
    self.toBeTested  = []
    self.tolerance = 0.0

  def readMoreXML(self,xmlNode):
    #try: 
    self.toBeTested = xmlNode.text.split(',')
    #except? raise IOError('not found variable list to be tested in tester '+self.name)
    #try: 
    self.name = xmlNode.attrib['tolerance']
    #except? raise IOError('not found tolerance for tester '+self.name)

  def addInitParams(self,tempDict):
    tempDict['toBeTested'] = self.toBeTested
    tempDict['tolerance' ] = self.tolerance

  def reset(self):
    return

  def checkConvergence(self,inDictionary):  #if a ROM present ???
    return

  def getROM(self,ROM):
    return

  def getOutput(self,ROM):
    return

  def testOutput(self):
    return



class Sigma(Test):
  pass



class Integral(Test):
  pass

'''
 Interface Dictionary (factory) (private)
'''
__base                      = 'Data'
__interFaceDict             = {}
__interFaceDict['Sigma'   ] = Sigma
__interFaceDict['Integral'] = Integral
__knownTypes                = __interFaceDict.keys()

def knonwnTypes():
  return __knownTypes

def returnInstance(Type):
  '''return one instance of Type''' 
  try: return __interFaceDict[Type]()
  except KeyError: raise NameError('not known '+__base+' type '+Type)  

