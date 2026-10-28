#!/usr/bin/env python3
"""Kiểm máy và khung, không ghi gì. Mọi mục phải [ok] hoặc [-].

    python scripts/doctor.py
"""
import runpy
import sys
from pathlib import Path

sys.argv = [sys.argv[0], "--check"]
runpy.run_path(str(Path(__file__).with_name("setup.py")), run_name="__main__")
