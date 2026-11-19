import importlib.util
import json
import unittest
import uuid
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("render_audit_visual", HERE / "render_audit_visual.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class RenderAuditVisualTests(unittest.TestCase):
    def setUp(self):
        self.example = HERE.parent / "examples" / "minimal-audit-bundle.json"

    def test_standalone_html_contains_core_views_and_bundle(self):
        bundle = json.loads(self.example.read_text(encoding="utf-8"))
        rendered = MODULE.render_bundle(bundle)
        self.assertIn("Synthetic qualified-service example", rendered)
        self.assertIn('id="graph"', rendered)
        self.assertIn('id="claims"', rendered)
        self.assertIn('id="timeline"', rendered)
        self.assertIn('id="companies"', rendered)
        self.assertIn('id="sources"', rendered)
        self.assertIn('id="relationList"', rendered)
        self.assertIn("showEdge", rendered)
        self.assertIn("status:p.status", rendered)
        self.assertIn("evidenceBlock(c.evidence_ids)", rendered)
        self.assertIn("exitClaim.claim_id", rendered)
        self.assertIn("b.offsetHeight+32", rendered)
        self.assertIn("full.length>34", rendered)
        self.assertIn("scroll-margin-top:72px", rendered)
        self.assertIn('"audit_id":"example-qualified-service"', rendered)
        self.assertNotIn("__AUDIT_DATA__", rendered)

    def test_script_writes_utf8_html(self):
        bundle = json.loads(self.example.read_text(encoding="utf-8"))
        tmp = HERE / ".test-output" / str(uuid.uuid4())
        tmp.mkdir(parents=True)
        try:
            output = tmp / "preview.html"
            output.write_text(MODULE.render_bundle(bundle), encoding="utf-8")
            self.assertTrue(output.read_text(encoding="utf-8").startswith("<!doctype html>"))
        finally:
            if output.exists():
                output.unlink()
            tmp.rmdir()
            tmp.parent.rmdir()


if __name__ == "__main__":
    unittest.main()
