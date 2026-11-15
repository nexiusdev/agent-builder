import unittest,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate_deliverable import validate
class Deliverables(unittest.TestCase):
 def setUp(self): self.d=json.loads((ROOT/'templates/deliverable.json').read_text())
 def test_draft(self): self.assertEqual(validate(self.d),[])
 def test_missing_consumer(self): self.d['consumer_ids']=[];self.assertTrue(validate(self.d))
 def test_acceptance_requires_records(self): self.d['state']='accepted';self.assertTrue(validate(self.d))
 def test_delivery_requires_record(self):
  self.d.update(state='delivered',artifact_ref='artifact-v1',review_record='review-1');self.assertTrue(validate(self.d))
  self.d['delivery_record']='receipt-1';self.assertEqual(validate(self.d),[])
 def test_unknown_state(self): self.d['state']='perfect';self.assertTrue(validate(self.d))
 def test_non_object(self): self.assertTrue(validate([]))
