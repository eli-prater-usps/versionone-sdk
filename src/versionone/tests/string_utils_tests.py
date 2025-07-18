import unittest
from v1pysdk.string_utils import split_attribute

class TestStringUtils(unittest.TestCase):
    def test_split_attribute(self):
        self.assertEqual(['[testing]]'],split_attribute('[testing]]'))
        self.assertEqual(['[[testing]'],split_attribute('[[testing]'))
        self.assertEqual(['testing','a','sentence','is','difficult'],split_attribute('testing.a.sentence.is.difficult'))
        self.assertEqual(['testing','[a.sentence]','is','difficult'],split_attribute('testing.[a.sentence].is.difficult'))
        self.assertEqual(['testing[.a.sentence]','is', 'difficult'],split_attribute('testing[.a.sentence].is.difficult'))
        self.assertEqual(['testing','a[.sentence.]is','difficult'],split_attribute('testing.a[.sentence.]is.difficult'))
        self.assertEqual(['testing','a','sentence','is','difficult]'],split_attribute('testing.a.sentence.is.difficult]'))
        self.assertEqual(['testing', 'a','sentence','is',']difficult'],split_attribute('testing.a.sentence.is.]difficult'))
        self.assertEqual(['[testing.a.sentence.is]','difficult'],split_attribute('[testing.a.sentence.is].difficult'))
        self.assertEqual(['[testing.][a.sentence.is.difficult]'],split_attribute('[testing.][a.sentence.is.difficult]'))
        self.assertEqual(['[testing]','[a]','[sentence]','[is]','[difficult]'],
                          split_attribute('[testing].[a].[sentence].[is].[difficult]'))
        self.assertEqual(['testing','[[a.sentence.]is]','difficult'],
                          split_attribute('testing.[[a.sentence.]is].difficult'))
        self.assertEqual(["History[Status.Name='Done']"],split_attribute("History[Status.Name='Done']"))
        self.assertEqual(["ParentMeAndUp[Scope.Workitems.@Count='2']"],
                          split_attribute("ParentMeAndUp[Scope.Workitems.@Count='2']") )
        self.assertEqual(["Owners","OwnedWorkitems[ChildrenMeAndDown=$]","@DistinctCount"],
                          split_attribute("Owners.OwnedWorkitems[ChildrenMeAndDown=$].@DistinctCount") )
        self.assertEqual(["Workitems[ParentAndUp[Scope=$].@Count='1']"],
                          split_attribute("Workitems[ParentAndUp[Scope=$].@Count='1']") )
        self.assertEqual(["RegressionPlan","RegressionSuites[AssetState!='Dead']","TestSets[AssetState!='Dead']","Environment", "@DistinctCount"]
                          ,split_attribute("RegressionPlan.RegressionSuites[AssetState!='Dead'].TestSets[AssetState!='Dead'].Environment.@DistinctCount") )
        self.assertEqual(["Scope","ChildrenMeAndDown","Workitems:Story[ChildrenMeAndDown.ToDo.@Sum!='0.0']","Estimate","@Sum"]
                          ,split_attribute("Scope.ChildrenMeAndDown.Workitems:Story[ChildrenMeAndDown.ToDo.@Sum!='0.0'].Estimate.@Sum") )

if __name__ == '__main__':
    unittest.main()