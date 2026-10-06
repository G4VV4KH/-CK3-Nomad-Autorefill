"""Static package checks. Native CK3 evidence is recorded separately."""
from __future__ import annotations
import codecs
import hashlib
import json
import re
from pathlib import Path

MOD = Path(__file__).resolve().parents[1]


def check():
    hashes = {}
    for dirname in ("common", "events", "gui", "localization"):
        for path in sorted((MOD / dirname).rglob("*")):
            if not path.is_file():
                continue
            raw = path.read_bytes()
            text = raw.decode("utf-8-sig")
            rel = path.relative_to(MOD).as_posix()
            hashes[rel] = hashlib.sha256(raw).hexdigest()
            if path.suffix == ".yml":
                assert raw.startswith(codecs.BOM_UTF8), f"Missing UTF-8 BOM: {rel}"
                continue
            # Strip quoted strings and comments together so # in GUI colors is safe.
            tokens = re.sub(r'"(?:[^"\\]|\\.)*"|#[^\n]*', '', text)
            depth = 0
            for char in tokens:
                depth += (char == "{") - (char == "}")
                assert depth >= 0, f"Unexpected close brace: {rel}"
            assert depth == 0, f"Unclosed braces: {rel}"
    localizations = {}
    for language in ("english", "russian"):
        paths = list((MOD / "localization" / language).glob("*.yml"))
        assert paths, f"Missing {language}"
        entries = {}
        for path in paths:
            lines = path.read_text(encoding="utf-8-sig").splitlines()
            assert lines[0] == f"l_{language}:", f"Bad language header: {path}"
            for line in lines[1:]:
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                match = re.fullmatch(r'\s*([\w.-]+):\d+\s+"((?:[^"\\]|\\.)*)"\s*', line)
                assert match, f"Malformed localization: {line}"
                assert match[1] not in entries, f"Duplicate key: {match[1]}"
                entries[match[1]] = match[2]
        localizations[language] = entries
    assert localizations["english"].keys() == localizations["russian"].keys(), "Translation keys differ"
    gui = (MOD / "gui/na_autorefill.gui").read_text(encoding="utf-8-sig")
    used = set(re.findall(r'(?:text|tooltip)\s*=\s*"(na_[\w]+)"', gui))
    assert used <= localizations["english"].keys(), f"Missing GUI strings: {used - localizations['english'].keys()}"
    descriptor = (MOD / "descriptor.mod").read_text()
    assert 'version="0.1.0"' in descriptor
    assert 'name="Nomad Autorefill"' in descriptor
    assert "remote_file_id" not in descriptor
    assert not (MOD / "common/governments").exists(), "Unexpected government override"
    print(json.dumps({"status": "PASS", "checked_text_files": len(hashes), "localization_keys_per_language": len(localizations["english"]), "runtime_sha256": hashes}, indent=2))


if __name__ == "__main__":
    check()
