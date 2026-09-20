r"""Run a .js file against a live tab, by URL fragment.

Exists because inline JS passed through a Python string loses its regex
escapes: \s, \d and \$ are mangled before CDP ever sees them. Reading the
JS from a file with encoding='utf-8' keeps it byte-exact.

Usage: python runjs.py <url-fragment> <file.js> [timeout]
"""
import sys, cdp

frag, path = sys.argv[1], sys.argv[2]
timeout = int(sys.argv[3]) if len(sys.argv) > 3 else 40
ws = cdp.conn(frag)
cdp.p(cdp.ev(ws, open(path, encoding='utf-8').read(), timeout=timeout))
