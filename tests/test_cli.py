import unittest
from filmforge_cli import validate, plan

P={"version":"0.1","kind":"FilmForgeProject","id":"x","title":"X","format":{"duration_target_minutes":18,"fps":24},"canon":{"universe_id":"u","characters":[],"locations":[],"props":[],"styles":[]},"scenes":[]}

class TestFilmForge(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate(P),[])
    def test_plan(self): self.assertEqual(plan(P)["shot_count"],0)
if __name__=="__main__": unittest.main()
