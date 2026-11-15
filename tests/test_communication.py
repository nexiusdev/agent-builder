import unittest,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_message import validate
class Communication(unittest.TestCase):
 def setUp(self): self.example=json.loads((ROOT/'templates/message.json').read_text())
 def test_example(self): self.assertEqual(validate(self.example),[])
 def test_missing_scope(self): self.example.pop('scope');self.assertTrue(validate(self.example))
 def test_bad_type(self): self.example['type']='override-authority';self.assertTrue(validate(self.example))
 def test_bad_state(self): self.example['state']='done';self.assertTrue(validate(self.example))
 def test_bad_evidence(self): self.example['evidence_refs']='secret';self.assertTrue(validate(self.example))
 def test_non_object(self): self.assertTrue(validate([]))
