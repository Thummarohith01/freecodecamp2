import unittest
import demographic_data_analyzer
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('adult.data.csv')
        self.results = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        race_count = self.results['race_count']
        expected_race_count = pd.Series({
            'White': 27816, 
            'Black': 3124, 
            'Asian-Pac-Islander': 1039, 
            'Amer-Indian-Eskimo': 311, 
            'Other': 271
        })
        pd.testing.assert_series_equal(race_count, expected_race_count)

    def test_average_age_men(self):
        average_age_men = self.results['average_age_men']
        self.assertAlmostEqual(average_age_men, 39.4, places=1)

    def test_percentage_bachelors(self):
        percentage_bachelors = self.results['percentage_bachelors']
        self.assertAlmostEqual(percentage_bachelors, 16.4, places=1)

    def test_higher_education_rich(self):
        higher_education_rich = self.results['higher_education_rich']
        self.assertAlmostEqual(higher_education_rich, 46.5, places=1)

    def test_lower_education_rich(self):
        lower_education_rich = self.results['lower_education_rich']
        self.assertAlmostEqual(lower_education_rich, 17.4, places=1)

    def test_min_work_hours(self):
        min_work_hours = self.results['min_work_hours']
        self.assertEqual(min_work_hours, 1)

    def test_rich_percentage(self):
        rich_percentage = self.results['rich_percentage']
        self.assertAlmostEqual(rich_percentage, 10.0, places=1)

    def test_highest_earning_country(self):
        highest_earning_country = self.results['highest_earning_country']
        self.assertEqual(highest_earning_country, 'United-States')

    def test_highest_earning_country_percentage(self):
        highest_earning_country_percentage = self.results['highest_earning_country_percentage']
        self.assertAlmostEqual(highest_earning_country_percentage, 91.0, places=1)

    def test_top_IN_occupation(self):
        top_IN_occupation = self.results['top_IN_occupation']
        self.assertEqual(top_IN_occupation, 'Prof-specialty')

if __name__ == "__main__":
    unittest.main()
