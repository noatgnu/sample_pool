from unittest import TestCase

import pandas as pd

from sample_pool.experiment import Experiment


class TestExperiment(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.samples = [
            "Abundance: 126",
            "Abundance: 127N",
            "Abundance: 127C",
            "Abundance: 128N",
            "Abundance: 128C",
            "Abundance: 129N",
            "Abundance: 129C",
            "Abundance: 130N",
            "Abundance: 130C",
            "Abundance: 131N",
            "Abundance: 131C",
            "Abundance: 132N",
            "Abundance: 132C",
            "Abundance: 133N",
            "Abundance: 133C"
        ]
        self.path = r"Z:\ALESSI\Toan\For_TMT mini pool\RN_220625_Hippo-TiO2_15TMT_Minipool_PSMs.txt"
        self.df = pd.read_csv(self.path, sep="\t")

    def test_calculate_sum(self):
        exp = Experiment(self.df, self.samples)
        s = exp.calculate_sum()
        print(s)

    def test_aliquot_ratio(self):
        exp = Experiment(self.df, self.samples)
        s = exp.get_aliquot_size("Abundance: 127N")
        print(s)

