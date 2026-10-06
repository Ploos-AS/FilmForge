import unittest
from filmforge_cli import validate, plan, assets

P={"version":"0.1","kind":"FilmForgeProject","id":"x","title":"X","format":{"duration_target_minutes":18,"fps":24},"canon":{"universe_id":"u","characters":[],"locations":[],"props":[],"styles":[]},"scenes":[]}

class TestFilmForge(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate(P),[])

    def test_plan(self):
        self.assertEqual(plan(P)["shot_count"],0)

    def test_assets_block_planned_required(self):
        result=assets({"kind":"FilmForgeAssetRegistry","film_id":"x","assets":[
            {"id":"look","required":True,"status":"approved"},
            {"id":"face","required":True,"status":"planned"}]})
        self.assertTrue(result["ok"])
        self.assertFalse(result["ready_for_generation"])
        self.assertEqual(result["blocking_assets"],["face"])

    def test_assets_ready_when_required_approved_or_locked(self):
        result=assets({"kind":"FilmForgeAssetRegistry","film_id":"x","assets":[
            {"id":"look","required":True,"status":"approved"},
            {"id":"face","required":True,"status":"locked"},
            {"id":"optional","required":False,"status":"planned"}]})
        self.assertTrue(result["ready_for_generation"])
        self.assertEqual(result["blocking_assets"],[])

    def test_assets_reject_invalid_state(self):
        result=assets({"kind":"FilmForgeAssetRegistry","film_id":"x","assets":[
            {"id":"face","required":True,"status":"required-reference"}]})
        self.assertFalse(result["ok"])
        self.assertIn("face invalid status: required-reference",result["errors"])

if __name__=="__main__": unittest.main()
